
import re

with open("awards.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update HTML
html_pattern = r'<div class="awards-hero-carousel">.*?<!-- Page 1 -->.*?<div class="awards-hero page-1 active">(.*?)</div>.*?<!-- Page 2 -->.*?<div class="awards-hero page-2">(.*?)</div>.*?</div>'
html_replacement = r'<div class="awards-hero">\1\2</div>'
content = re.sub(html_pattern, html_replacement, content, flags=re.DOTALL)

# 2. Update CSS
css_pattern = r'\.awards-hero-carousel \{[^\}]+\}\s*\.awards-hero \{([^\}]+)position: absolute;[^\}]+opacity: 0;[^\}]+pointer-events: none;[^\}]+transition: [^\}]+transform: [^\}]+\}\s*\.awards-hero\.active \{[^\}]+\}'
css_replacement = r'.awards-hero {\1margin-bottom: 6rem;\n        }'
content = re.sub(css_pattern, css_replacement, content, flags=re.DOTALL)

# 3. Update JS
js_pattern = r'const heroPages = document\.querySelectorAll\('\.awards-hero'\);\s*// Update hero pages\s*heroPages\.forEach\(\(hero, idx\) => \{.*?\n\s*\}\);'
js_replacement = r''
content = re.sub(js_pattern, js_replacement, content, flags=re.DOTALL)

with open("awards.html", "w", encoding="utf-8") as f:
    f.write(content)

print("done")
