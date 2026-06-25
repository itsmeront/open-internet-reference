"""Render raster favicon assets from the canonical OIR logo SVG."""

from __future__ import annotations

import io
from pathlib import Path

try:
    import fitz
    from PIL import Image
except ImportError:  # pragma: no cover - exercised only when setup is incomplete.
    print("PyMuPDF and Pillow are required. Install docs dependencies with: python -m pip install -e .[docs]")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
IMAGES_DIR = ROOT / "website" / "assets" / "images"
SOURCE = IMAGES_DIR / "oir-logo-mark.svg"


def _render_svg(size: int) -> Image.Image:
    doc = fitz.open(stream=SOURCE.read_bytes(), filetype="svg")
    try:
        page = doc[0]
        scale = size / max(page.rect.width, page.rect.height)
        matrix = fitz.Matrix(scale, scale)
        pixmap = page.get_pixmap(matrix=matrix, alpha=True)
        image = Image.open(io.BytesIO(pixmap.tobytes("png"))).convert("RGBA")
    finally:
        doc.close()

    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    offset = ((size - image.width) // 2, (size - image.height) // 2)
    canvas.paste(image, offset, image)
    return canvas


def _write_ico(path: Path, sizes: list[int]) -> None:
    images = [_render_svg(size) for size in sizes]
    images[0].save(
        path,
        format="ICO",
        sizes=[(size, size) for size in sizes],
        append_images=images[1:],
    )


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing canonical logo: {SOURCE.as_posix()}")
        return 1

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    _render_svg(32).save(IMAGES_DIR / "favicon.png")
    _render_svg(180).save(IMAGES_DIR / "apple-touch-icon.png")
    _render_svg(512).save(IMAGES_DIR / "logo-mark.png")
    _write_ico(IMAGES_DIR / "favicon.ico", [16, 32, 48])

    print(f"Rendered favicon assets from {SOURCE.name} in {IMAGES_DIR.as_posix()}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
