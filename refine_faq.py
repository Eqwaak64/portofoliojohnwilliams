import re

def refine_faq_styles():
    with open('faq.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. faq-main: padding-top from 15vh to 22vh
    content = re.sub(
        r'(\.faq-main\s*\{[^}]*padding-top:\s*)15vh',
        r'\g<1>22vh',
        content
    )

    # 2. faq-title: font-weight 700, tighter letter spacing
    content = re.sub(
        r'(\.faq-title\s*\{[^}]*font-weight:\s*)400([^}]*letter-spacing:\s*)0\.05em',
        r'\g<1>700\g<2>-0.01em',
        content
    )
    # also add -webkit-text-stroke to FaQ to make it very bold
    content = re.sub(
        r'(\.faq-title\s*\{[^}]*margin-bottom:\s*1rem;)',
        r'\g<1>\n            -webkit-text-stroke: 1px currentColor;',
        content
    )

    # 3. faq-subtitle: larger and bolder
    content = re.sub(
        r'(\.faq-subtitle\s*\{[^}]*font-size:\s*)1\.15rem([^}]*font-weight:\s*)500',
        r'\g<1>1.4rem\g<2>700',
        content
    )
    # Update subtitle color slightly darker
    content = re.sub(
        r'(\.faq-subtitle\s*\{[^}]*color:\s*)rgba\(26,\s*26,\s*26,\s*0\.6\)',
        r'\g<1>rgba(26, 26, 26, 0.8)',
        content
    )

    # 4. faq-list: wider
    content = re.sub(
        r'(\.faq-list\s*\{[^}]*max-width:\s*)900px',
        r'\g<1>1100px',
        content
    )

    # 5. faq-question: larger and thicker
    content = re.sub(
        r'(\.faq-question\s*\{[^}]*font-size:\s*)1\.55rem',
        r'\g<1>1.8rem',
        content
    )
    # Add text-stroke to faq-question for extra thickness
    content = re.sub(
        r'(\.faq-question\s*\{[^}]*color:\s*#1a1a1a;)',
        r'\g<1>\n            -webkit-text-stroke: 0.5px currentColor;',
        content
    )

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    refine_faq_styles()
