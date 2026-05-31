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

    # Find and replace the old transition JS
    # We look for "// Page Intro Transition" up to the end of the if block
    old_transition_pattern = r'// Page Intro Transition.*?\}\s*\n'
    
    new_transition_js = f"""// Page Intro Transition
        const pageTl = gsap.timeline();
        const hideElements = [{config['hide_elements']}];
        const titleEl = document.querySelector("{config['title_selector']}");
        
        if (titleEl) {{
            // 1. Hide everything else
            gsap.set(hideElements, {{ opacity: 0 }});
            
            // 2. Split text preserving HTML (for spans/svgs inside)
            const childNodes = Array.from(titleEl.childNodes);
            titleEl.innerHTML = '';
            childNodes.forEach(node => {{
                if (node.nodeType === 3) {{
                    const chars = node.nodeValue.split('');
                    chars.forEach(char => {{
                        if (char.trim() === '') {{
                            titleEl.appendChild(document.createTextNode(char));
                        }} else {{
                            const span = document.createElement('span');
                            span.style.display = 'inline-block';
                            span.className = 'title-char';
                            span.textContent = char;
                            titleEl.appendChild(span);
                        }}
                    }});
                }} else if (node.nodeType === 1) {{
                    node.style.display = 'inline-block';
                    node.classList.add('title-char');
                    titleEl.appendChild(node);
                }}
            }});

            // 3. Set initial center position for the whole title container
            gsap.set(titleEl, {{ y: "25vh", perspective: 800 }});
            
            // 4. Animate characters thrown in and snapping upright
            pageTl.from(".title-char", {{
                duration: 0.9,
                opacity: 0,
                scale: 1.5,
                x: () => gsap.utils.random(-150, 150),
                y: () => gsap.utils.random(-100, 200),
                z: () => gsap.utils.random(100, 300),
                rotationX: () => gsap.utils.random(70, 110), // laid flat
                rotationY: () => gsap.utils.random(-45, 45),
                rotationZ: () => gsap.utils.random(-45, 45),
                stagger: 0.08,
                ease: "back.out(2.5)" // snaps upright quickly
            }})
            // 5. Move title up to original position
            .to(titleEl, {{
                y: 0, 
                duration: 1.2, 
                ease: "power3.inOut"
            }}, "+=0.3")
            // 6. Fade in content
            .to(hideElements, {{
                opacity: 1, duration: 1.2, stagger: 0.1, ease: "power2.out"
            }}, "-=0.6");
        }}
"""

    if '// Page Intro Transition' in content:
        content = re.sub(old_transition_pattern, new_transition_js, content, flags=re.DOTALL)
    else:
        # Fallback if not found for some reason
        content = content.replace('document.addEventListener("DOMContentLoaded", () => {', 'document.addEventListener("DOMContentLoaded", () => {\n' + new_transition_js)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated page transitions with exploding characters.")
