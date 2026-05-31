import re

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

title_html = '''        <h1 class="work-page-title" style="font-family: 'Clearface', serif; font-size: 5rem; font-weight: 700; color: #000; text-align: center; margin-top: 4rem; z-index: 10;">W<span class="star-wrapper">o<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>rk</h1>'''

content = content.replace('<div class="work-list">', '<div class="work-list">\n' + title_html)

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(content)
