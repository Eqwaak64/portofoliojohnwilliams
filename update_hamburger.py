import glob
import os

css_addition = """
        #menu-toggle svg rect {
            transition: transform 0.4s cubic-bezier(0.77, 0, 0.175, 1);
        }

        #menu-toggle svg rect:nth-child(2) {
            transform: translateY(-2.5px);
        }

        #menu-toggle:hover svg rect:nth-child(1),
        #menu-toggle:hover svg rect:nth-child(3),
        body.menu-active #menu-toggle svg rect:nth-child(1),
        body.menu-active #menu-toggle svg rect:nth-child(3) {
            transform: translateY(-2.5px);
        }

        #menu-toggle:hover svg rect:nth-child(2),
        body.menu-active #menu-toggle svg rect:nth-child(2) {
            transform: translateY(2.5px);
        }
"""

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '#menu-toggle svg rect {' in content:
        print(f"Skipping {file}, already updated.")
        continue
    
    # Find the insertion point
    insert_after = """        .icon-btn svg {
            width: 24px;
            height: 24px;
            fill: currentColor;
        }"""
    
    if insert_after in content:
        new_content = content.replace(insert_after, insert_after + "\n" + css_addition)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Could not find insertion point in {file}")
