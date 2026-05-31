import re

def fix_fonts_and_spacing():
    files = ['index.html', 'work.html', 'faq.html']
    
    # 1. New Font Link
    old_font_regex = r'<link\s+href="https://fonts\.googleapis\.com/css2\?[^"]+"\s+rel="stylesheet">'
    new_font_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&family=Cormorant+Upright:wght@300;400;500;600;700&family=Herr+Von+Muellerhoff&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">'
    
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace font link
        if re.search(old_font_regex, content):
            content = re.sub(old_font_regex, new_font_link, content)
            
        if filename == 'faq.html':
            # 2. Fix Spacing in FAQ
            # .faq-header-content margin-bottom
            content = content.replace("margin-bottom: 8vh;", "margin-bottom: 12vh;")
            
            # .faq-question padding
            content = content.replace("padding: 2.2rem 0;", "padding: 3rem 0;")
            
            # Make the title FaQ use Cormorant Upright to see if it matches better (or keep Garamond? The user said "huruf yang digunakan disini agak tebal". They meant the questions.)
            # I will ensure .faq-question has font-weight: 700 and font-size: 1.6rem
            content = content.replace("font-size: 1.4rem;\n            font-weight: 700;", "font-size: 1.55rem;\n            font-weight: 700;\n            letter-spacing: 0.01em;")
            
            # Subtitle is 1.15rem, make it 1.25rem
            content = content.replace("font-size: 1.15rem;\n            font-weight: 600;", "font-size: 1.15rem;\n            font-weight: 500;")
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    fix_fonts_and_spacing()
