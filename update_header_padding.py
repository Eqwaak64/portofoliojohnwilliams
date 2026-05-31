import glob

for file in glob.glob('*.html'):
    if file in ["scratch_hero.html", "temp.html", "temp_extracted.html", "test_hero.html"]:
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'padding: 2.5rem 4rem;' in content:
        content = content.replace('padding: 2.5rem 4rem;', 'padding: 2.5rem 3rem;')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Skipping {file}")
