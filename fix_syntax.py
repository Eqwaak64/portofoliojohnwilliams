import re
for f in ['biography.html', 'awards.html', 'faq.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Target the specific block of lines
    content = re.sub(r'gsap\.from\("\.intro-enter".*?\);\s*\}\);', 'gsap.from(".intro-enter", { opacity: 0, y: 20, duration: 1.5, ease: "power2.out", delay: 2 });', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
