import re

with open('awards.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Header
content = content.replace('<div class="col-song">SONG</div>', '<div class="col-song">SONG / WORK</div>')

# Replace Signature
content = content.replace('<div class="awards-signature">Alan Menken</div>', '<div class="awards-signature">John Williams</div>')

# Replace Subtitle
content = content.replace('See the full list of all the awards that Alan has won.', 'See the full list of all the awards that John has won.')

# Replace Rows
with open('new_rows.html', 'r', encoding='utf-8') as f:
    new_rows = f.read()

pattern = re.compile(r'<div class="awards-row">.*?(?=<div style="height: 10vh;"></div>)', re.DOTALL)
content = pattern.sub(new_rows, content)

with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(content)
