"""Render raster favicon assets from the canonical OIR logo PNG."""

from __future__ import annotations

import io
from collections import deque
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
BACKGROUND_TOLERANCE = 40


def _matches_background(color: tuple[int, ...], reference: tuple[int, int, int], tolerance: int) -> bool:
    red, green, blue = color[:3]
    ref_red, ref_green, ref_blue = reference
    return (
        abs(red - ref_red) <= tolerance
        and abs(green - ref_green) <= tolerance
        and abs(blue - ref_blue) <= tolerance
    )


def strip_background(image: Image.Image, *, tolerance: int = BACKGROUND_TOLERANCE) -> Image.Image:
    """Remove the flat light backdrop outside the circular logo."""
    rgba = image.convert("RGBA")
    width, height = rgba.size
    work = rgba.copy()
    pixels = work.load()
    reference = pixels[0, 0][:3]
    queue: deque[tuple[int, int]] = deque()
    seen = bytearray(width * height)

    for x in range(width):
        for y in (0, height - 1):
            if _matches_background(pixels[x, y][:3], reference, tolerance):
                queue.append((x, y))
    for y in range(height):
        for x in (0, width - 1):
            if _matches_background(pixels[x, y][:3], reference, tolerance):
                queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        index = y * width + x
        if seen[index]:
            continue
        seen[index] = 1

        red, green, blue, _alpha = pixels[x, y]
        if not _matches_background((red, green, blue), reference, tolerance):
            continue

        pixels[x, y] = (red, green, blue, 0)
        if x > 0:
            queue.append((x - 1, y))
        if x + 1 < width:
            queue.append((x + 1, y))
        if y > 0:
            queue.append((x, y - 1))
        if y + 1 < height:
            queue.append((x, y + 1))

    return apply_circular_alpha(work)


def apply_circular_alpha(image: Image.Image) -> Image.Image:
    """Clip square canvas padding outside the round logo mark."""
    rgba = image.convert("RGBA")
    width, height = rgba.size
    center_x = width / 2
    center_y = height / 2
    radius = min(width, height) / 2 - 1
    radius_sq = radius * radius
    pixels = rgba.load()

    for y in range(height):
        for x in range(width):
            dx = x - center_x
            dy = y - center_y
            if dx * dx + dy * dy > radius_sq:
                red, green, blue, _alpha = pixels[x, y]
                pixels[x, y] = (red, green, blue, 0)

    return rgba


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


def _load_source_image() -> Image.Image:
    if SOURCE.exists():
        with Image.open(SOURCE) as image:
            return strip_background(image)
    if LEGACY_SOURCE.exists():
        doc = fitz.open(stream=LEGACY_SOURCE.read_bytes(), filetype="svg")
        try:
            page = doc[0]
            scale = 512 / max(page.rect.width, page.rect.height)
            matrix = fitz.Matrix(scale, scale)
            pixmap = page.get_pixmap(matrix=matrix, alpha=True)
            image = Image.open(io.BytesIO(pixmap.tobytes("png"))).convert("RGBA")
        finally:
            doc.close()
        return image
    raise FileNotFoundError(f"Missing canonical logo: {SOURCE.as_posix()}")


def _render_logo(source: Image.Image, size: int) -> Image.Image:
    return _fit_image(source.convert("RGBA"), size)


def _write_ico(path: Path, source: Image.Image, sizes: list[int]) -> None:
    image = _render_logo(source, max(sizes))
    icon_sizes = [(size, size) for size in sizes]
    image.save(path, format="ICO", sizes=icon_sizes)


def main() -> int:
    if not SOURCE.exists() and not LEGACY_SOURCE.exists():
        print(f"Missing canonical logo: {SOURCE.as_posix()}")
        return 1

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    source = _load_source_image()
    source.save(SOURCE)

    _render_logo(source, 32).save(IMAGES_DIR / "favicon.png")
    _render_logo(source, 180).save(IMAGES_DIR / "apple-touch-icon.png")
    _render_logo(source, 512).save(IMAGES_DIR / "logo-mark.png")
    ico_sizes = [16, 32, 48, 64, 128, 256]
    _write_ico(IMAGES_DIR / "favicon.ico", source, ico_sizes)
    _write_ico(IMAGES_DIR / "oir-logo-mark.ico", source, ico_sizes)

    source_name = SOURCE.name if SOURCE.exists() else LEGACY_SOURCE.name
    print(f"Rendered favicon assets from {source_name} in {IMAGES_DIR.as_posix()}/")
    print("  Saved transparent logo PNG and ICO files with 16–256 px sizes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
