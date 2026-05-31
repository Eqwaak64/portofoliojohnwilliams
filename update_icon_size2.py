import glob
import re

for file in glob.glob('*.html'):
    if file in ["scratch_hero.html", "temp.html", "temp_extracted.html", "test_hero.html"]:
        continue

    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update .icon-btn svg size from 34px to 44px
    content = re.sub(
        r'\.icon-btn svg \{\s*width: \d+px;\s*height: \d+px;\s*fill: currentColor;\s*\}',
        '.icon-btn svg {\n            width: 44px;\n            height: 44px;\n            fill: currentColor;\n        }',
        content
    )

    # 2. Update translateY for hamburger animation
    content = content.replace('translateY(-4px)', 'translateY(-5px)')
    content = content.replace('translateY(4px)', 'translateY(5px)')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {file}")
