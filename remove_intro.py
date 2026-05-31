import re

files = ['work.html', 'awards.html', 'faq.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if intro-screen exists
    if 'intro-screen' in content:
        # We need to remove the intro-screen div. It starts with <!-- Intro Screen --> and ends before <!-- Menu Dropdown -->
        # Using a more robust regex to remove the intro screen div
        content = re.sub(r'<!-- Intro Screen -->\s*<div id="intro-screen">.*?</div>\s*', '', content, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Removed intro-screen from {f}")
    else:
        print(f"No intro-screen in {f}")

