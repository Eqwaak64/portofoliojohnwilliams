import re
with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'<h2 class="work-title"[^>]*>\s*(.*?)\s*</h2>', content, flags=re.DOTALL)
print("First match:", matches[0] if matches else "No match")
