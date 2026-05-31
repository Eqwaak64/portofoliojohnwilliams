import sys

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'font-weight' in line or 'fontWeight' in line:
        print(f"Line {i+1}: {line.strip()}")
