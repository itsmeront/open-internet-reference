document.addEventListener("DOMContentLoaded", () => {
  const currentHost = window.location.host;

  document.querySelectorAll("a[href]").forEach((link) => {
    const href = link.getAttribute("href");
    if (!href) {
      return;
    }

    const url = new URL(href, window.location.href);
    if ((url.protocol === "http:" || url.protocol === "https:") && url.host !== currentHost) {
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener noreferrer");
    }
  });
});
