"""Render raster favicon assets from the canonical OIR logo PNG."""

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
SOURCE = IMAGES_DIR / "oir-logo-mark.png"
LEGACY_SOURCE = IMAGES_DIR / "oir-logo-mark.svg"


def _fit_image(image: Image.Image, size: int) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    scale = size / max(image.width, image.height)
    resized = image.resize(
        (max(1, round(image.width * scale)), max(1, round(image.height * scale))),
        Image.Resampling.LANCZOS,
    )
    offset = ((size - resized.width) // 2, (size - resized.height) // 2)
    canvas.paste(resized, offset, resized)
    return canvas


def _render_png(size: int) -> Image.Image:
    with Image.open(SOURCE) as image:
        return _fit_image(image.convert("RGBA"), size)


def _render_svg(size: int) -> Image.Image:
    doc = fitz.open(stream=LEGACY_SOURCE.read_bytes(), filetype="svg")
    try:
        page = doc[0]
        scale = size / max(page.rect.width, page.rect.height)
        matrix = fitz.Matrix(scale, scale)
        pixmap = page.get_pixmap(matrix=matrix, alpha=True)
        image = Image.open(io.BytesIO(pixmap.tobytes("png"))).convert("RGBA")
    finally:
        doc.close()

    return _fit_image(image, size)


def _render_logo(size: int) -> Image.Image:
    if SOURCE.exists():
        return _render_png(size)
    if LEGACY_SOURCE.exists():
        return _render_svg(size)
    raise FileNotFoundError(f"Missing canonical logo: {SOURCE.as_posix()}")


def _write_ico(path: Path, sizes: list[int]) -> None:
    image = _render_logo(max(sizes))
    icon_sizes = [(size, size) for size in sizes]
    image.save(path, format="ICO", sizes=icon_sizes)


def main() -> int:
    if not SOURCE.exists() and not LEGACY_SOURCE.exists():
        print(f"Missing canonical logo: {SOURCE.as_posix()}")
        return 1

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    _render_logo(32).save(IMAGES_DIR / "favicon.png")
    _render_logo(180).save(IMAGES_DIR / "apple-touch-icon.png")
    _render_logo(512).save(IMAGES_DIR / "logo-mark.png")
    ico_sizes = [16, 32, 48, 64, 128, 256]
    _write_ico(IMAGES_DIR / "favicon.ico", ico_sizes)
    _write_ico(IMAGES_DIR / "oir-logo-mark.ico", ico_sizes)

    source_name = SOURCE.name if SOURCE.exists() else LEGACY_SOURCE.name
    print(f"Rendered favicon assets from {source_name} in {IMAGES_DIR.as_posix()}/")
    print("  favicon.ico and oir-logo-mark.ico include 16, 32, 48, 64, 128, and 256 px sizes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
