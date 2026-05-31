import re

with open('d:/alanmenken/awards.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract from "const pageTl" up to the end of the if (titleEl) block
pattern = r'const pageTl = gsap\.timeline\(\);.*?\}\s*(?=const tl = gsap\.timeline)'

replacement = """const pageTl = gsap.timeline();
        const hideElements = [".header", ".awards-subtitle", ".awards-summary", ".awards-table-container"];
        const titleEl = document.querySelector(".awards-title");
        const heroSlices = document.querySelectorAll(".hero-slice");
        
        if (titleEl) {
            // 1. Hide everything else
            gsap.set(hideElements, { opacity: 0 });
            
            // 1b. Set initial state for hero slices (hidden below screen)
            gsap.set(heroSlices, { y: "100vh", opacity: 0 });
            
            // 2. Split text preserving HTML (for spans/svgs inside)
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

            // 3. Set initial center position for the whole title container
            gsap.set(titleEl, { y: "-62vh", perspective: 800 });
            
            // 4. Animate characters thrown in and snapping upright
            pageTl.from(".title-char", {
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
            })
            // 5. Move title down to original position
            .to(titleEl, {
                y: 0, 
                duration: 1.2, 
                ease: "power3.inOut"
            }, "+=0.3")
            // 6. Slices slide up sequentially to flush position
            .to(heroSlices, {
                y: 0,
                opacity: 1,
                duration: 0.8,
                stagger: 0.15,
                ease: "power3.out"
            }, "-=0.2")
            // 7. Slices adjust to staggered varied heights
            .to(heroSlices, {
                y: (index) => {
                    const offsets = ["-3vh", "3vh", "-5vh", "2vh", "-2vh"];
                    return offsets[index] || 0;
                },
                duration: 0.8,
                ease: "power2.inOut"
            }, "+=0.1")
            // 8. Fade in rest of content
            .to(hideElements, {
                opacity: 1, duration: 1.2, stagger: 0.1, ease: "power2.out"
            }, "-=0.6");
        }
        
        """

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('d:/alanmenken/awards.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
