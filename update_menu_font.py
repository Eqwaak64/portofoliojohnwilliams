import glob
import re

html_files = glob.glob("*.html")

for file in html_files:
    if file.startswith("scratch") or file.startswith("temp") or file.startswith("test"):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update .menu-link font-size: Xrem; to font-size: 2.8rem;
    pattern = r'(\.menu-link\s*\{[^}]*?font-size:\s*)[0-9.]+rem;'
    new_content = re.sub(pattern, r'\g<1>2.8rem;', content, flags=re.DOTALL)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated .menu-link in {file}")

print("All files processed.")
