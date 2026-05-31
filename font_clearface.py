import re

def update_fonts_to_clearface():
    with open('faq.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. faq-question: Use ITC Clearface and increase size
    content = re.sub(
        r'(\.faq-question\s*\{[^}]*font-family:\s*)\'Cormorant Garamond\',\s*serif;([^}]*font-size:\s*)2\.3rem',
        r"\g<1>'ITC Clearface', 'Clearface', 'Cormorant Garamond', serif;\g<2>2.6rem",
        content
    )

    # 2. faq-answer: Use ITC Clearface and increase size
    content = re.sub(
        r'(\.faq-answer\s*\{[^}]*font-family:\s*)\'Cormorant Garamond\',\s*serif;([^}]*font-size:\s*)1\.25rem',
        r"\g<1>'ITC Clearface', 'Clearface', 'Cormorant Garamond', serif;\g<2>1.5rem",
        content
    )
    
    # 3. faq-subtitle: Let's also ensure it uses Clearface if they want consistency? 
    # User said: "font yang pertanyaan dan jawabannya pakai font itc clearface". 
    # I'll just change question and answer as requested.

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_fonts_to_clearface()
