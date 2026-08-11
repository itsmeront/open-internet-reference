(() => {
  const SVG_NS = "http://www.w3.org/2000/svg";
  const NODE_WIDTH = 280;
  const NODE_HEIGHT = 72;
  const ROW_GAP = 28;
  const FOCUS_X = 80;
  const NEIGHBOR_X = 520;
  const TOP_Y = 88;

  function svgElement(name, attributes = {}) {
    const element = document.createElementNS(SVG_NS, name);
    Object.entries(attributes).forEach(([key, value]) => {
      element.setAttribute(key, String(value));
    });
    return element;
  }

  function truncate(text, maxLength) {
    return text.length > maxLength ? `${text.slice(0, maxLength - 1)}…` : text;
  }

  function isSourceId(id) {
    return String(id).startsWith("SRC-");
  }

  function isCitationEdge(edge) {
    return edge.predicate === "cites";
  }

  function readFocusFromUrl() {
    try {
      return new URLSearchParams(window.location.search).get("focus");
    } catch (_error) {
      return null;
    }
  }

  function writeFocusToUrl(focusId) {
    try {
      const url = new URL(window.location.href);
      if (focusId) {
        url.searchParams.set("focus", focusId);
      } else {
        url.searchParams.delete("focus");
      }
      window.history.replaceState({}, "", `${url.pathname}${url.search}${url.hash}`);
    } catch (_error) {
      // Ignore history failures in restricted contexts.
    }
  }

  function buildIndexes(data) {
    const nodesById = new Map(data.nodes.map((node) => [node.id, node]));
    const adjacency = new Map();

    data.nodes.forEach((node) => {
      adjacency.set(node.id, []);
    });

    data.edges.forEach((edge) => {
      if (!nodesById.has(edge.subject) || !nodesById.has(edge.object)) {
        return;
      }
      adjacency.get(edge.subject).push(edge);
      adjacency.get(edge.object).push({
        subject: edge.object,
        predicate: edge.predicate,
        object: edge.subject,
        reverseOf: edge,
      });
    });

    return { nodesById, adjacency };
  }

  function neighborDegree(nodeId, adjacency, includeCitations) {
    return (adjacency.get(nodeId) || []).filter((edge) => (
      includeCitations || !isCitationEdge(edge.reverseOf || edge)
    )).length;
  }

  function starterSuggestions(nodesById, adjacency, limit = 8) {
    return [...nodesById.values()]
      .filter((node) => !isSourceId(node.id))
      .map((node) => ({
        node,
        degree: neighborDegree(node.id, adjacency, false),
      }))
      .filter((entry) => entry.degree > 0)
      .sort((a, b) => b.degree - a.degree || a.node.id.localeCompare(b.node.id))
      .slice(0, limit)
      .map((entry) => entry.node);
  }

  function egoSubgraph(focusId, nodesById, adjacency, includeCitations) {
    const focus = nodesById.get(focusId);
    if (!focus) {
      return { nodes: [], edges: [], focus: null };
    }

    const neighborIds = new Set();
    const edges = [];
    const seenEdgeKeys = new Set();

    (adjacency.get(focusId) || []).forEach((edge) => {
      const canonical = edge.reverseOf || edge;
      if (!includeCitations && isCitationEdge(canonical)) {
        return;
      }

      const neighborId = edge.object;
      if (neighborId === focusId || !nodesById.has(neighborId)) {
        return;
      }
      if (!includeCitations && isSourceId(neighborId) && isCitationEdge(canonical)) {
        return;
      }

      neighborIds.add(neighborId);
      const key = `${canonical.subject}|${canonical.predicate}|${canonical.object}`;
      if (!seenEdgeKeys.has(key)) {
        seenEdgeKeys.add(key);
        edges.push(canonical);
      }
    });

    const nodes = [focus, ...[...neighborIds].sort().map((id) => nodesById.get(id))];
    return { nodes, edges, focus };
  }

  function layoutEgo(focus, neighbors) {
    const positions = new Map();
    positions.set(focus.id, {
      x: FOCUS_X,
      y: TOP_Y + Math.max(0, neighbors.length - 1) * (NODE_HEIGHT + ROW_GAP) / 2,
    });

    neighbors.forEach((node, index) => {
      positions.set(node.id, {
        x: NEIGHBOR_X,
        y: TOP_Y + index * (NODE_HEIGHT + ROW_GAP),
      });
    });

    const height = TOP_Y
      + Math.max(1, neighbors.length) * (NODE_HEIGHT + ROW_GAP)
      + 80;

    return {
      positions,
      width: NEIGHBOR_X + NODE_WIDTH + 120,
      height,
    };
  }

  function edgePath(from, to) {
    const startX = from.x + NODE_WIDTH;
    const startY = from.y + NODE_HEIGHT / 2;
    const endX = to.x;
    const endY = to.y + NODE_HEIGHT / 2;
    const curve = Math.max(120, (endX - startX) / 2);
    return `M ${startX} ${startY} C ${startX + curve} ${startY}, ${endX - curve} ${endY}, ${endX} ${endY}`;
  }

  function addNode(group, node, position, { focused = false, onFocus } = {}) {
    const nodeGroup = svgElement("g", {
      class: [
        "oir-graph-node",
        isSourceId(node.id) ? "oir-graph-node--source" : "oir-graph-node--knowledge",
        focused ? "oir-graph-node--focus" : "",
      ].filter(Boolean).join(" "),
      transform: `translate(${position.x}, ${position.y})`,
      tabindex: "0",
      role: "button",
      "aria-label": focused
        ? `Focused record ${node.id}`
        : `Focus graph on ${node.id}`,
    });

    nodeGroup.appendChild(svgElement("rect", {
      width: NODE_WIDTH,
      height: NODE_HEIGHT,
      rx: 12,
      ry: 12,
    }));

    const text = svgElement("text", { x: 16, y: 24 });
    const id = svgElement("tspan", { class: "oir-graph-node__id", x: 16, dy: 0 });
    id.textContent = node.id;
    const title = svgElement("tspan", { class: "oir-graph-node__title", x: 16, dy: 20 });
    title.textContent = truncate(node.title, 42);
    text.appendChild(id);
    text.appendChild(title);
    nodeGroup.appendChild(text);

    nodeGroup.addEventListener("click", (event) => {
      event.preventDefault();
      event.stopPropagation();
      if (!focused && onFocus) {
        onFocus(node.id);
      }
    });

    nodeGroup.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        if (!focused && onFocus) {
          onFocus(node.id);
        }
      }
    });

    group.appendChild(nodeGroup);
  }

  function addLaneTitles(group, hasNeighbors) {
    const focusTitle = svgElement("text", {
      class: "oir-graph-lane-title",
      x: FOCUS_X,
      y: 42,
    });
    focusTitle.textContent = "Focus";
    group.appendChild(focusTitle);

    if (hasNeighbors) {
      const neighborTitle = svgElement("text", {
        class: "oir-graph-lane-title",
        x: NEIGHBOR_X,
        y: 42,
      });
      neighborTitle.textContent = "1-hop neighbors";
      group.appendChild(neighborTitle);
    }
  }

  function createEmptyState(viewport, suggestions, onFocus) {
    const empty = document.createElement("div");
    empty.className = "oir-relationship-graph__empty";

    const heading = document.createElement("p");
    heading.className = "oir-relationship-graph__empty-title";
    heading.textContent = "Choose a record to explore its relationships";
    empty.appendChild(heading);

    const body = document.createElement("p");
    body.className = "oir-relationship-graph__empty-body";
    body.textContent = "Search above, or start with a highly connected topic. Citation edges to source records are hidden by default.";
    empty.appendChild(body);

    if (suggestions.length) {
      const list = document.createElement("div");
      list.className = "oir-relationship-graph__suggestions";
      suggestions.forEach((node) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "oir-relationship-graph__suggestion";
        button.textContent = node.id;
        button.title = node.title;
        button.addEventListener("click", () => onFocus(node.id));
        list.appendChild(button);
      });
      empty.appendChild(list);
    }

    viewport.replaceChildren(empty);
  }

  function createViewportController(viewport) {
    let scale = 1;
    let dragStart = null;
    let svg = null;
    let graphGroup = null;
    let width = 0;
    let height = 0;

    function applyScale() {
      if (!svg || !graphGroup) {
        return;
      }
      graphGroup.removeAttribute("transform");
      const scaledWidth = width * scale;
      const scaledHeight = height * scale;
      svg.style.width = `${scaledWidth}px`;
      svg.style.height = `${scaledHeight}px`;
      svg.style.minWidth = `${scaledWidth}px`;
      svg.style.minHeight = `${scaledHeight}px`;
    }

    function centerViewport() {
      if (!svg) {
        return;
      }
      const scrollLeft = Math.max(0, (svg.offsetWidth - viewport.clientWidth) / 2);
      const scrollTop = Math.max(0, (svg.offsetHeight - viewport.clientHeight) / 2);
      viewport.scrollTo({ left: scrollLeft, top: scrollTop });
    }

    function zoom(factor) {
      if (!svg) {
        return;
      }
      const previousScale = scale;
      const centerX = viewport.scrollLeft + viewport.clientWidth / 2;
      const centerY = viewport.scrollTop + viewport.clientHeight / 2;
      scale = Math.min(2.5, Math.max(0.35, scale * factor));
      applyScale();
      viewport.scrollLeft = (centerX / previousScale) * scale - viewport.clientWidth / 2;
      viewport.scrollTop = (centerY / previousScale) * scale - viewport.clientHeight / 2;
    }

    function reset() {
      if (!svg) {
        return;
      }
      scale = 1;
      applyScale();
      viewport.scrollTo({ left: 0, top: 0 });
    }

    function fit() {
      if (!svg) {
        return;
      }
      const box = viewport.getBoundingClientRect();
      scale = Math.min(1.2, Math.max(0.35, Math.min(box.width / width, box.height / height) * 0.95));
      applyScale();
      centerViewport();
    }

    function attach(nextSvg, nextGroup, nextWidth, nextHeight) {
      svg = nextSvg;
      graphGroup = nextGroup;
      width = nextWidth;
      height = nextHeight;
      scale = 1;
      dragStart = null;

      svg.addEventListener("wheel", (event) => {
        event.preventDefault();
        zoom(event.deltaY < 0 ? 1.08 : 0.92);
      }, { passive: false });

      svg.addEventListener("pointerdown", (event) => {
        if (event.target.closest(".oir-graph-node")) {
          return;
        }
        event.preventDefault();
        dragStart = {
          x: event.clientX,
          y: event.clientY,
          scrollLeft: viewport.scrollLeft,
          scrollTop: viewport.scrollTop,
        };
        svg.classList.add("is-panning");
        svg.setPointerCapture(event.pointerId);
      });

      svg.addEventListener("pointermove", (event) => {
        if (!dragStart) {
          return;
        }
        event.preventDefault();
        viewport.scrollLeft = dragStart.scrollLeft - (event.clientX - dragStart.x);
        viewport.scrollTop = dragStart.scrollTop - (event.clientY - dragStart.y);
      });

      const endPan = () => {
        dragStart = null;
        svg?.classList.remove("is-panning");
      };

      svg.addEventListener("pointerup", endPan);
      svg.addEventListener("pointercancel", endPan);
      fit();
    }

    function clear() {
      svg = null;
      graphGroup = null;
      width = 0;
      height = 0;
      scale = 1;
      dragStart = null;
    }

    return { attach, clear, zoom, reset, fit };
  }

  function renderFocusedGraph(viewport, subgraph, onFocus, viewportController) {
    const neighbors = subgraph.nodes.filter((node) => node.id !== subgraph.focus.id);
    const { positions, width, height } = layoutEgo(subgraph.focus, neighbors);

    const svg = svgElement("svg", {
      role: "img",
      "aria-label": `Relationships for ${subgraph.focus.id}`,
      preserveAspectRatio: "xMinYMin meet",
    });
    const defs = svgElement("defs");
    const marker = svgElement("marker", {
      id: "oir-graph-arrow",
      markerWidth: 10,
      markerHeight: 10,
      refX: 8,
      refY: 3,
      orient: "auto",
      markerUnits: "strokeWidth",
    });
    marker.appendChild(svgElement("path", { d: "M0,0 L0,6 L9,3 z", fill: "rgba(71, 85, 105, 0.55)" }));
    defs.appendChild(marker);
    svg.appendChild(defs);

    const graphGroup = svgElement("g");
    svg.appendChild(graphGroup);
    viewport.replaceChildren(svg);

    svg.style.width = `${width}px`;
    svg.style.height = `${height}px`;
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    addLaneTitles(graphGroup, neighbors.length > 0);

    subgraph.edges.forEach((edge) => {
      const fromId = edge.subject === subgraph.focus.id ? edge.subject : edge.object;
      const toId = edge.subject === subgraph.focus.id ? edge.object : edge.subject;
      const from = positions.get(fromId);
      const to = positions.get(toId);
      if (!from || !to) {
        return;
      }

      const path = svgElement("path", {
        class: "oir-graph-edge",
        d: edgePath(from, to),
        markerEnd: "url(#oir-graph-arrow)",
      });
      graphGroup.appendChild(path);

      const label = svgElement("text", {
        class: "oir-graph-edge-label",
        x: (from.x + NODE_WIDTH + to.x) / 2 - 26,
        y: (from.y + to.y) / 2 + NODE_HEIGHT / 2 - 8,
      });
      label.textContent = edge.predicate;
      graphGroup.appendChild(label);
    });

    addNode(graphGroup, subgraph.focus, positions.get(subgraph.focus.id), {
      focused: true,
      onFocus,
    });

    neighbors.forEach((node) => {
      addNode(graphGroup, node, positions.get(node.id), { onFocus });
    });

    viewportController.attach(svg, graphGroup, width, height);
  }

  function setupGraph(container, data) {
    const viewport = container.querySelector(".oir-relationship-graph__viewport");
    const searchInput = container.querySelector("[data-graph-search]");
    const suggestionsList = container.querySelector("[data-graph-search-results]");
    const showSources = container.querySelector("[data-graph-show-sources]");
    const clearButton = container.querySelector("[data-graph-clear]");
    const openButton = container.querySelector("[data-graph-open]");
    const status = container.querySelector("[data-graph-status]");
    const { nodesById, adjacency } = buildIndexes(data);
    const starters = starterSuggestions(nodesById, adjacency);
    const viewportController = createViewportController(viewport);

    let focusId = null;

    function searchableNodes(query) {
      const normalized = query.trim().toLowerCase();
      const includeSources = Boolean(showSources?.checked);
      return [...nodesById.values()]
        .filter((node) => includeSources || !isSourceId(node.id))
        .filter((node) => {
          if (!normalized) {
            return false;
          }
          return node.id.toLowerCase().includes(normalized)
            || node.title.toLowerCase().includes(normalized)
            || String(node.type || "").toLowerCase().includes(normalized);
        })
        .sort((a, b) => {
          const aExact = a.id.toLowerCase() === normalized ? 0 : 1;
          const bExact = b.id.toLowerCase() === normalized ? 0 : 1;
          if (aExact !== bExact) {
            return aExact - bExact;
          }
          return a.id.localeCompare(b.id);
        })
        .slice(0, 12);
    }

    function renderSuggestions(query) {
      if (!suggestionsList) {
        return;
      }
      const matches = searchableNodes(query);
      suggestionsList.replaceChildren();
      if (!matches.length) {
        suggestionsList.hidden = true;
        return;
      }
      matches.forEach((node) => {
        const option = document.createElement("button");
        option.type = "button";
        option.className = "oir-relationship-graph__search-option";
        option.innerHTML = `<strong>${node.id}</strong><span>${truncate(node.title, 64)}</span>`;
        option.addEventListener("click", () => {
          setFocus(node.id);
          suggestionsList.hidden = true;
          if (searchInput) {
            searchInput.value = node.id;
          }
        });
        suggestionsList.appendChild(option);
      });
      suggestionsList.hidden = false;
    }

    function updateChrome(subgraph) {
      if (status) {
        if (!subgraph.focus) {
          status.textContent = "No focus selected. Search for a record or pick a starter below.";
        } else {
          const neighborCount = subgraph.nodes.length - 1;
          const sourceNote = showSources?.checked
            ? "including citation edges"
            : "citation edges hidden";
          status.textContent = `Focus: ${subgraph.focus.id} · ${neighborCount} neighbor${neighborCount === 1 ? "" : "s"} · ${subgraph.edges.length} edge${subgraph.edges.length === 1 ? "" : "s"} (${sourceNote}). Click a neighbor to refocus.`;
        }
      }

      if (openButton) {
        if (subgraph.focus?.href && subgraph.focus.href !== "#") {
          openButton.hidden = false;
          openButton.href = subgraph.focus.href;
        } else {
          openButton.hidden = true;
          openButton.removeAttribute("href");
        }
      }

      if (clearButton) {
        clearButton.disabled = !subgraph.focus;
      }
    }

    function paint() {
      const includeCitations = Boolean(showSources?.checked);
      if (!focusId || !nodesById.has(focusId)) {
        focusId = null;
        writeFocusToUrl(null);
        viewportController.clear();
        createEmptyState(viewport, starters, setFocus);
        updateChrome({ focus: null, nodes: [], edges: [] });
        return;
      }

      const subgraph = egoSubgraph(focusId, nodesById, adjacency, includeCitations);
      writeFocusToUrl(focusId);
      renderFocusedGraph(viewport, subgraph, setFocus, viewportController);
      updateChrome(subgraph);
    }

    function setFocus(nextFocusId) {
      focusId = nextFocusId;
      if (searchInput && nextFocusId) {
        searchInput.value = nextFocusId;
      }
      if (suggestionsList) {
        suggestionsList.hidden = true;
      }
      paint();
    }

    searchInput?.addEventListener("input", () => {
      renderSuggestions(searchInput.value);
    });

    searchInput?.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        const matches = searchableNodes(searchInput.value);
        if (matches[0]) {
          setFocus(matches[0].id);
          if (suggestionsList) {
            suggestionsList.hidden = true;
          }
        }
      }
      if (event.key === "Escape" && suggestionsList) {
        suggestionsList.hidden = true;
      }
    });

    document.addEventListener("click", (event) => {
      if (!suggestionsList || suggestionsList.hidden) {
        return;
      }
      if (!container.contains(event.target)) {
        suggestionsList.hidden = true;
      }
    });

    showSources?.addEventListener("change", paint);
    clearButton?.addEventListener("click", () => {
      if (searchInput) {
        searchInput.value = "";
      }
      setFocus(null);
    });

    container.querySelector("[data-graph-zoom-in]")?.addEventListener("click", () => {
      viewportController.zoom(1.18);
    });
    container.querySelector("[data-graph-zoom-out]")?.addEventListener("click", () => {
      viewportController.zoom(0.82);
    });
    container.querySelector("[data-graph-reset]")?.addEventListener("click", () => {
      viewportController.reset();
    });
    container.querySelector("[data-graph-fit]")?.addEventListener("click", () => {
      viewportController.fit();
    });

    const initialFocus = readFocusFromUrl();
    if (initialFocus && nodesById.has(initialFocus)) {
      setFocus(initialFocus);
    } else {
      paint();
    }
  }

  function initRelationshipGraphs() {
    document.querySelectorAll(".oir-relationship-graph").forEach((container) => {
      const dataScript = container.querySelector('script[type="application/json"]');
      if (!dataScript || container.dataset.rendered === "true") {
        return;
      }
      container.dataset.rendered = "true";
      setupGraph(container, JSON.parse(dataScript.textContent));
    });
  }

  if (window.document$) {
    window.document$.subscribe(initRelationshipGraphs);
  } else {
    document.addEventListener("DOMContentLoaded", initRelationshipGraphs);
  }
})();
