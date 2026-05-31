import re

def update_work_html():
    with open('work.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Google Fonts to include Cormorant Upright
    # Find the link tag
    font_link_regex = r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=Cormorant\+Garamond[^"]+"\s+rel="stylesheet">'
    new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=Cormorant+Upright:wght@300;400;500;600;700&family=Herr+Von+Muellerhoff&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">'
    
    if re.search(font_link_regex, content):
        content = re.sub(font_link_regex, new_font_link, content)
    else:
        # Fallback if regex fails
        content = content.replace('family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&', 'family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=Cormorant+Upright:wght@300;400;500;600;700&')

    # 2. Update CSS for .work-title and .cat-title
    # .work-title
    content = content.replace("font-family: 'Clearface', serif;\n            font-size: 4.5rem;", "font-family: 'Clearface', serif;\n            font-size: 4.5rem;")
    
    # .cat-title
    cat_title_css_old = """        .cat-title {
            font-family: 'Graphik', sans-serif;
            font-size: 0.8rem;
            letter-spacing: 0.25em;
            color: #000;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }"""
    
    cat_title_css_new = """        .cat-title {
            font-family: 'Clearface', serif;
            font-size: 1.1rem;
            letter-spacing: 0.2em;
            font-weight: 600;
            color: #000;
            margin-bottom: 0.2rem;
            text-transform: uppercase;
        }"""
    content = content.replace(cat_title_css_old, cat_title_css_new)
    
    # 3. Update cat-divider SVG
    # Find the cat-divider HTML
    divider_regex = r'<div class="cat-divider">.*?</div>'
    
    new_divider = """<div class="cat-divider" style="margin-top: 5px;">
                        <svg width="240" height="24" viewBox="0 0 240 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <!-- Left swooping curve -->
                            <path d="M 20 12 C 50 12 70 16 100 8" fill="none" stroke="#000" stroke-width="1.5" stroke-linecap="round"/>
                            <!-- Music Note -->
                            <path d="M 116 14.5 C 114 14.5 113 15.5 113 17 C 113 18.5 114.5 19.5 116 19.5 C 117.5 19.5 119 18.5 119 17 L 119 7 L 126 9 L 126 11 L 120.5 9.5 L 120.5 17 Z" fill="#000" />
                            <!-- Right swooping curve -->
                            <path d="M 140 8 C 170 16 190 12 220 12" fill="none" stroke="#000" stroke-width="1.5" stroke-linecap="round"/>
                        </svg>
                    </div>"""
    
    # Using re.DOTALL to match across newlines
    content = re.sub(divider_regex, new_divider, content, flags=re.DOTALL)

    with open('work.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_work_html()
