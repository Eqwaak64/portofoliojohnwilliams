import glob

old_svg = """<svg viewBox="0 0 24 24" fill="currentColor">
                <rect x="5.5" y="5" width="2" height="14" rx="0.5"/>
                <rect x="11" y="5" width="2" height="14" rx="0.5"/>
                <rect x="16.5" y="5" width="2" height="14" rx="0.5"/>
            </svg>"""

new_svg = """<svg viewBox="0 0 24 24" fill="currentColor">
                <rect x="4" y="4" width="3.5" height="16" rx="0.8"/>
                <rect x="10.25" y="4" width="3.5" height="16" rx="0.8"/>
                <rect x="16.5" y="4" width="3.5" height="16" rx="0.8"/>
            </svg>"""

for file in glob.glob('*.html'):
    if file in ["scratch_hero.html", "temp.html", "temp_extracted.html", "test_hero.html"]:
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_svg in content:
        content = content.replace(old_svg, new_svg)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Skipping {file} (SVG not found or already modified)")
