import re

with open('work.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to replace the content of <main class="main-content"> ... </main>
# and <footer class="footer"> ... </footer>
# and the scripts related to gallery.

# Find the start of main
main_start = content.find('<main class="main-content">')
footer_end = content.find('</footer>') + len('</footer>')

# We can replace everything from main_start to footer_end
work_html = """
    <main class="work-main">
        <div class="work-bg-container">
            <img src="https://picsum.photos/seed/bg1/1920/1080" class="work-bg-img active" id="work-bg" alt="Background">
        </div>
        
        <div class="work-scroll-container">
            <div class="work-list">
                
                <!-- Category 1 -->
                <div class="work-category">
                    <span class="cat-title">ANIMATED FILM MUSICAL</span>
                    <div class="cat-divider">
                        <span class="cat-line"></span>
                        <svg class="cat-icon" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                        <span class="cat-line"></span>
                    </div>
                </div>
                
                <h2 class="work-title active" data-bg="https://picsum.photos/seed/bg1/1920/1080">The Lit<span class="star-wrapper">t<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>le Mermai<span class="star-wrapper">d<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span></h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg2/1920/1080">Beauty a<span class="star-wrapper">n<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>d t<span class="star-wrapper">h<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>e Bea<span class="star-wrapper">s<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>t</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg3/1920/1080">Aladdi<span class="star-wrapper">n<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span></h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg4/1920/1080">Pocahontas</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg5/1920/1080">The Hunchback of Notre Dame</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg6/1920/1080">Hercules</h2>

                <!-- Category 2 -->
                <div class="work-category">
                    <span class="cat-title">LIVE-ACTION FILM MUSICAL</span>
                    <div class="cat-divider">
                        <span class="cat-line"></span>
                        <svg class="cat-icon" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                        <span class="cat-line"></span>
                    </div>
                </div>

                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg7/1920/1080">Little Shop of H<span class="star-wrapper">o<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>rrors</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg8/1920/1080">New<span class="star-wrapper">s<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>ies</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg9/1920/1080">A Christmas C<span class="star-wrapper">a<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>rol</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg10/1920/1080">Enchant<span class="star-wrapper">e<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>d</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg11/1920/1080">Beauty and the Beast</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg12/1920/1080">Aladdin</h2>

                <!-- Category 3 -->
                <div class="work-category">
                    <span class="cat-title">MUSICAL ANIMATED TELEVISION SERIES</span>
                    <div class="cat-divider">
                        <span class="cat-line"></span>
                        <svg class="cat-icon" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                        <span class="cat-line"></span>
                    </div>
                </div>

                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg13/1920/1080">Tangl<span class="star-wrapper">e<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>d: The S<span class="star-wrapper">e<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>ries</h2>

                <!-- Category 4 -->
                <div class="work-category">
                    <span class="cat-title">MUSICAL TELEVISION SERIES</span>
                    <div class="cat-divider">
                        <span class="cat-line"></span>
                        <svg class="cat-icon" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                        <span class="cat-line"></span>
                    </div>
                </div>

                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg14/1920/1080">Galav<span class="star-wrapper">a<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>nt</h2>

                <!-- Category 5 -->
                <div class="work-category">
                    <span class="cat-title">STAGE</span>
                    <div class="cat-divider">
                        <span class="cat-line"></span>
                        <svg class="cat-icon" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                        <span class="cat-line"></span>
                    </div>
                </div>

                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg15/1920/1080">G<span class="star-wrapper">o<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>d Bless Y<span class="star-wrapper">o<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>u Mr. R<span class="star-wrapper">o<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>sewater</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg16/1920/1080">Little Shop of Horrors</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg17/1920/1080">Beauty and the Beast</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg18/1920/1080">A Christmas Carol</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg19/1920/1080">King David</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg20/1920/1080">The Little Mermaid</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg21/1920/1080">Sister Act</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg22/1920/1080">Newsies</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg23/1920/1080">Aladdin</h2>

                <!-- Category 6 -->
                <div class="work-category">
                    <span class="cat-title">DOCUMENTARY</span>
                    <div class="cat-divider">
                        <span class="cat-line"></span>
                        <svg class="cat-icon" viewBox="0 0 24 24"><path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/></svg>
                        <span class="cat-line"></span>
                    </div>
                </div>

                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg24/1920/1080">Ho<span class="star-wrapper">w<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>ard</h2>
                <h2 class="work-title" data-bg="https://picsum.photos/seed/bg25/1920/1080">Linc<span class="star-wrapper">o<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>ln</h2>
                
                <div style="height: 30vh;"></div>
            </div>
        </div>
    </main>
"""

new_content = content[:main_start] + work_html + content[footer_end:]

# Now let's remove the script logic that is specific to index.html (like intro-screen, gallery animation)
# We can find `// --- Intro Screen Logic ---` and `// --- Single View Dynamic Logic ---`
# Actually, since it's a new file, let's just replace the whole script block!

script_start = new_content.find('<script>')
script_end = new_content.find('</script>', script_start) + len('</script>')

new_script = """<script>
    document.addEventListener("DOMContentLoaded", () => {
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
    });
</script>"""

new_content = new_content[:script_start] + new_script + new_content[script_end:]

# Now we add the CSS for .work-main etc.
style_end = new_content.find('</style>')

work_css = """
        /* Work Page CSS */
        .work-main {
            position: relative;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            background-color: #EBE8E0;
        }

        .work-bg-container {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 1;
            overflow: hidden;
            opacity: 0.25; /* highly brightened, so the background is faded */
        }

        .work-bg-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: grayscale(100%);
        }

        .work-scroll-container {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 2;
            overflow-y: auto;
            scroll-behavior: smooth;
        }

        .work-scroll-container::-webkit-scrollbar {
            width: 6px;
        }
        .work-scroll-container::-webkit-scrollbar-thumb {
            background-color: rgba(0,0,0,0.3);
            border-radius: 4px;
        }

        .work-list {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 30vh;
            padding-bottom: 20vh;
        }

        .work-category {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 6rem;
            margin-bottom: 2rem;
        }

        .cat-title {
            font-family: 'Graphik', sans-serif;
            font-size: 0.8rem;
            letter-spacing: 0.25em;
            color: #000;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }

        .cat-divider {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .cat-line {
            width: 30px;
            height: 1px;
            background-color: #000;
        }

        .cat-icon {
            width: 12px;
            height: 12px;
            fill: #000;
        }

        .work-title {
            font-family: 'Clearface', serif;
            font-size: 4.5rem;
            font-weight: 400;
            color: rgba(0,0,0,0.3);
            margin: 0.5rem 0;
            cursor: pointer;
            transition: color 0.4s ease, opacity 0.4s ease;
            text-align: center;
        }

        .work-title:hover {
            color: rgba(0,0,0,0.6);
        }

        .work-title.active {
            color: #000;
        }

        .char {
            display: inline-block;
        }
"""

new_content = new_content[:style_end] + work_css + new_content[style_end:]

# Also remove intro-screen HTML
intro_start = new_content.find('<!-- Intro Screen -->')
intro_end = new_content.find('</div>', new_content.find('</div>', new_content.find('</div>', intro_start)+1)+1) + len('</div>')
if intro_start != -1:
    new_content = new_content[:intro_start] + new_content[intro_end:]

# Update the header link in work.html so Home points to index.html and Work is active
new_content = new_content.replace('<a href="#" class="menu-link active">Hom', '<a href="index.html" class="menu-link">Hom')
new_content = new_content.replace('<a href="#" class="menu-link">Work</a>', '<a href="work.html" class="menu-link active">Work</a>')

with open('work.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

