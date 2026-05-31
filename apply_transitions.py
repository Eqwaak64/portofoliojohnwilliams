import re

files_to_update = {
    'biography.html': {
        'title_selector': '.bio-title',
        'hide_elements': '".header", ".bio-subtitle", ".bio-hero-scene", ".bio-separator", ".bio-content-wrapper"',
    },
    'awards.html': {
        'title_selector': '.awards-title',
        'hide_elements': '".header", ".awards-subtitle", ".awards-summary", ".awards-table-container"',
    },
    'faq.html': {
        'title_selector': '.faq-title',
        'hide_elements': '".header", ".faq-subtitle", ".faq-list"',
    }
}

for filename, config in files_to_update.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove intro HTML if it exists
    content = re.sub(r'<!-- Intro Screen -->\s*<div id="intro-screen">.*?</div>\s*<!-- Menu Dropdown -->', '<!-- Menu Dropdown -->', content, flags=re.DOTALL)
        
    # 2. Remove intro JS if it exists
    content = re.sub(r'// --- Intro Screen Logic ---.*?(?=//)', '//', content, flags=re.DOTALL)
        
    # 3. Remove existing entrance animations
    content = re.sub(r'// Entrance animation\s*gsap\.from\(".faq-header-content".*?\);\s*gsap\.from\(".faq-item".*?\);', '', content, flags=re.DOTALL)

    # 4. Add the new page transition
    transition_js = f"""
        // Page Intro Transition
        const pageTl = gsap.timeline();
        const hideElements = [{config['hide_elements']}];
        const titleEl = document.querySelector("{config['title_selector']}");
        
        if (titleEl) {{
            // Ensure no layout shift by using visibility or opacity
            gsap.set(hideElements, {{ opacity: 0 }});
            
            pageTl.fromTo(titleEl, 
                {{ y: "25vh", scale: 1.25, opacity: 0 }},
                {{ y: "25vh", scale: 1.25, opacity: 1, duration: 1.2, ease: "power3.out", delay: 0.2 }}
            )
            .to(titleEl, {{
                y: 0, scale: 1, duration: 1.2, ease: "power3.inOut"
            }}, "+=0.3")
            .to(hideElements, {{
                opacity: 1, duration: 1.2, stagger: 0.1, ease: "power2.out"
            }}, "-=0.6");
        }}
    """
    
    # Insert it right after the DOMContentLoaded wrapper
    content = content.replace('document.addEventListener("DOMContentLoaded", () => {', 'document.addEventListener("DOMContentLoaded", () => {' + transition_js)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated page transitions.")
