import re

svg_str = '<svg class="sparkle sp-{}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>'

def get_svgs(n):
    return ''.join([svg_str.format(i+1) for i in range(n)])

for filename in ['awards.html', 'build_awards.py']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # First, remove all existing sparkles to start fresh
    content = re.sub(r'<svg class="sparkle[^>]*>.*?</svg>', '', content)
    
    # Now inject exactly 6 SVGs before each <img src="assets/X.png"
    for i in range(5):
        target = f'<img src="assets/{i+1}.png"'
        replacement = get_svgs(6) + target
        content = re.sub(f'(<div class="summary-icon">)({target})', r'\1' + replacement, content)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
