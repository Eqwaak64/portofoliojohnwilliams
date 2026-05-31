import re

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Resize icons
content = content.replace('width: 28px;', 'width: 20px;')
content = content.replace('height: 28px;', 'height: 20px;')
# Also reduce logo-text size slightly just in case
content = content.replace('font-size: 1.2rem;', 'font-size: 1.1rem;')

# 2. Change font-family for .swash to Desire
content = content.replace("font-family: 'Lust Script', 'Desire', cursive;", "font-family: 'Desire', cursive;")
content = content.replace("font-size: 1.05em;", "font-size: 0.95em;")

# 3. Strip existing swashes
content = re.sub(r'<span class="swash">(.*?)</span>', r'\1', content)

# 4. Apply varied swashes
replacements = {
    'The Lit<span class="star-wrapper">t<svg': '<span class="swash">T</span>he Li<span class="swash">t</span><span class="star-wrapper">t<svg',
    'le Mermai<span class="star-wrapper">d<svg': 'le <span class="swash">M</span>ermai<span class="star-wrapper">d<svg',
    
    'Beauty a<span class="star-wrapper">n<svg': '<span class="swash">B</span>eauty a<span class="star-wrapper">n<svg',
    'd t<span class="star-wrapper">h<svg': 'd t<span class="star-wrapper">h<svg', # revert this to default
    'e Bea<span class="star-wrapper">s<svg': 'e <span class="swash">B</span>ea<span class="star-wrapper">s<svg',
    
    'Aladdi<span class="star-wrapper">n<svg': '<span class="swash">A</span>ladd<span class="swash">i</span><span class="star-wrapper">n<svg',
    
    '">Pocahontas<': '"><span class="swash">P</span>ocahont<span class="swash">a</span>s<',
    
    '">The Hunchback of Notre Dame<': '"><span class="swash">T</span>he <span class="swash">H</span>unchback o<span class="swash">f</span> <span class="swash">N</span>otre <span class="swash">D</span>ame<',
    
    '">Hercules<': '"><span class="swash">H</span>ercul<span class="swash">e</span>s<',
    
    'Little Shop of H<span class="star-wrapper">o<svg': '<span class="swash">L</span>ittle <span class="swash">S</span>hop o<span class="swash">f</span> <span class="swash">H</span><span class="star-wrapper">o<svg',
    
    'New<span class="star-wrapper">s<svg': 'N<span class="swash">e</span>w<span class="star-wrapper">s<svg',
    
    'A Christmas C<span class="star-wrapper">a<svg': '<span class="swash">A</span> <span class="swash">C</span>hristm<span class="swash">a</span>s <span class="swash">C</span><span class="star-wrapper">a<svg',
    
    'Enchant<span class="star-wrapper">e<svg': '<span class="swash">E</span>nchant<span class="star-wrapper">e<svg',
    
    'Tangl<span class="star-wrapper">e<svg': '<span class="swash">T</span>angl<span class="star-wrapper">e<svg',
    'd: The S<span class="star-wrapper">e<svg': 'd: <span class="swash">T</span>he <span class="swash">S</span><span class="star-wrapper">e<svg',
    
    'Galav<span class="star-wrapper">a<svg': '<span class="swash">G</span>alav<span class="star-wrapper">a<svg',
    
    'G<span class="star-wrapper">o<svg': '<span class="swash">G</span><span class="star-wrapper">o<svg',
    'd Bless Y<span class="star-wrapper">o<svg': 'd <span class="swash">B</span>less Y<span class="star-wrapper">o<svg',
    'u Mr. R<span class="star-wrapper">o<svg': 'u <span class="swash">M</span>r. <span class="swash">R</span><span class="star-wrapper">o<svg',
    
    '">King David<': '"><span class="swash">K</span>ing <span class="swash">D</span>avi<span class="swash">d</span><',
    
    '">Sister Act<': '"><span class="swash">S</span>ister <span class="swash">A</span>c<span class="swash">t</span><',
    
    'Ho<span class="star-wrapper">w<svg': '<span class="swash">H</span>o<span class="star-wrapper">w<svg',
    'Linc<span class="star-wrapper">o<svg': '<span class="swash">L</span>inc<span class="star-wrapper">o<svg',

    # Duplicates without stars
    '">Little Shop of Horrors<': '"><span class="swash">L</span>ittle <span class="swash">S</span>hop o<span class="swash">f</span> <span class="swash">H</span>orrors<',
    '">Beauty and the Beast<': '"><span class="swash">B</span>eauty and t<span class="swash">h</span>e <span class="swash">B</span>east<',
    '">A Christmas Carol<': '"><span class="swash">A</span> <span class="swash">C</span>hristm<span class="swash">a</span>s <span class="swash">C</span>arol<',
    '">Aladdin<': '"><span class="swash">A</span>ladd<span class="swash">i</span>n<',
    '">Newsies<': '">N<span class="swash">e</span>wsies<',
    '">The Little Mermaid<': '"><span class="swash">T</span>he Li<span class="swash">t</span>tle <span class="swash">M</span>ermaid<'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(content)
