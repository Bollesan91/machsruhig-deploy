"""
Generate city-spezifische og-images.
Base: existing /assets/og-image.png (1200x630).
Overlay: City-Name als Text + Subtitle.
Output: /assets/og-cities/{slug}.png
"""
import os
import re
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

_HERE = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT = _HERE.parent.parent
BESTATTER = ROOT / "bestatter"
OUT_DIR = ROOT / "assets" / "og-cities"
OUT_DIR.mkdir(parents=True, exist_ok=True)

BASE_IMG = ROOT / "assets" / "og-image.png"

CITY_DISPLAY = {
    "muelheim": "Mülheim an der Ruhr",
    "moenchengladbach": "Mönchengladbach",
    "luebeck": "Lübeck",
    "duesseldorf": "Düsseldorf",
    "nuernberg": "Nürnberg",
    "muenchen": "München",
    "muenster": "Münster",
    "saarbruecken": "Saarbrücken",
    "koeln": "Köln",
    "osnabrueck": "Osnabrück",
}


def get_display(slug):
    if slug in CITY_DISPLAY:
        return CITY_DISPLAY[slug]
    return slug.capitalize()


# Try to load font from common Windows locations
FONT_PATHS = [
    "C:/Windows/Fonts/seguibl.ttf",  # Segoe UI Black
    "C:/Windows/Fonts/segoeuib.ttf",  # Segoe UI Bold
    "C:/Windows/Fonts/calibrib.ttf",  # Calibri Bold
    "C:/Windows/Fonts/arial.ttf",
]


def load_font(size):
    for fp in FONT_PATHS:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()


def generate_city_og(slug, display):
    img = Image.open(BASE_IMG).convert("RGBA")
    width, height = img.size

    # Add semi-transparent overlay for text contrast
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    # Gradient overlay at bottom (for text legibility)
    for y in range(int(height * 0.55), height):
        alpha = int(160 * ((y - height * 0.55) / (height * 0.45)))
        overlay_draw.rectangle([(0, y), (width, y + 1)], fill=(45, 35, 25, alpha))

    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # City name (big)
    city_font = load_font(80)
    subtitle_font = load_font(34)
    brand_font = load_font(28)

    title = f"Bestattung in {display}"
    subtitle = "Friedhöfe · Kosten · Bestatter-Wahl"
    brand = "mach's ruhig"

    # Position title bottom-left with padding
    pad = 60
    # Measure text
    try:
        title_bbox = draw.textbbox((0, 0), title, font=city_font)
        title_w = title_bbox[2] - title_bbox[0]
        title_h = title_bbox[3] - title_bbox[1]
    except Exception:
        title_w, title_h = len(title) * 35, 80

    # If title too wide, reduce font
    while title_w > width - 2 * pad and city_font.size > 50:
        city_font = load_font(city_font.size - 4)
        try:
            title_bbox = draw.textbbox((0, 0), title, font=city_font)
            title_w = title_bbox[2] - title_bbox[0]
            title_h = title_bbox[3] - title_bbox[1]
        except Exception:
            title_w = len(title) * (city_font.size // 2)

    # Draw text
    y_title = height - pad - title_h - 80
    draw.text((pad, y_title), title, font=city_font, fill=(255, 253, 249, 255))

    # Subtitle below title
    draw.text((pad, y_title + title_h + 12), subtitle, font=subtitle_font, fill=(232, 224, 214, 235))

    # Brand top-right
    try:
        brand_bbox = draw.textbbox((0, 0), brand, font=brand_font)
        brand_w = brand_bbox[2] - brand_bbox[0]
    except Exception:
        brand_w = len(brand) * 14
    draw.text((width - pad - brand_w, pad), brand, font=brand_font, fill=(255, 253, 249, 220))

    # Save
    out_path = OUT_DIR / f"{slug}.png"
    img.convert("RGB").save(out_path, "PNG", optimize=True)
    return out_path


# Generate per city
generated = []
for c in sorted(BESTATTER.iterdir()):
    if not c.is_dir():
        continue
    if c.name in {"lübeck", "mönchengladbach"}:
        continue
    display = get_display(c.name)
    path = generate_city_og(c.name, display)
    size_kb = round(path.stat().st_size / 1024.0, 1)
    generated.append((c.name, size_kb))

print(f"Generated {len(generated)} og-images:")
for slug, kb in generated[:5]:
    print(f"  {slug}: {kb} KB")
print(f"  ... +{len(generated)-5} more")
print(f"\nOutput dir: {OUT_DIR}")
