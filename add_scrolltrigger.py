import re

with open('d:/alanmenken/awards.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add ScrollTrigger script after gsap.min.js
gsap_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>'
scroll_trigger_script = '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>'

if scroll_trigger_script not in content:
    content = content.replace(gsap_script, gsap_script + '\n    ' + scroll_trigger_script)

with open('d:/alanmenken/awards.html', 'w', encoding='utf-8') as f:
    f.write(content)
