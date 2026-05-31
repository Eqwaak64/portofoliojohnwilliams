import re

with open('d:/alanmenken/biography.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The script messed up the titles entirely. Let's just find each section by its id, and replace the h2 inside it.
sections = {
    'summary': '<h2 class="section-title">Biography <span class="swash">o</span>f J<span class="swash">o</span>hn Williams</h2>',
    'early-life': '<h2 class="section-title">E<span class="swash">a</span>rly Life &amp; Music<span class="swash">a</span>l F<span class="swash">o</span>undations</h2>',
    'apprentice': '<h2 class="section-title">H<span class="swash">o</span>llyw<span class="swash">o</span>od Apprentice Y<span class="swash">e</span>ars</h2>',
    'spielberg-lucas': '<h2 class="section-title">The Spi<span class="swash">e</span>lberg-L<span class="swash">u</span>cas Revol<span class="swash">u</span>tion</h2>',
    'golden-era': '<h2 class="section-title">The G<span class="swash">o</span>lden <span class="swash">E</span>ra</h2>',
    'legacy-expands': '<h2 class="section-title">The L<span class="swash">e</span>gacy <span class="swash">E</span>xpands</h2>',
    'summit': '<h2 class="section-title">The M<span class="swash">a</span>ster at the S<span class="swash">u</span>mmit</h2>',
    'legend': '<h2 class="section-title">The L<span class="swash">i</span>ving L<span class="swash">e</span>gend</h2>'
}

for section_id, new_h2 in sections.items():
    # find <section id="summary" ...> ... <h2 class="section-title">...</h2>
    # we need to be careful because the h2 is completely mangled
    pattern = re.compile(f'(<section id="{section_id}"[^>]*>.*?)(<h2 class="section-title">.*?</h2>)', re.DOTALL | re.IGNORECASE)
    html = pattern.sub(rf'\1{new_h2}', html)

with open('d:/alanmenken/biography.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed titles")
