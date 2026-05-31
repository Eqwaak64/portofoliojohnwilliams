
    document.addEventListener("DOMContentLoaded", () => {
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

            // Preload Bickham Script font to ensure it's available instantly on hover
            const preloadFont = document.createElement('div');
            preloadFont.style.fontFamily = "'Bickham Script Pro', cursive";
            preloadFont.style.position = 'absolute';
            preloadFont.style.opacity = '0';
            preloadFont.style.pointerEvents = 'none';
            preloadFont.textContent = 'preload';
            document.body.appendChild(preloadFont);

            let currentBgAnim;
            const bgImg = document.getElementById('work-bg');

            // Split .work-title for letter-by-letter hover color fill AND click interactions
            document.querySelectorAll('.work-title').forEach(title => {
                const titleChildNodes = Array.from(title.childNodes);
                title.innerHTML = '';
                titleChildNodes.forEach(node => {
                    if (node.nodeType === 3) {
                        const chars = node.nodeValue.split('');
                        chars.forEach(char => {
                            if (char === ' ') {
                                title.appendChild(document.createTextNode('\u00A0')); // Use non-breaking space like the original code
                            } else if (char.trim() !== '') {
                                const span = document.createElement('span');
                                span.className = 'hover-char char';
                                span.style.display = 'inline-block';
                                span.textContent = char;
                                title.appendChild(span);
                            }
                        });
                    } else if (node.nodeType === 1) {
                        // Wrap the element in hover-char to isolate GSAP transforms
                        const wrapper = document.createElement('span');
                        wrapper.className = 'hover-char char';
                        wrapper.style.display = 'inline-block';
                        wrapper.style.transformStyle = 'preserve-3d';
                        
                        node.style.display = 'inline-block';
                        wrapper.appendChild(node);
                        title.appendChild(wrapper);
                    }
                });

                const chars = title.querySelectorAll('.hover-char');
                const swashes = title.querySelectorAll('.swash');

                let hoverTimeouts = [];

                // Initialize styles
                if (title.classList.contains('active')) {
                    chars.forEach(char => { char.style.color = '#000'; });
                } else {
                    chars.forEach(char => { char.style.color = 'rgba(0,0,0,0.3)'; });
                }

                // Hover Interaction
                title.addEventListener('mouseenter', () => {
                    hoverTimeouts.forEach(t => clearTimeout(t)); // Clear any reversing timeouts
                    hoverTimeouts = [];

                    // PURE Disney Squash and Stretch Physics!
                    gsap.set(chars, { transformOrigin: "50% 100%" });
                    gsap.to(chars, {
                        keyframes: [
                            { y: 0, scaleY: 0.5, scaleX: 1.3, rotationZ: -10, duration: 0.15, ease: "power2.inOut" },
                            { y: -45, scaleY: 1.5, scaleX: 0.6, rotationZ: 10, duration: 0.2, ease: "power2.out" },
                            { y: -50, scaleY: 1, scaleX: 1, rotationZ: 0, duration: 0.15, ease: "sine.inOut" },
                            { y: 0, scaleY: 0.6, scaleX: 1.4, rotationZ: 0, duration: 0.15, ease: "power2.in" },
                            { y: 0, scaleY: 1, scaleX: 1, rotationZ: 0, duration: 0.5, ease: "elastic.out(1.5, 0.4)" }
                        ],
                        stagger: { each: 0.04, from: "start" },
                        overwrite: "auto"
                    });

                    // JS Stagger for Color and Font Swap
                    chars.forEach((char, i) => {
                        const timeout = setTimeout(() => {
                            char.style.transition = 'color 0.2s ease';
                            char.style.color = '#000';
                            
                            const swash = char.querySelector('.swash');
                            if (swash) {
                                swash.style.transition = 'none';
                                swash.style.fontFamily = "'Bickham Script Pro', cursive";
                                swash.style.fontSize = "1.7em";
                                swash.style.marginRight = "0.04em";
                                swash.style.marginLeft = "0.02em";
                                swash.style.lineHeight = "0.5";
                            }
                        }, i * 20);
                        hoverTimeouts.push(timeout);
                    });
                });

                title.addEventListener('mouseleave', () => {
                    hoverTimeouts.forEach(t => clearTimeout(t)); // Clear any forward timeouts
                    hoverTimeouts = [];
                    const isActive = title.classList.contains('active');

                    // Reset Transforms cleanly
                    gsap.to(chars, {
                        y: 0,
                        rotationZ: 0,
                        scale: 1,
                        scaleY: 1,
                        scaleX: 1,
                        duration: 0.4,
                        ease: "power2.out",
                        overwrite: "auto"
                    });

                    // Fast Reverse Stagger for Color and Font Swap
                    chars.forEach((char, i) => {
                        const timeout = setTimeout(() => {
                            char.style.transition = 'color 0.2s ease';
                            char.style.color = isActive ? '#000' : 'rgba(0,0,0,0.3)';
                            
                            const swash = char.querySelector('.swash');
                            if (swash) {
                                swash.style.transition = 'none';
                                swash.style.fontFamily = "inherit";
                                swash.style.fontSize = "inherit";
                                swash.style.marginRight = "0em";
                                swash.style.marginLeft = "0em";
                                swash.style.lineHeight = "inherit";
                            }
                        }, i * 10);
                        hoverTimeouts.push(timeout);
                    });
                });

                // Click Interaction
                title.addEventListener('click', () => {
                    if(title.classList.contains('active')) return;
                    
                    // Remove active from all
                    document.querySelectorAll('.work-title').forEach(t => t.classList.remove('active'));
                    // Add active
                    title.classList.add('active');
                    
                    // Change background with slight zoom
                    const newBgSrc = title.getAttribute('data-bg');
                    
                    if(currentBgAnim) currentBgAnim.kill();
                    
                    // Fade out old bg slightly, swap src, fade in and zoom
                    gsap.to(bgImg, {opacity: 0, duration: 0.3, onComplete: () => {
                        bgImg.src = newBgSrc;
                        
                        // Reset scale and animate to zoom slightly
                        gsap.set(bgImg, {scale: 1, opacity: 0});
                        currentBgAnim = gsap.timeline()
                            .to(bgImg, {opacity: 1, duration: 0.8, ease: "power2.out"})
                            .to(bgImg, {scale: 1.05, duration: 6, ease: "sine.out"}, "<");
                    }});
                    
                    // Text animation: stagger letters
                    gsap.fromTo(chars, 
                        { opacity: 0, y: 15 },
                        { opacity: 1, y: 0, duration: 0.6, ease: "back.out(1.5)", stagger: 0.03, overwrite: "auto" }
                    );
                });
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

        const newsBtnSvg = newsBtn.querySelector('svg');
        gsap.set(newsBtnSvg, { transformOrigin: "50% 10%" });
        
        const ringBellAnim = () => {
            if (gsap.isTweening(newsBtnSvg)) return;
            gsap.fromTo(newsBtnSvg, 
                { rotation: 25 }, 
                { rotation: 0, duration: 1.5, ease: "elastic.out(1.5, 0.2)", clearProps: "rotation" }
            );
        };
        
        newsBtn.addEventListener('mouseenter', ringBellAnim);

        newsBtn.addEventListener('click', () => {
            ringBellAnim();
            newsSidebar.classList.add('open');
            document.body.classList.add('news-active');
        });

        newsClose.addEventListener('click', () => {
            newsSidebar.classList.remove('open');
            document.body.classList.remove('news-active');
        });
        
        // Work List Interaction
        const titles = document.querySelectorAll('.work-title');
        const bgImg = document.getElementById('work-bg');
        let currentBgAnim;

        // Split text into spans for animation while preserving star-wrapper
        titles.forEach(title => {
            let newHtml = '';
            const childNodes = Array.from(title.childNodes);
            childNodes.forEach(node => {
                if (node.nodeType === 3) { // Text node
                    const chars = node.textContent.split('');
                    chars.forEach(char => {
                        if(char === ' ') {
                            newHtml += '&nbsp;';
                        } else {
                            newHtml += `<span class="char">${char}</span>`;
                        }
                    });
                } else {
                    newHtml += `<span class="char" style="display:inline-block">${node.outerHTML}</span>`;
                }
            });
            title.innerHTML = newHtml;
            
            // Interaction
            title.addEventListener('click', () => {
                if(title.classList.contains('active')) return;
                
                // Remove active from all
                titles.forEach(t => t.classList.remove('active'));
                // Add active
                title.classList.add('active');
                
                // Change background with slight zoom
                const newBgSrc = title.getAttribute('data-bg');
                
                if(currentBgAnim) currentBgAnim.kill();
                
                // Fade out old bg slightly, swap src, fade in and zoom
                gsap.to(bgImg, {opacity: 0, duration: 0.3, onComplete: () => {
                    bgImg.src = newBgSrc;
                    
                    // Reset scale and animate to zoom slightly
                    gsap.set(bgImg, {scale: 1, opacity: 0});
                    currentBgAnim = gsap.timeline()
                        .to(bgImg, {opacity: 1, duration: 0.8, ease: "power2.out"})
                        .to(bgImg, {scale: 1.05, duration: 6, ease: "sine.out"}, "<");
                }});
                
                // Text animation: stagger letters
                const chars = title.querySelectorAll('.char');
                gsap.fromTo(chars, 
                    { opacity: 0, y: 15 },
                    { opacity: 1, y: 0, duration: 0.6, ease: "back.out(1.5)", stagger: 0.03 }
                );
            });
        });
        
        // Initial setup for the first item
        const activeTitle = document.querySelector('.work-title.active');
        if(activeTitle) {
            bgImg.src = activeTitle.getAttribute('data-bg');
            gsap.set(bgImg, {scale: 1, opacity: 1});
            currentBgAnim = gsap.to(bgImg, {scale: 1.05, duration: 10, ease: "none"});
        }

        // Logo hide on scroll (Handles both Native Scroll and Auto-Scroll Transform)
        let logoHidden = false;
        function toggleLogo(hide) {
            if (hide !== logoHidden) {
                logoHidden = hide;
                gsap.to('.logo-text', {
                    y: hide ? -20 : 0,
                    opacity: hide ? 0 : 1,
                    duration: 0.3,
                    ease: "power2.inOut",
                    overwrite: "auto"
                });
            }
        }

        document.querySelector('.work-scroll-container').addEventListener('scroll', (e) => {
            if (e.target.scrollTop > 50) {
                toggleLogo(true);
            } else {
                toggleLogo(false);
            }
        });

        // Auto Scroll "Movie Credits" Logic (GPU Accelerated)
        const scrollContainer = document.querySelector('.work-scroll-container');
        const workList = document.querySelector('.work-list');
        let autoScrollActive = false;
        let inactivityTimer;
        let autoScrollTween;
        const scrollSpeedPixelsPerSecond = 40; // Cinematic speed

        function startAutoScroll() {
            if (autoScrollActive) return;
            autoScrollActive = true;
            
            // Calculate how far we can scroll
            const maxScroll = scrollContainer.scrollHeight - scrollContainer.clientHeight;
            const currentScroll = scrollContainer.scrollTop;
            const remainingScroll = maxScroll - currentScroll;
            
            if (remainingScroll <= 1) {
                autoScrollActive = false;
                return; // Already at bottom
            }
            
            // Calculate duration based on constant speed
            const duration = remainingScroll / scrollSpeedPixelsPerSecond;
            
            // Use GPU transform for buttery smooth sub-pixel animation
            autoScrollTween = gsap.to(workList, {
                y: -remainingScroll,
                duration: duration,
                ease: "none",
                onUpdate: () => {
                    if (Math.abs(gsap.getProperty(workList, "y")) + scrollContainer.scrollTop > 50) {
                        toggleLogo(true);
                    }
                },
                onComplete: () => {
                    syncScrollAndResetY();
                    autoScrollActive = false;
                }
            });
        }

        function syncScrollAndResetY() {
            if (!workList) return;
            const currentY = gsap.getProperty(workList, "y");
            if (currentY < 0) {
                // Instantly apply the fake visual scroll to the real physical scroll
                scrollContainer.scrollTop += Math.abs(currentY);
                // Reset fake visual scroll
                gsap.set(workList, { y: 0 });
            }
        }

        function stopAutoScroll() {
            if (!autoScrollActive) return;
            autoScrollActive = false;
            
            if (autoScrollTween) {
                autoScrollTween.kill();
            }
            // Hand over control back to the native browser scrollbar
            syncScrollAndResetY();
        }

        function resetInactivityTimer() {
            stopAutoScroll();
            clearTimeout(inactivityTimer);
            inactivityTimer = setTimeout(() => {
                startAutoScroll();
            }, 10000); // 10 seconds of inactivity
        }

        // Start scrolling immediately once the initial page animations finish
        setTimeout(() => {
            startAutoScroll();
        }, 3000); // Wait 3s for intro anims to fully finish

        // Listen for INTENTIONAL user activity to pause the scroll
        window.addEventListener('mousedown', resetInactivityTimer);
        window.addEventListener('keydown', resetInactivityTimer);
        window.addEventListener('touchstart', resetInactivityTimer, { passive: true });
        scrollContainer.addEventListener('wheel', resetInactivityTimer, { passive: true });
        scrollContainer.addEventListener('touchmove', resetInactivityTimer, { passive: true });
    });
