from pathlib import Path
from PIL import Image

WALLPAPER_DIR = Path(".")
THUMBNAIL_DIR = Path(".thumbnails")
README_FILE = Path("README.md")
MAX_THUMB_SIZE = (400, 400)  # Maximum thumbnail dimensions (pixels)


def ensure_thumbnail(img_path: Path) -> Path:
    """Generate and compress a thumbnail for the image, or return existing thumbnail path."""
    THUMBNAIL_DIR.mkdir(exist_ok=True)
    thumb_path = THUMBNAIL_DIR / img_path.name

    # Skip regeneration if thumbnail exists and original image hasn't been modified since
    if thumb_path.exists() and thumb_path.stat().st_mtime >= img_path.stat().st_mtime:
        return thumb_path

    try:
        with Image.open(img_path) as img:
            # Convert RGBA/P modes to RGB to allow JPEG compression if needed
            if img.mode in ("RGBA", "P") and img_path.suffix.lower() in [
                ".jpg",
                ".jpeg",
            ]:
                img = img.convert("RGB")

            # Resize image while preserving aspect ratio
            img.thumbnail(MAX_THUMB_SIZE)

            # Save image with quality optimization
            if img_path.suffix.lower() in [".jpg", ".jpeg"]:
                img.save(thumb_path, optimize=True, quality=75)
            else:
                img.save(thumb_path, optimize=True)

    except Exception as e:
        print(f"Failed to compress image {img_path.name}: {e}")
        return img_path  # Fallback to original image on error

    return thumb_path


def generate_markdown(image_pairs):
    """Generate HTML responsive Flexbox structure with 4 thumbnail previews per row linking to original images."""
    rows = []
    row = []

    for i, (orig_path, thumb_path) in enumerate(image_pairs, start=1):
        # Convert path objects to POSIX string format for cross-platform link compatibility
        orig_rel_path = orig_path.as_posix()
        thumb_rel_path = thumb_path.as_posix()

        # Wrap image with anchor tag pointing to original full-size wallpaper
        row.append(
            f"<a href='{orig_rel_path}'><img src='{thumb_rel_path}' alt='Wallpaper' width='200px' style='margin: 5px;'></a>"
        )

        # Break into a new row every 4 images
        if i % 4 == 0:
            rows.append(
                "<div style='display: flex; justify-content: center; align-items: center; gap: 10px;'>\n"
                + "\n".join(row)
                + "\n</div>"
            )
            row = []

    if row:
        rows.append(
            "<div style='display: flex; justify-content: center; align-items: center; gap: 10px;'>\n"
            + "\n".join(row)
            + "\n</div>"
        )

    return "\n".join(rows)


def main():
    # Supported image extensions
    valid_extensions = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

    # Retrieve all valid wallpaper images (excluding files in .thumbnails)
    raw_images = [
        f
        for f in sorted(WALLPAPER_DIR.iterdir())
        if f.is_file() and f.suffix.lower() in valid_extensions
    ]

    if not raw_images:
        print("No wallpaper images found.")
        return

    print(f"Found {len(raw_images)} image(s). Processing thumbnails...")

    # Generate or get cached thumbnail for each image, maintaining a tuple pair (original, thumbnail)
    image_pairs = [(img, ensure_thumbnail(img)) for img in raw_images]

    markdown = generate_markdown(image_pairs)

    readme_content = (
        "# Wallpaper Previews\n\n"
        "Here is a preview of all wallpapers in this repository:\n\n" + markdown
    )

    README_FILE.write_text(readme_content, encoding="utf-8")
    print(f"Successfully updated {README_FILE}")


if __name__ == "__main__":
    main()
