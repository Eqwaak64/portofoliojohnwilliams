import sys

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.work-page-title' in line or '.logo-text' in line or '.work-title' in line:
        # print 5 lines before and after
        start = max(0, i - 5)
        end = min(len(lines), i + 6)
        print(f"--- Line {i} Match: {line.strip()} ---")
        for j in range(start, end):
            print(f"{j+1}: {lines[j].rstrip()}")
