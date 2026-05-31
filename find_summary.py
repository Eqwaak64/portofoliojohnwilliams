import re

with open('d:/alanmenken/awards.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'<div class="awards-summary">(.*?)</div>\s*<!-- Awards Table -->', content, re.DOTALL)
if match:
    print(match.group(1)[:1000])
else:
    print('Not found')
