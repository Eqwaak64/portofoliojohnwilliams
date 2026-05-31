import re

def update_files():
    files = ['index.html', 'work.html']
    
    # 1. New bell SVG
    bell_svg = '''<svg viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2c-.8 0-1.5.7-1.5 1.5v.68c-2.83.48-5 2.94-5 6.07v5l-2.5 2.5v1h18v-1L18.5 15.25v-5c0-3.13-2.17-5.59-5-6.07V3.5C13.5 2.7 12.8 2 12 2zm-2 18c0 1.1.9 2 2 2s2-.9 2-2h-4z"/>
            </svg>'''
    
    # 2. New hamburger SVG
    hamburger_svg = '''<svg viewBox="0 0 24 24" fill="currentColor">
                <rect x="5.5" y="5" width="2" height="14" rx="0.5"/>
                <rect x="11" y="5" width="2" height="14" rx="0.5"/>
                <rect x="16.5" y="5" width="2" height="14" rx="0.5"/>
            </svg>'''
            
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace hamburger
        # We need to find the <button class="icon-btn" id="menu-toggle"> block
        h_pattern = r'<button class="icon-btn" id="menu-toggle">.*?</button>'
        h_repl = f'<button class="icon-btn" id="menu-toggle">\n            {hamburger_svg}\n        </button>'
        content = re.sub(h_pattern, h_repl, content, flags=re.DOTALL)
        
        # Replace bell
        b_pattern = r'<button class="icon-btn" id="news-btn">.*?</button>'
        b_repl = f'<button class="icon-btn" id="news-btn">\n            {bell_svg}\n        </button>'
        content = re.sub(b_pattern, b_repl, content, flags=re.DOTALL)
        
        if filename == 'work.html':
            # Update font weights in work.html
            # .work-title
            content = content.replace("font-family: 'Clearface', serif;\n            font-size: 4.5rem;\n            font-weight: 400;", "font-family: 'Clearface', serif;\n            font-size: 4.5rem;\n            font-weight: 700;")
            
            # .cat-title
            content = content.replace("font-family: 'Clearface', serif;\n            font-size: 1.1rem;\n            letter-spacing: 0.2em;\n            font-weight: 600;", "font-family: 'Clearface', serif;\n            font-size: 1.1rem;\n            letter-spacing: 0.2em;\n            font-weight: 700;")
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    update_files()
