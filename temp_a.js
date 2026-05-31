
    document.addEventListener("DOMContentLoaded", () => {
        // Page Intro Transition
        const pageTl = gsap.timeline();
        const hideElements = [".header", ".awards-hero", ".awards-subtitle", ".awards-summary", ".awards-table-container"];
        const titleEl = document.querySelector(".awards-title");
        
        if (titleEl) {
            // 1. Hide everything else
            gsap.set(hideElements, { opacity: 0 });
            
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
    
        // Hamburger Menu Logic
        const menuToggle = document.getElementById('menu-toggle');
        const menuOverlay = document.querySelector('.menu-overlay');

        menuToggle.addEventListener('click', () => {
            menuOverlay.classList.toggle('open');
            document.body.classList.toggle('menu-active');
        });

        // News Sidebar Logic
        const newsBtn = document.getElementById('news-btn');
        const newsSidebar = document.getElementById('news-sidebar');
        const newsClose = document.getElementById('news-close');

        newsBtn.addEventListener('click', () => {
            newsSidebar.classList.add('open');
            document.body.classList.add('news-active');
        });

        newsClose.addEventListener('click', () => {
            newsSidebar.classList.remove('open');
            document.body.classList.remove('news-active');
        });
        
        // FAQ Accordion Logic
        const faqItems = document.querySelectorAll('.faq-item');
        
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            const answer = item.querySelector('.faq-answer');
            
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                
                // Close all others
                faqItems.forEach(otherItem => {
                    if(otherItem !== item && otherItem.classList.contains('active')) {
                        otherItem.classList.remove('active');
                        gsap.to(otherItem.querySelector('.faq-answer'), {
                            height: 0,
                            opacity: 0,
                            duration: 0.4,
                            ease: "power2.inOut"
                        });
                    }
                });
                
                // Toggle current
                if (isActive) {
                    item.classList.remove('active');
                    gsap.to(answer, {
                        height: 0,
                        opacity: 0,
                        duration: 0.4,
                        ease: "power2.inOut"
                    });
                } else {
                    item.classList.add('active');
                    gsap.set(answer, { height: "auto" });
                    const targetHeight = answer.offsetHeight;
                    gsap.set(answer, { height: 0 });
                    
                    gsap.to(answer, {
                        height: targetHeight,
                        opacity: 1,
                        duration: 0.5,
                        ease: "power3.out"
                    });
                }
            });
        });
        
        
    });
    