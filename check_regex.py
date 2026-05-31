import re

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'<h2 class="work-title"[^>]*>\s*.*?\s*</h2>', content, flags=re.DOTALL)
print(f"Found {len(matches)} matches")
if matches:
    print(matches[0])
