
        document.addEventListener("DOMContentLoaded", () => {
        // Page Intro Transition
        const pageTl = gsap.timeline();
        const hideElements = [".header", ".bio-subtitle", ".bio-hero-scene", ".bio-separator", ".bio-content-wrapper"];
        const titleEl = document.querySelector(".bio-title");
        
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
            gsap.set(titleEl, { y: "25vh", perspective: 800 });
            
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
    
            const tl = gsap.timeline({ defaults: { ease: "power3.out" }, paused: true });

            tl.from(".header", { y: -30, opacity: 0, duration: 1.2 }, "start")
                .from(".featured-text-wrapper", { y: 30, opacity: 0, duration: 1.2 }, "start+=0.6")
                .from(".footer", { y: 30, opacity: 0, duration: 1.2 }, "start+=0.8");

            // Custom Main Gallery Entrance Animation
            function animateMainGalleryEntrance(tlInstance) {
                const cols = document.querySelectorAll('.col');
                if (cols.length < 10) return;

                const centerCols = [cols[4], cols[5]];
                const pair1 = [cols[3], cols[6]]; // Innermost (sebelah persis kotak tengah)
                const pair2 = [cols[2], cols[7]];
                const pair3 = [cols[1], cols[8]];
                const pair4 = [cols[0], cols[9]]; // Outermost (paling ujung)

                gsap.set(cols, { opacity: 0, x: 0, y: 0, scale: 1 });

                const galleryTl = gsap.timeline();

                // 1. Center timbul (muncul dari bawah)
                galleryTl.fromTo(centerCols,
                    { opacity: 0, y: 60, scale: 0.95 },
                    { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "power4.out", clearProps: "all" }
                );

                // 2. Melesat dari ujung secara berpasangan
                galleryTl.add("pairs", 0.5); // Delay 0.5 detik setelah center mulai

                galleryTl.fromTo(pair1[0], { opacity: 0, x: "-50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs");
                galleryTl.fromTo(pair1[1], { opacity: 0, x: "50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs");

                galleryTl.fromTo(pair2[0], { opacity: 0, x: "-50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs+=0.3");
                galleryTl.fromTo(pair2[1], { opacity: 0, x: "50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs+=0.3");

                galleryTl.fromTo(pair3[0], { opacity: 0, x: "-50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs+=0.6");
                galleryTl.fromTo(pair3[1], { opacity: 0, x: "50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs+=0.6");

                galleryTl.fromTo(pair4[0], { opacity: 0, x: "-50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs+=0.9");
                galleryTl.fromTo(pair4[1], { opacity: 0, x: "50vw" }, { opacity: 1, x: 0, duration: 1, ease: "power3.out", clearProps: "all" }, "pairs+=0.9");

                if (tlInstance) {
                    tlInstance.add(galleryTl, "start+=0.2");
                }
            }

            // Attach gallery entrance to paused timeline
            animateMainGalleryEntrance(tl);

            //// Intro entrance animations (fade in the elements of the intro screen)
            gsap.from(".intro-sound", { opacity: 0, y: -20, duration: 1.5, ease: "power2.out", delay: 0.5 });
            gsap.from(".intro-signature", { opacity: 0, scale: 0.9, duration: 2, ease: "power3.out", delay: 1 });
            gsap.from(".intro-desc", { opacity: 0, y: 20, duration: 1.5, ease: "power2.out", delay: 1.5 });
            gsap.from(".intro-enter", { opacity: 0, y: 20, duration: 1.5, ease: "power2.out", delay: 2 });

            // --- Single View Dynamic Logic ---
            const projectsData = [
                { title: "Pocahontas", song: "Just Around the Riverbend", signature: "H", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4", imgSrc: "https://picsum.photos/seed/menken1/600/1000", layout: 1 },
                { title: "Tangled", song: "When Will My Life Begin?", signature: "T", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4", imgSrc: "https://picsum.photos/seed/menken2/600/1000", layout: 2 },
                { title: "Aladdin", song: "A Whole New World", signature: "A", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4", imgSrc: "https://picsum.photos/seed/menken3/600/1000", layout: 3 },
                { title: "The Little Mermaid", displayTitle: "Little<br>Mermaid", navTitle: "The Little<br>Mermaid", song: "Part of Your World", signature: "L", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", imgSrc: "https://picsum.photos/seed/menken4/600/1000", layout: 4 },
                { title: "Beauty and the Beast", displayTitle: "Beauty<br>and the Beast", navTitle: "Beauty &<br>the Beast", song: "Be Our Guest", signature: "B", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4", imgSrc: "https://picsum.photos/seed/menken5/600/1000", layout: 5 },
                { title: "Hercules", song: "Go the Distance", signature: "H", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4", imgSrc: "https://picsum.photos/seed/menken6/600/1000", layout: 1 },
                { title: "Enchanted", song: "That's How You Know", signature: "E", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4", imgSrc: "https://picsum.photos/seed/menken7/600/1000", layout: 2 },
                { title: "Newsies", song: "Seize the Day", signature: "N", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4", imgSrc: "https://picsum.photos/seed/menken8/600/1000", layout: 3 },
                { title: "Little Shop of Horrors", displayTitle: "Little Shop<br>of Horrors", navTitle: "Little Shop<br>of Horrors", song: "Suddenly Seymour", signature: "L", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4", imgSrc: "https://picsum.photos/seed/menken9/600/1000", layout: 4 },
                { title: "Sister Act", displayTitle: "Sister<br>Act", navTitle: "Sister<br>Act", song: "I Will Follow Him", signature: "S", videoSrc: "https://storage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4", imgSrc: "https://picsum.photos/seed/menken10/600/1000", layout: 5 }
            ];

            const layouts = {
                1: [
                    { type: 'image', l: '0vw', t: '10vh', h: '50vh', w: '7vw' },
                    { type: 'title', l: '8vw', t: '7vh', h: '56vh', w: '7.5vw' },
                    { type: 'image', l: '16.5vw', t: '4vh', h: '62vh', w: '7vw' },
                    { type: 'image', l: '24.5vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'image', l: '32.5vw', t: '3vh', h: '64vh', w: '7vw' },
                    { type: 'image', l: '40.5vw', t: '2vh', h: '66vh', w: '7vw' },
                    { type: 'song', l: '46.6vw', t: '-1vh', h: '46vh', w: '2.8vw' },
                    { type: 'image', l: '48.5vw', t: '4vh', h: '62vh', w: '7vw' }
                ],
                2: [
                    { type: 'image', l: '0vw', t: '4vh', h: '62vh', w: '7vw' },
                    { type: 'song', l: '6.1vw', t: '-1vh', h: '46vh', w: '2.8vw' },
                    { type: 'image', l: '8vw', t: '2vh', h: '66vh', w: '7vw' },
                    { type: 'image', l: '16vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'image', l: '24vw', t: '3vh', h: '64vh', w: '7vw' },
                    { type: 'image', l: '32vw', t: '6vh', h: '56vh', w: '7vw' },
                    { type: 'title', l: '40vw', t: '7vh', h: '56vh', w: '7.5vw' },
                    { type: 'image', l: '48.5vw', t: '10vh', h: '50vh', w: '7vw' }
                ],
                3: [
                    { type: 'image', l: '0vw', t: '8vh', h: '54vh', w: '7vw' },
                    { type: 'image', l: '8vw', t: '4vh', h: '62vh', w: '7vw' },
                    { type: 'song', l: '14.1vw', t: '1vh', h: '46vh', w: '2.8vw' },
                    { type: 'image', l: '16vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'title', l: '24vw', t: '5vh', h: '60vh', w: '7.5vw' },
                    { type: 'image', l: '32.5vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'image', l: '40.5vw', t: '4vh', h: '62vh', w: '7vw' },
                    { type: 'image', l: '48.5vw', t: '8vh', h: '54vh', w: '7vw' }
                ],
                4: [
                    { type: 'title', l: '0vw', t: '8vh', h: '54vh', w: '7.5vw' },
                    { type: 'image', l: '8.5vw', t: '4vh', h: '62vh', w: '7vw' },
                    { type: 'image', l: '16.5vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'image', l: '24.5vw', t: '4vh', h: '62vh', w: '7vw' },
                    { type: 'image', l: '32.5vw', t: '2vh', h: '66vh', w: '7vw' },
                    { type: 'image', l: '40.5vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'song', l: '46.6vw', t: '2vh', h: '46vh', w: '2.8vw' },
                    { type: 'image', l: '48.5vw', t: '4vh', h: '62vh', w: '7vw' }
                ],
                5: [
                    { type: 'image', l: '0vw', t: '6vh', h: '58vh', w: '7vw' },
                    { type: 'song', l: '6.1vw', t: '0vh', h: '46vh', w: '2.8vw' },
                    { type: 'image', l: '8vw', t: '2vh', h: '66vh', w: '7vw' },
                    { type: 'image', l: '16vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'image', l: '24vw', t: '4vh', h: '62vh', w: '7vw' },
                    { type: 'image', l: '32vw', t: '0vh', h: '70vh', w: '7vw' },
                    { type: 'image', l: '40vw', t: '5vh', h: '60vh', w: '7vw' },
                    { type: 'title', l: '48vw', t: '10vh', h: '50vh', w: '7.5vw' }
                ]
            };

            let currentProjectIdx = 0;
            const singleGallery = document.querySelector('.single-gallery');
            const leftNavText = document.querySelector('.left-nav .nav-text');
            const rightNavText = document.querySelector('.right-nav .nav-text');

            function renderSingleView(idx) {
                const data = projectsData[idx];
                const layout = layouts[data.layout];
                let html = '';
                layout.forEach(slice => {
                    if (slice.type === 'image') {
                        html += `
                            <div class="single-slice" style="--l: ${slice.l}; --t: ${slice.t}; --h: ${slice.h}; --w: ${slice.w};">
                                <img class="single-slice-img" src="${data.imgSrc}" alt="">
                                <video class="single-slice-media" src="${data.videoSrc}" autoplay loop muted playsinline></video>
                            </div>
                        `;
                    } else if (slice.type === 'title') {
                        html += `
                            <div class="single-slice title-box" style="--l: ${slice.l}; --t: ${slice.t}; --h: ${slice.h}; --w: ${slice.w};">
                                <div class="vertical-title-container">
                                    <span class="vertical-title">${data.displayTitle || data.title}</span>
                                    <span class="title-signature">${data.signature}</span>
                                </div>
                                <div class="explore-text">Explore Song &<br>Extra Material</div>
                            </div>
                        `;
                    } else if (slice.type === 'song') {
                        html += `
                            <div class="single-slice dark-box" style="--l: ${slice.l}; --t: ${slice.t}; --h: ${slice.h}; --w: ${slice.w};">
                                <div class="riverbend-text-container">
                                    <span class="riverbend-text">${data.song}</span>
                                </div>
                                <div class="play-circle">
                                    <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                                </div>
                            </div>
                        `;
                    }
                });
                singleGallery.innerHTML = html;

                const prevData = projectsData[(idx - 1 + projectsData.length) % projectsData.length];
                const nextData = projectsData[(idx + 1) % projectsData.length];

                leftNavText.innerHTML = prevData.navTitle || prevData.title;
                rightNavText.innerHTML = nextData.navTitle || nextData.title;
            }

            // Dynamic Text Swap on Hover
            const cols = document.querySelectorAll('.col');
            const featuredText = document.querySelector('.featured-text');
            if (featuredText) {
                const originalContent = featuredText.innerHTML;
                let textAnim;

                cols.forEach(col => {
                    col.addEventListener('mouseenter', () => {
                        const title = col.dataset.title;
                        const subtitle = col.dataset.subtitle;
                        const desc = col.dataset.desc;

                        if (textAnim) textAnim.kill();

                        let newHTML = '';
                        if (subtitle) newHTML += `<p class="subtitle">${subtitle}</p>`;
                        newHTML += `<h2>${title}</h2>`;
                        if (desc) newHTML += `<p class="desc">${desc}</p>`;

                        textAnim = gsap.timeline()
                            .to(featuredText, { opacity: 0, y: 10, duration: 0.2, ease: "power2.in" })
                            .call(() => {
                                featuredText.innerHTML = newHTML;
                            })
                            .fromTo(featuredText, { opacity: 0, y: -10 }, { opacity: 1, y: 0, duration: 0.3, ease: "power2.out" });
                    });

                    col.addEventListener('mouseleave', () => {
                        if (textAnim) textAnim.kill();

                        textAnim = gsap.timeline()
                            .to(featuredText, { opacity: 0, y: 10, duration: 0.2, ease: "power2.in" })
                            .call(() => {
                                featuredText.innerHTML = originalContent;
                            })
                            .fromTo(featuredText, { opacity: 0, y: -10 }, { opacity: 1, y: 0, duration: 0.3, ease: "power2.out" });
                    });
                });
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

            // GSAP Text Hover Animations for Menu Links
            const menuLinks = document.querySelectorAll('.menu-link:not(.active)');

            menuLinks.forEach((link, index) => {
                const text = link.innerText;
                link.innerHTML = '';

                // Wrapper inside the link to isolate GSAP transforms from CSS entrance animations
                const wrapper = document.createElement('div');
                wrapper.style.perspective = "500px";
                wrapper.style.display = "inline-block";

                text.split('').forEach(char => {
                    const span = document.createElement('span');
                    span.innerText = char;
                    span.style.display = 'inline-block';
                    span.style.transformOrigin = '50% 50%';
                    wrapper.appendChild(span);
                });

                link.appendChild(wrapper);
                const chars = wrapper.querySelectorAll('span');

                link.addEventListener('mouseenter', () => {
                    gsap.killTweensOf(chars);

                    if (index === 0) {
                        // Work: "Skew & Slide"
                        gsap.to(chars, { skewX: -20, x: 5, color: "#EBE8E0", stagger: 0.04, duration: 0.4, ease: "back.out(1.5)" });
                    } else if (index === 1) {
                        // Biography: "Wave Jump" (Bouncing wave)
                        gsap.to(chars, { y: -12, stagger: { each: 0.03, yoyo: true, repeat: 1 }, duration: 0.25, ease: "power1.inOut" });
                        gsap.to(chars, { color: "#EBE8E0", duration: 0.3 });
                    } else if (index === 2) {
                        // Awards: "3D Flip"
                        gsap.to(chars, { rotationX: 360, y: -5, color: "#EBE8E0", stagger: 0.04, duration: 0.6, ease: "back.out(1.7)" });
                    } else if (index === 3) {
                        // FAQ: "Elastic Pop"
                        gsap.to(chars, { scale: 1.35, color: "#EBE8E0", stagger: 0.05, duration: 0.7, ease: "elastic.out(1, 0.3)" });
                    }
                });

                link.addEventListener('mouseleave', () => {
                    gsap.killTweensOf(chars);

                    if (index === 0) {
                        gsap.to(chars, { skewX: 0, x: 0, color: "#555", stagger: 0.02, duration: 0.4, ease: "power2.out" });
                    } else if (index === 1) {
                        gsap.to(chars, { y: 0, color: "#555", stagger: 0.02, duration: 0.4, ease: "power2.out" });
                    } else if (index === 2) {
                        gsap.to(chars, { rotationX: 0, y: 0, color: "#555", stagger: 0.02, duration: 0.4, ease: "power2.out" });
                    } else if (index === 3) {
                        gsap.to(chars, { scale: 1, color: "#555", stagger: 0.02, duration: 0.4, ease: "power2.out" });
                    }
                });
            });

            // Active Link Hover (Home)
            const activeLink = document.querySelector('.menu-link.active');
            if (activeLink) {
                const activeHTML = activeLink.innerHTML;
                activeLink.innerHTML = '';

                const activeWrapper = document.createElement('div');
                activeWrapper.style.display = "inline-block";
                activeWrapper.style.transformOrigin = "center";
                activeWrapper.innerHTML = activeHTML;
                activeLink.appendChild(activeWrapper);

                activeLink.addEventListener('mouseenter', () => {
                    gsap.killTweensOf(activeWrapper);
                    gsap.to(activeWrapper, { scale: 1.08, rotation: -2, duration: 0.4, ease: "back.out(2)" });
                });
                activeLink.addEventListener('mouseleave', () => {
                    gsap.killTweensOf(activeWrapper);
                    gsap.to(activeWrapper, { scale: 1, rotation: 0, duration: 0.4, ease: "power2.out" });
                });
            }

            // View Transition Logic
            const playBtn = document.querySelector('.play-btn');
            const listBtn = document.querySelector('.list-btn');
            const viewGallery = document.querySelector('.view-gallery');
            const viewSingle = document.querySelector('.view-single');
            let isSingleView = false;
            window.isAnimatingSingle = false;

            // Initialize active state
            if (listBtn) {
                listBtn.classList.add('active');
            }

            // Custom Single View Entrance Animation
            function animateSingleEntrance(onComplete) {
                const slices = document.querySelectorAll('.single-slice');
                if (slices.length < 8) {
                    if (onComplete) onComplete();
                    return;
                }

                const centerSlices = [slices[3], slices[4]];
                const pair1 = [slices[2], slices[5]];
                const pair2 = [slices[1], slices[6]];
                const pair3 = [slices[0], slices[7]];

                const tl = gsap.timeline({ onComplete });

                // Reset positions to avoid flashes
                gsap.set(slices, { opacity: 0 });

                // 1. Center timbul
                tl.fromTo(centerSlices,
                    { opacity: 0, y: 50, scale: 0.95 },
                    { opacity: 1, y: 0, scale: 1, duration: 0.8, ease: "power4.out" }
                );

                // 2. Bergerak dari luar ke tengah berpasangan dengan delay
                const moveDist = 150;

                tl.add("pairs", "+=0.6"); // Delay 0.6s after center finishes

                tl.fromTo(pair1[0], { opacity: 0, x: moveDist }, { opacity: 1, x: 0, duration: 0.9, ease: "power3.out" }, "pairs");
                tl.fromTo(pair1[1], { opacity: 0, x: -moveDist }, { opacity: 1, x: 0, duration: 0.9, ease: "power3.out" }, "pairs");

                tl.fromTo(pair2[0], { opacity: 0, x: moveDist }, { opacity: 1, x: 0, duration: 0.9, ease: "power3.out" }, "pairs+=0.2");
                tl.fromTo(pair2[1], { opacity: 0, x: -moveDist }, { opacity: 1, x: 0, duration: 0.9, ease: "power3.out" }, "pairs+=0.2");

                tl.fromTo(pair3[0], { opacity: 0, x: moveDist }, { opacity: 1, x: 0, duration: 0.9, ease: "power3.out" }, "pairs+=0.4");
                tl.fromTo(pair3[1], { opacity: 0, x: -moveDist }, { opacity: 1, x: 0, duration: 0.9, ease: "power3.out" }, "pairs+=0.4");
            }

            if (playBtn && viewGallery && viewSingle) {
                playBtn.addEventListener('click', () => {
                    if (isSingleView) return;
                    isSingleView = true;

                    playBtn.classList.add('active');
                    listBtn.classList.remove('active');

                    const tlt = gsap.timeline({ defaults: { ease: "power3.inOut" } });

                    tlt.to(viewGallery, { opacity: 0, y: -20, duration: 0.6 })
                        .set(viewGallery, { display: "none" })
                        .set(viewSingle, { display: "flex" })
                        .call(() => {
                            renderSingleView(currentProjectIdx);
                            animateSingleEntrance();
                        })
                        .fromTo(".side-nav",
                            { y: 20, opacity: 0 },
                            { y: 0, opacity: 1, duration: 0.8, stagger: 0.1, ease: "power3.out" },
                            "+=1.5"
                        );
                });
            }

            if (listBtn && viewGallery && viewSingle) {
                listBtn.addEventListener('click', () => {
                    if (!isSingleView) return;
                    isSingleView = false;

                    listBtn.classList.add('active');
                    playBtn.classList.remove('active');

                    const tlt = gsap.timeline({ defaults: { ease: "power3.inOut" } });

                    tlt.to(".side-nav", { y: 20, opacity: 0, duration: 0.4 })
                        .to(".single-slice", { y: (i) => (i % 2 === 0 ? -100 : 100), opacity: 0, duration: 0.6, stagger: 0.05, ease: "power3.in" }, "-=0.2")
                        .set(viewSingle, { display: "none" })
                        .set(viewGallery, { display: "flex", opacity: 1 })
                        .call(() => {
                            animateMainGalleryEntrance();
                        });
                });
            }

            // Navigation Arrows Hover & Click
            const sideNavs = document.querySelectorAll('.side-nav');
            sideNavs.forEach(nav => {
                const arrow = nav.querySelector('.nav-arrow svg');
                const text = nav.querySelector('.nav-text');
                const isRight = nav.classList.contains('right-nav');

                nav.addEventListener('mouseenter', () => {
                    gsap.to(arrow, { scaleX: 1.5, x: isRight ? 10 : -10, duration: 0.4, ease: "back.out(2)" });
                    gsap.to(text, { y: -3, opacity: 0.7, duration: 0.3 });
                });
                nav.addEventListener('mouseleave', () => {
                    gsap.to(arrow, { scaleX: 1, x: 0, duration: 0.4, ease: "power2.out" });
                    gsap.to(text, { y: 0, opacity: 1, duration: 0.3 });
                });

                nav.addEventListener('click', () => {
                    if (window.isAnimatingSingle) return;
                    window.isAnimatingSingle = true;

                    gsap.to(".single-slice", {
                        y: (i) => (i % 2 === 0 ? -100 : 100),
                        opacity: 0,
                        duration: 0.6,
                        stagger: 0.05,
                        ease: "power3.in",
                        onComplete: () => {
                            if (isRight) {
                                currentProjectIdx = (currentProjectIdx + 1) % projectsData.length;
                            } else {
                                currentProjectIdx = (currentProjectIdx - 1 + projectsData.length) % projectsData.length;
                            }
                            renderSingleView(currentProjectIdx);

                            animateSingleEntrance(() => { window.isAnimatingSingle = false; });
                        }
                    });
                });
            });

        });
    