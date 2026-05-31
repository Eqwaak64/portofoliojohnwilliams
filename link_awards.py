import os

def link_awards_page():
    files = ['index.html', 'work.html', 'faq.html', 'awards.html']
    
    for filename in files:
        if not os.path.exists(filename):
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the Awards link in the menu
        # It looks like: <a href="#" class="menu-link">Awards</a>
        # Or in awards.html it might have it already, but we need to set it to active
        
        content = content.replace('<a href="#" class="menu-link">Awards</a>', '<a href="awards.html" class="menu-link">Awards</a>')
        
        # In awards.html, make it active
        if filename == 'awards.html':
            content = content.replace('<a href="awards.html" class="menu-link">Awards</a>', '<a href="awards.html" class="menu-link active">Awards</a>')
            # remove active from FAQ
            content = content.replace('<a href="faq.html" class="menu-link active">FAQ</a>', '<a href="faq.html" class="menu-link">FAQ</a>')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    link_awards_page()
