import re

with open('d:/alanmenken/biography.html', 'r', encoding='utf-8') as f:
    html = f.read()

def inject_swashes(match):
    text = match.group(2)
    # Target characters: vowels and some nice swash letters
    targets = ['a', 'e', 'o', 'r', 'y', 's', 'l', 'm', 'n', 'A', 'E', 'O', 'R', 'S']
    import random
    random.seed(hash(text))
    
    result = ""
    count = 0
    max_swashes = max(1, len(text) // 5) # 1 swash per 5 chars roughly
    
    # We want a nice spread
    for char in text:
        if char in targets and count < max_swashes and random.random() > 0.6:
            result += f'<span class="swash">{char}</span>'
            count += 1
        else:
            result += char
            
    # If no swashes added, add one to the first target found
    if count == 0:
        res2 = ""
        added = False
        for char in text:
            if char in targets and not added:
                res2 += f'<span class="swash">{char}</span>'
                added = True
            else:
                res2 += char
        result = res2

    return match.group(1) + result + match.group(3)

# Find <h2 class="section-title">...</h2>
pattern = re.compile(r'(<h2 class="section-title">)(.*?)(</h2>)', re.IGNORECASE | re.DOTALL)
new_html = pattern.sub(inject_swashes, html)

with open('d:/alanmenken/biography.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Expanded swashes in biography.html")
