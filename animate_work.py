import re

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The GSAP logic
gsap_logic = """
        // Page Intro Transition
        const pageTl = gsap.timeline();
        const hideElements = [".header", ".work-category", ".work-title"];
        const titleEl = document.querySelector(".work-page-title");
        
        if (titleEl) {
            // 1. Hide everything else
            gsap.set(hideElements, { opacity: 0 });
            
            // 2. Split text preserving HTML
            const childNodes = Array.from(titleEl.childNodes);
            titleEl.innerHTML = '';
            childNodes.forEach(node => {
                if (node.nodeType === 3) {
                    const chars = node.nodeValue.split('');
                    chars.forEach(char => {
                        if (char.trim() === '') {
                            titleEl.appendChild(document.createTextNode(char));
                        } else {
                            const span = document.createElement('span');
                            span.style.display = 'inline-block';
                            span.className = 'title-char';
                            span.textContent = char;
                            titleEl.appendChild(span);
                        }
                    });
                } else if (node.nodeType === 1) {
                    node.style.display = 'inline-block';
                    node.classList.add('title-char');
                    titleEl.appendChild(node);
                }
            });

            // 3. Set initial center position
            gsap.set(titleEl, { y: "25vh", perspective: 800 });
            
            // 4. Animate characters thrown in and snapping upright
            pageTl.from(".title-char", {
                duration: 0.9,
                opacity: 0,
                scale: 1.5,
                x: () => gsap.utils.random(-150, 150),
                y: () => gsap.utils.random(-100, 200),
                z: () => gsap.utils.random(100, 300),
                rotationX: () => gsap.utils.random(70, 110),
                rotationY: () => gsap.utils.random(-45, 45),
                rotationZ: () => gsap.utils.random(-45, 45),
                stagger: 0.08,
                ease: "back.out(2.5)"
            })
            // 5. Move title up to original position
            .to(titleEl, {
                y: 0, 
                duration: 1.2, 
                ease: "power3.inOut"
            }, "+=0.3")
            // 6. Fade in content
            .to(hideElements, {
                opacity: 1, duration: 1.2, stagger: 0.1, ease: "power2.out"
            }, "-=0.6");
        }
"""

# Insert GSAP logic at the start of DOMContentLoaded
content = content.replace('document.addEventListener("DOMContentLoaded", () => {', 'document.addEventListener("DOMContentLoaded", () => {' + gsap_logic)

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(content)
