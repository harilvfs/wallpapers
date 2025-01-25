import os
from pathlib import Path

WALLPAPER_DIR = "."
README_FILE = "README.md"

def generate_markdown(images):
    """Generates Markdown for a responsive grid of four images per row."""
    rows = []
    row = []
    for i, img in enumerate(images, start=1):
        row.append(f"<img src='{img}' alt='Wallpaper' width='250px' style='margin: 10px;'>")  # Adjust width as needed
        if i % 4 == 0:  
            rows.append("<div style='display: flex; justify-content: center; gap: 10px;'>\n" + "\n".join(row) + "\n</div>")
            row = []
    if row:  
        rows.append("<div style='display: flex; justify-content: center; gap: 10px;'>\n" + "\n".join(row) + "\n</div>")
    return "\n".join(rows)

def main():
    images = [
        file for file in sorted(os.listdir(WALLPAPER_DIR))
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
    ]

    if not images:
        print("No wallpapers found.")
        return

    markdown = generate_markdown(images)

    readme_content = (
        "# Wallpaper Previews\n\n"
        "Here is a preview of all wallpapers in this repository:\n\n"
        + markdown
    )

    with open(README_FILE, "w") as readme:
        readme.write(readme_content)

if __name__ == "__main__":
    main()
