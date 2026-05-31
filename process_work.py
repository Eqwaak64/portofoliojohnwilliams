import re
import random

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_title(match):
    prefix = match.group(1)
    text = match.group(2).strip()
    
    if '<span' in text:
        return match.group(0)
    
    chars = list(text)
    
    # Track original casing and spaces
    if len(chars) > 0 and chars[0].isalpha():
        chars[0] = f'<span class="swash">{chars[0]}</span>'
        
    vowels = [i for i, c in enumerate(chars) if c.lower() in 'aeiou' and not c.startswith('<')]
    if vowels:
        v_idx = vowels[len(vowels) // 2]
        c = chars[v_idx]
        chars[v_idx] = f'<span class="star-wrapper">{c}<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>'
        
    consonants = [i for i, c in enumerate(chars) if c.isalpha() and c.lower() not in 'aeiou' and not c.startswith('<')]
    if consonants:
        c_idx = consonants[-1]
        chars[c_idx] = f'<span class="swash">{chars[c_idx]}</span>'
        
    res = prefix + ''.join(chars) + '</h2>'
    # Debug
    # print("Replaced:", text, "->", ''.join(chars))
    return res

new_content = re.sub(r'(<h2 class="work-title"[^>]*>)\s*(.*?)\s*</h2>', replace_title, content, flags=re.DOTALL)

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Done!")
