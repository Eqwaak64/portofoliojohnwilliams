import re
import random
random.seed(42)

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

def clean_text(text):
    # Remove all <span> tags entirely
    text = re.sub(r'<span[^>]*>', '', text)
    text = text.replace('</span>', '')
    # Remove the svg entirely
    text = re.sub(r'<svg.*?</svg>', '', text)
    return text.strip()

def process_title(match):
    prefix = match.group(1)
    raw_text = clean_text(match.group(2))
    
    words = raw_text.split(' ')
    result_words = []
    
    for word in words:
        if not word: continue
        chars = list(word)
        
        # Add swash to the first letter of words longer than 2 chars
        if len(word) > 2 and chars[0].isalpha():
            chars[0] = f'<span class="swash">{chars[0]}</span>'
            
        # Maybe add a swash to one other letter if word is very long
        if len(word) > 6:
            middle_indices = [i for i, c in enumerate(chars) if i > 1 and i < len(chars)-1 and c.isalpha()]
            if middle_indices:
                idx = random.choice(middle_indices)
                chars[idx] = f'<span class="swash">{chars[idx]}</span>'
                
        # Maybe add a star to a vowel
        vowels = [i for i, c in enumerate(chars) if c.lower() in 'aeiou' and '<' not in c]
        if vowels and random.random() > 0.5:
            v_idx = random.choice(vowels)
            c = chars[v_idx]
            chars[v_idx] = f'<span class="star-wrapper">{c}<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>'
            
        result_words.append(''.join(chars))
        
    final_text = ' '.join(result_words)
    
    # Always make sure the very last letter is a swash if it isn't already
    # Actually, let's just do a regex replace for the last letter
    def replace_last(m):
        return f'<span class="swash">{m.group(1)}</span>'
    final_text = re.sub(r'([a-zA-Z])([^a-zA-Z]*)$', replace_last, final_text)
    
    return prefix + final_text + '</h2>'

new_content = re.sub(r'(<h2[^>]*class="[^"]*work-title[^"]*"[^>]*>)\s*(.*?)\s*</h2>', process_title, content, flags=re.DOTALL)

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Done expanding swashes!")
