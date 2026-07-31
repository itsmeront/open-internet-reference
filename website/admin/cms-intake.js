/*!
 * OIR Decap CMS intake helpers
 * - Auto-assign pending IDs on save (editors/AI rename later)
 * - Local draft autosave / restore for mobile leave-and-return
 * - Delete local draft control
 */
(function () {
  var STORAGE_PREFIX = "oir-cms-local-draft:";
  var LAST_KEY = "oir-cms-last-draft";
  var SAVE_INTERVAL_MS = 1500;
  var RESTORE_RETRY_MS = 400;
  var RESTORE_MAX_TRIES = 25;

  var COLLECTION_PREFIX = {
    organizations: function () {
      return "ORG";
    },
    people: function (data) {
      return data && data.type === "attorney" ? "ATT" : "PERSON";
    },
    legal: function (data) {
      if (!data) return "CASE";
      if (data.type === "statute" || data.type === "regulation") return "STAT";
      if (data.type === "topic") return "TOPIC";
      return "CASE";
    },
    sources: function () {
      return "SRC";
    },
    contacts: function () {
      return "CONTACT";
    },
  };

  function uniquePendingId(prefix) {
    var stamp = Date.now().toString(36).toUpperCase();
    var rand = Math.random().toString(36).slice(2, 6).toUpperCase();
    return prefix + "-PENDING-" + stamp + rand;
  }

  function ensureId(collection, data) {
    var current = data && data.id;
    // Keep real IDs when editing existing records (e.g. ORG-EFF).
    if (current && !/PENDING/i.test(String(current))) {
      return data;
    }
    var prefixFn = COLLECTION_PREFIX[collection];
    var prefix = prefixFn ? prefixFn(data) : "ORG";
    // Intake stubs use PENDING-*; AI/editors assign canonical IDs during review.
    return Object.assign({}, data, { id: uniquePendingId(prefix) });
  }

  /* ---------- Local draft persistence ---------- */

  function collectionFromHash(hash) {
    var m = String(hash || "").match(/\/collections\/([^/]+)/);
    return m ? m[1] : null;
  }

  function isEditorHash(hash) {
    return /\/collections\/[^/]+\/(new|entries\/)/.test(String(hash || ""));
  }

  function draftStorageKey(hash) {
    return STORAGE_PREFIX + (hash || "#/");
  }

  function setNativeValue(el, value) {
    if (!el) return;
    var proto = Object.getPrototypeOf(el);
    var protoDesc = proto && Object.getOwnPropertyDescriptor(proto, "value");
    var ownDesc = Object.getOwnPropertyDescriptor(el, "value");
    if (protoDesc && protoDesc.set) {
      protoDesc.set.call(el, value);
    } else if (ownDesc && ownDesc.set) {
      ownDesc.set.call(el, value);
    } else {
      el.value = value;
    }
    el.dispatchEvent(new Event("input", { bubbles: true }));
    el.dispatchEvent(new Event("change", { bubbles: true }));
  }

  function fieldBlocks() {
    var root =
      document.querySelector("[class*='ControlPane']") ||
      document.querySelector("[class*='EditorContainer']") ||
      document.querySelector("main") ||
      document.body;
    if (!root) return [];
    var labels = Array.prototype.slice.call(root.querySelectorAll("label"));
    return labels
      .map(function (label) {
        var name = (label.textContent || "").replace(/\s+/g, " ").trim();
        if (!name || name.length > 80) return null;
        // Skip ID (auto-assigned) and noisy nested relationship/source labels.
        if (/^ID$/i.test(name)) return null;
        var container = label.closest("[class*='Control']") || label.parentElement;
        if (!container) return null;
        var input =
          container.querySelector("input:not([type=hidden]):not([type=checkbox]):not([type=radio])") ||
          container.querySelector("textarea") ||
          container.querySelector("select") ||
          container.querySelector("[contenteditable='true']");
        if (!input) return null;
        return { name: name, input: input, container: container };
      })
      .filter(Boolean);
  }

  function readDraftFields() {
    var data = {};
    fieldBlocks().forEach(function (block) {
      var el = block.input;
      var val;
      if (el.getAttribute && el.getAttribute("contenteditable") === "true") {
        val = el.innerText || el.textContent || "";
      } else {
        val = el.value;
      }
      if (val != null && String(val).length) {
        data[block.name] = String(val);
      }
    });
    return data;
  }

  function writeDraftFields(data) {
    if (!data) return 0;
    var written = 0;
    fieldBlocks().forEach(function (block) {
      if (!Object.prototype.hasOwnProperty.call(data, block.name)) return;
      var val = data[block.name];
      var el = block.input;
      if (el.getAttribute && el.getAttribute("contenteditable") === "true") {
        el.focus();
        el.innerText = val;
        el.dispatchEvent(new Event("input", { bubbles: true }));
      } else {
        setNativeValue(el, val);
      }
      written += 1;
    });
    return written;
  }

  function saveLocalDraft() {
    if (!isEditorHash(location.hash)) return;
    var fields = readDraftFields();
    if (!Object.keys(fields).length) return;
    var payload = {
      hash: location.hash,
      collection: collectionFromHash(location.hash),
      updatedAt: new Date().toISOString(),
      fields: fields,
    };
    try {
      localStorage.setItem(draftStorageKey(location.hash), JSON.stringify(payload));
      localStorage.setItem(LAST_KEY, JSON.stringify(payload));
      updateToolbar(payload);
    } catch (err) {
      console.warn("OIR CMS draft save failed", err);
    }
  }

  function loadDraftForHash(hash) {
    try {
      var raw = localStorage.getItem(draftStorageKey(hash));
      return raw ? JSON.parse(raw) : null;
    } catch (err) {
      return null;
    }
  }

  function loadLastDraft() {
    try {
      var raw = localStorage.getItem(LAST_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (err) {
      return null;
    }
  }

  function deleteLocalDraft(hash) {
    hash = hash || location.hash;
    try {
      localStorage.removeItem(draftStorageKey(hash));
      var last = loadLastDraft();
      if (last && last.hash === hash) {
        localStorage.removeItem(LAST_KEY);
      }
    } catch (err) {
      /* ignore */
    }
    updateToolbar(null);
  }

  function clearVisibleFields() {
    fieldBlocks().forEach(function (block) {
      var el = block.input;
      if (el.getAttribute && el.getAttribute("contenteditable") === "true") {
        el.innerText = "";
        el.dispatchEvent(new Event("input", { bubbles: true }));
      } else if (el.tagName === "SELECT") {
        /* leave defaults */
      } else {
        setNativeValue(el, "");
      }
    });
  }

  function attemptRestore(tries) {
    tries = tries || 0;
    if (!isEditorHash(location.hash)) return;
    var draft = loadDraftForHash(location.hash);
    if (!draft || !draft.fields) return;
    var written = writeDraftFields(draft.fields);
    if (written === 0 && tries < RESTORE_MAX_TRIES) {
      setTimeout(function () {
        attemptRestore(tries + 1);
      }, RESTORE_RETRY_MS);
      return;
    }
    updateToolbar(draft);
    if (written > 0) {
      showToast("Restored your local draft (" + Object.keys(draft.fields).length + " fields).");
    }
  }

  /* ---------- Toolbar UI ---------- */

  function ensureToolbar() {
    var bar = document.getElementById("oir-cms-draft-bar");
    if (bar) return bar;
    bar = document.createElement("div");
    bar.id = "oir-cms-draft-bar";
    bar.innerHTML =
      '<div class="oir-cms-draft-bar__text" id="oir-cms-draft-status">Local drafts save automatically on this device.</div>' +
      '<div class="oir-cms-draft-bar__actions">' +
      '<button type="button" id="oir-cms-draft-resume" class="oir-cms-btn oir-cms-btn--secondary" hidden>Resume draft</button>' +
      '<button type="button" id="oir-cms-draft-delete" class="oir-cms-btn oir-cms-btn--danger">Delete draft</button>' +
      "</div>";
    document.body.appendChild(bar);

    document.getElementById("oir-cms-draft-delete").addEventListener("click", function () {
      if (!confirm("Delete the local draft on this device and clear the form fields you have entered?")) {
        return;
      }
      deleteLocalDraft(location.hash);
      clearVisibleFields();
      showToast("Local draft deleted. Form cleared.");
    });

    document.getElementById("oir-cms-draft-resume").addEventListener("click", function () {
      var last = loadLastDraft();
      if (last && last.hash) {
        location.hash = last.hash;
      }
    });

    return bar;
  }

  function updateToolbar(payload) {
    ensureToolbar();
    var status = document.getElementById("oir-cms-draft-status");
    var del = document.getElementById("oir-cms-draft-delete");
    var resume = document.getElementById("oir-cms-draft-resume");
    var last = payload || loadLastDraft();
    var onEditor = isEditorHash(location.hash);
    var hasDraftForPage = !!loadDraftForHash(location.hash);

    if (onEditor) {
      resume.hidden = true;
      del.hidden = false;
      if (last && last.updatedAt && hasDraftForPage) {
        status.textContent = "Local draft saved " + formatTime(last.updatedAt) + ". Leave anytime — return here to continue.";
      } else {
        status.textContent = "Start typing — a local draft will save on this device automatically.";
      }
    } else {
      del.hidden = true;
      if (last && last.hash && last.fields && Object.keys(last.fields).length) {
        resume.hidden = false;
        status.textContent =
          "Unfinished " + (last.collection || "intake") + " draft from " + formatTime(last.updatedAt) + ".";
      } else {
        resume.hidden = true;
        status.textContent = "Tip: log into GitHub before opening the editor. IDs are assigned automatically on save.";
      }
    }
  }

  function formatTime(iso) {
    try {
      return new Date(iso).toLocaleString();
    } catch (err) {
      return iso;
    }
  }

  function showToast(message) {
    var el = document.getElementById("oir-cms-toast");
    if (!el) {
      el = document.createElement("div");
      el.id = "oir-cms-toast";
      document.body.appendChild(el);
    }
    el.textContent = message;
    el.classList.add("oir-cms-toast--show");
    clearTimeout(showToast._t);
    showToast._t = setTimeout(function () {
      el.classList.remove("oir-cms-toast--show");
    }, 3500);
  }

  function ensureLoginBanner() {
    if (document.getElementById("oir-cms-login-help")) return;
    var help = document.createElement("div");
    help.id = "oir-cms-login-help";
    help.innerHTML =
      "<strong>Before you sign in:</strong> open GitHub in this browser and log in first " +
      '(<a href="https://github.com/login" target="_blank" rel="noopener">github.com/login</a>), ' +
      "then return here and choose <em>Login with GitHub</em>. " +
      "The Outreach CRM on the public site does not require login — only this editor does. " +
      "You do not need to invent an ID; one is created when your suggestion is saved/processed. " +
      'Need the guide? <a href="/about/suggest/">How to suggest content</a>.';
    document.body.insertBefore(help, document.body.firstChild);
  }

  /* ---------- Wire Decap + page lifecycle ---------- */

  function onHashChange() {
    updateToolbar();
    if (isEditorHash(location.hash)) {
      setTimeout(function () {
        attemptRestore(0);
      }, 600);
    }
  }

  function bootUi() {
    ensureLoginBanner();
    ensureToolbar();
    updateToolbar();
    onHashChange();
  }

  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState === "hidden") {
      saveLocalDraft();
    } else if (isEditorHash(location.hash)) {
      attemptRestore(0);
    }
  });

  window.addEventListener("pagehide", saveLocalDraft);
  window.addEventListener("hashchange", onHashChange);

  document.addEventListener(
    "input",
    function () {
      if (!isEditorHash(location.hash)) return;
      clearTimeout(bootUi._saveTimer);
      bootUi._saveTimer = setTimeout(saveLocalDraft, SAVE_INTERVAL_MS);
    },
    true
  );

  document.addEventListener(
    "change",
    function () {
      if (!isEditorHash(location.hash)) return;
      saveLocalDraft();
    },
    true
  );

  setInterval(function () {
    if (isEditorHash(location.hash)) saveLocalDraft();
  }, 5000);

  function registerCmsHooks() {
    if (!window.CMS || typeof window.CMS.registerEventListener !== "function") {
      return false;
    }

    window.CMS.registerEventListener({
      name: "preSave",
      handler: function (event) {
        var entry = event.entry;
        var collection = entry.get("collection");
        var data = entry.get("data");
        var js = typeof data.toJS === "function" ? data.toJS() : {};
        var next = ensureId(collection, js);

        if (!Array.isArray(next.relationships)) next.relationships = [];
        if (!Array.isArray(next.sources)) next.sources = [];
        if (!Array.isArray(next.tags)) next.tags = [];
        if (!next.status) next.status = "draft";
        if (next.last_verified == null) next.last_verified = "";

        var out = data;
        Object.keys(next).forEach(function (key) {
          out = out.set(key, next[key]);
        });
        return out;
      },
    });

    window.CMS.registerEventListener({
      name: "postSave",
      handler: function () {
        deleteLocalDraft(location.hash);
        showToast("Saved to GitHub workflow. Local draft cleared.");
      },
    });

    return true;
  }

  var hookTries = 0;
  (function waitCms() {
    if (registerCmsHooks() || hookTries > 40) {
      bootUi();
      return;
    }
    hookTries += 1;
    setTimeout(waitCms, 250);
  })();

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootUi);
  } else {
    bootUi();
  }
})();
