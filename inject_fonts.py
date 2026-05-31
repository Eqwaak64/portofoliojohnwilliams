import re

def inject_local_fonts():
    with open('faq.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The @font-face rules
    font_face_css = """
        @font-face {
            font-family: 'ITC Clearface';
            src: url('assets/fonts/ClearfaceStd-Regular.woff2') format('woff2');
            font-weight: 400;
            font-style: normal;
        }

        @font-face {
            font-family: 'ITC Clearface';
            src: url('assets/fonts/ClearfaceStd-Bold.woff2') format('woff2');
            font-weight: 700;
            font-style: normal;
        }

        @font-face {
            font-family: 'ITC Clearface';
            src: url('assets/fonts/ClearfaceStd-Heavy.woff2') format('woff2');
            font-weight: 900;
            font-style: normal;
        }
"""
    # Insert just after <style>
    if '@font-face' not in content:
        content = content.replace('<style>', '<style>' + font_face_css)

    # Let's ensure faq-question is very thick by using the Heavy font weight 900
    # Current weight is 700
    content = re.sub(
        r'(\.faq-question\s*\{[^}]*font-weight:\s*)700',
        r'\g<1>900',
        content
    )

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    inject_local_fonts()
