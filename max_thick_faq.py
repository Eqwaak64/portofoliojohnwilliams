import re

def max_thick_faq():
    with open('faq.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. faq-question: much larger and much thicker
    content = re.sub(
        r'(\.faq-question\s*\{[^}]*font-size:\s*)1\.8rem([^}]*-webkit-text-stroke:\s*)0\.5px',
        r'\g<1>2.3rem\g<2>1px',
        content
    )

    # 2. faq-icon css: much larger size
    content = re.sub(
        r'(\.faq-icon\s*\{[^}]*width:\s*)32px([^}]*height:\s*)32px',
        r'\g<1>44px\g<2>44px',
        content
    )

    # 3. faq-icon SVG: much thicker stroke
    content = content.replace('stroke-width="2.2"', 'stroke-width="3.5"')

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    max_thick_faq()
