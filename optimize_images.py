"""Gera as imagens leves usadas pelo site sem alterar os originais."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parent
PHOTOS = ROOT / "assets" / "fotos"
OG_SOURCE = PHOTOS / "20251030_162521(1).jpg"
OG_TARGET = ROOT / "assets" / "og-cover.jpg"
MAX_EDGE = 1920
WEBP_QUALITY = 82


def webp_from(source: Path) -> Path:
    target = source.with_suffix(".webp")
    with Image.open(source) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        image.thumbnail((MAX_EDGE, MAX_EDGE), Image.Resampling.LANCZOS)
        image.save(target, "WEBP", quality=WEBP_QUALITY, method=6)
    return target


def social_cover() -> None:
    with Image.open(OG_SOURCE) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        image = ImageOps.fit(image, (1200, 630), Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        image.save(OG_TARGET, "JPEG", quality=86, optimize=True, progressive=True)


def main() -> None:
    sources = sorted(PHOTOS.glob("*.jpg"))
    if not sources:
        raise SystemExit("Nenhuma foto JPG encontrada em assets/fotos")

    original_bytes = sum(source.stat().st_size for source in sources)
    targets = [webp_from(source) for source in sources]
    social_cover()
    optimized_bytes = sum(target.stat().st_size for target in targets)

    reduction = 100 * (1 - optimized_bytes / original_bytes)
    print(
        f"{len(targets)} fotos: {original_bytes / 1048576:.2f} MB -> "
        f"{optimized_bytes / 1048576:.2f} MB ({reduction:.1f}% menor)"
    )
    print(f"Capa social: {OG_TARGET.relative_to(ROOT)} ({OG_TARGET.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
