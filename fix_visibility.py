import os
import glob

html_files = glob.glob("*.html")

for file in html_files:
    if file.startswith("scratch") or file.startswith("temp") or file.startswith("test"):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the visibility property from .hidden-logo
    if 'visibility: hidden !important;' in content:
        content = content.replace('visibility: hidden !important;', '')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed visibility issue in {file}")

print("All files processed.")
