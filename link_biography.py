import glob

def link_biography():
    for file in glob.glob('*.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We need to replace `<a href="#" class="menu-link">Biography</a>` 
        # or `<a href="biography.html" class="menu-link">Biography</a>` (just to be safe)
        if '<a href="#" class="menu-link">Biography</a>' in content:
            content = content.replace('<a href="#" class="menu-link">Biography</a>', '<a href="biography.html" class="menu-link">Biography</a>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated links in {file}")

if __name__ == '__main__':
    link_biography()
