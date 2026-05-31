import re

def tweak_faq_again():
    with open('faq.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. faq-main: move further down
    content = re.sub(
        r'(\.faq-main\s*\{[^}]*padding-top:\s*)22vh',
        r'\g<1>28vh',
        content
    )

    # 2. faq-subtitle: larger font
    content = re.sub(
        r'(\.faq-subtitle\s*\{[^}]*font-size:\s*)1\.4rem',
        r'\g<1>1.65rem',
        content
    )

    # 3. faq-list: make it wider
    content = re.sub(
        r'(\.faq-list\s*\{[^}]*max-width:\s*)1100px',
        r'\g<1>1400px',
        content
    )

    # 4. faq-icon css: larger size
    content = re.sub(
        r'(\.faq-icon\s*\{[^}]*width:\s*)24px([^}]*height:\s*)24px',
        r'\g<1>32px\g<2>32px',
        content
    )

    # 5. faq-icon SVG: thicker stroke
    # find: stroke-width="1.5" inside the span class="faq-icon"
    content = content.replace('stroke-width="1.5"', 'stroke-width="2.2"')

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    tweak_faq_again()
