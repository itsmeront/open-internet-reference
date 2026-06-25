(() => {
  const SVG_NS = "http://www.w3.org/2000/svg";
  const NODE_WIDTH = 280;
  const NODE_HEIGHT = 72;
  const ROW_GAP = 36;
  const LEFT_X = 120;
  const RIGHT_X = 700;
  const TOP_Y = 96;

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

  function nodeKind(node) {
    return node.id.startsWith("SRC-") ? "source" : "knowledge";
  }

  function layoutNodes(nodes) {
    const leftNodes = nodes.filter((node) => nodeKind(node) === "knowledge");
    const rightNodes = nodes.filter((node) => nodeKind(node) === "source");
    const positions = new Map();

    leftNodes.forEach((node, index) => {
      positions.set(node.id, {
        x: LEFT_X,
        y: TOP_Y + index * (NODE_HEIGHT + ROW_GAP),
      });
    });

    rightNodes.forEach((node, index) => {
      positions.set(node.id, {
        x: RIGHT_X,
        y: TOP_Y + index * (NODE_HEIGHT + ROW_GAP),
      });
    });

    return {
      positions,
      width: RIGHT_X + NODE_WIDTH + 160,
      height: TOP_Y + Math.max(leftNodes.length, rightNodes.length) * (NODE_HEIGHT + ROW_GAP) + 80,
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

  function addNode(group, node, position) {
    const anchor = svgElement("a", { href: node.href });
    const nodeGroup = svgElement("g", {
      class: `oir-graph-node oir-graph-node--${nodeKind(node)}`,
      transform: `translate(${position.x}, ${position.y})`,
      tabindex: "0",
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
    anchor.appendChild(nodeGroup);
    group.appendChild(anchor);
  }

  function addLaneTitles(group) {
    const knowledge = svgElement("text", {
      class: "oir-graph-lane-title",
      x: LEFT_X,
      y: 42,
    });
    knowledge.textContent = "Knowledge Records";
    const sources = svgElement("text", {
      class: "oir-graph-lane-title",
      x: RIGHT_X,
      y: 42,
    });
    sources.textContent = "Source Records";
    group.appendChild(knowledge);
    group.appendChild(sources);
  }

  function renderGraph(container, data) {
    const viewport = container.querySelector(".oir-relationship-graph__viewport");
    const svg = svgElement("svg", {
      role: "img",
      "aria-label": "Interactive relationship graph",
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

    const { positions, width, height } = layoutNodes(data.nodes);
    svg.style.width = `${width}px`;
    svg.style.height = `${height}px`;
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    addLaneTitles(graphGroup);

    data.edges.forEach((edge) => {
      const from = positions.get(edge.subject);
      const to = positions.get(edge.object);
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

    data.nodes.forEach((node) => {
      const position = positions.get(node.id);
      if (position) {
        addNode(graphGroup, node, position);
      }
    });

    let scale = 1;
    let dragStart = null;

    function applyScale() {
      graphGroup.removeAttribute("transform");
      const scaledWidth = width * scale;
      const scaledHeight = height * scale;
      svg.style.width = `${scaledWidth}px`;
      svg.style.height = `${scaledHeight}px`;
      svg.style.minWidth = `${scaledWidth}px`;
      svg.style.minHeight = `${scaledHeight}px`;
    }

    function centerViewport() {
      const scrollLeft = Math.max(0, (svg.offsetWidth - viewport.clientWidth) / 2);
      const scrollTop = Math.max(0, (svg.offsetHeight - viewport.clientHeight) / 2);
      viewport.scrollTo({ left: scrollLeft, top: scrollTop });
    }

    function zoom(factor) {
      const previousScale = scale;
      const centerX = viewport.scrollLeft + viewport.clientWidth / 2;
      const centerY = viewport.scrollTop + viewport.clientHeight / 2;
      scale = Math.min(2.5, Math.max(0.35, scale * factor));
      applyScale();
      viewport.scrollLeft = (centerX / previousScale) * scale - viewport.clientWidth / 2;
      viewport.scrollTop = (centerY / previousScale) * scale - viewport.clientHeight / 2;
    }

    function reset() {
      scale = 1;
      applyScale();
      viewport.scrollTo({ left: 0, top: 0 });
    }

    function fit() {
      const box = viewport.getBoundingClientRect();
      scale = Math.min(1.2, Math.max(0.35, Math.min(box.width / width, box.height / height) * 0.95));
      applyScale();
      centerViewport();
    }

    container.querySelector("[data-graph-zoom-in]").addEventListener("click", () => zoom(1.18));
    container.querySelector("[data-graph-zoom-out]").addEventListener("click", () => zoom(0.82));
    container.querySelector("[data-graph-reset]").addEventListener("click", reset);
    container.querySelector("[data-graph-fit]").addEventListener("click", fit);

    svg.addEventListener("wheel", (event) => {
      event.preventDefault();
      zoom(event.deltaY < 0 ? 1.08 : 0.92);
    }, { passive: false });

    svg.addEventListener("pointerdown", (event) => {
      if (event.target.closest("a")) {
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

    svg.addEventListener("pointerup", (event) => {
      event.preventDefault();
      dragStart = null;
      svg.classList.remove("is-panning");
    });

    svg.addEventListener("pointercancel", () => {
      dragStart = null;
      svg.classList.remove("is-panning");
    });

    fit();
  }

  function initRelationshipGraphs() {
    document.querySelectorAll(".oir-relationship-graph").forEach((container) => {
      const dataScript = container.querySelector('script[type="application/json"]');
      if (!dataScript || container.dataset.rendered === "true") {
        return;
      }
      container.dataset.rendered = "true";
      renderGraph(container, JSON.parse(dataScript.textContent));
    });
  }

  if (window.document$) {
    window.document$.subscribe(initRelationshipGraphs);
  } else {
    document.addEventListener("DOMContentLoaded", initRelationshipGraphs);
  }
})();
