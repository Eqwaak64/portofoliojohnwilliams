import re
import sys

def update_menu_links(filepath, active_page):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The HTML for the menu links
    # <a href="index.html" class="menu-link active">Hom...</a>
    # <a href="work.html" class="menu-link">Work</a>
    # <a href="faq.html" class="menu-link">FAQ</a>
    
    # We will just replace all href="#" to appropriate links
    # But wait, index.html might still have href="#"
    
    # We can rebuild the menu completely for safety
    menu_regex = r'<nav class="menu-nav">.*?</nav>'
    
    # Determine active classes
    home_active = ' active' if active_page == 'home' else ''
    work_active = ' active' if active_page == 'work' else ''
    faq_active = ' active' if active_page == 'faq' else ''
    
    new_menu = f'''<nav class="menu-nav">
            <a href="index.html" class="menu-link{home_active}">Hom<span class="star-wrapper">e<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span></a>
            <a href="work.html" class="menu-link{work_active}">Work</a>
            <a href="#" class="menu-link">Biography</a>
            <a href="#" class="menu-link">Awards</a>
            <a href="faq.html" class="menu-link{faq_active}">FAQ</a>
        </nav>'''
        
    content = re.sub(menu_regex, new_menu, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def build_faq_html():
    with open('faq.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the main content and footer
    main_start = content.find('<main class="main-content">')
    footer_end = content.find('</footer>') + len('</footer>')
    
    # Remove intro screen
    intro_start = content.find('<!-- Intro Screen -->')
    if intro_start != -1:
        # Find the end of the intro screen div
        intro_end = content.find('</div>', content.find('</div>', content.find('</div>', intro_start)+1)+1) + len('</div>')
        content = content[:intro_start] + content[intro_end:]

    # Recalculate main_start because indices shifted
    main_start = content.find('<main class="main-content">')
    footer_end = content.find('</footer>') + len('</footer>')
    
    faq_html = """
    <main class="faq-main">
        <div class="faq-header-content">
            <h1 class="faq-title">F<span class="star-wrapper">a<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>Q</h1>
            <p class="faq-subtitle">Find your answers for the most asked questions</p>
        </div>
        
        <div class="faq-list">
            <div class="faq-item">
                <div class="faq-question">
                    <span>How do I send Alan fan-mail or request something to be autographed?</span>
                    <span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 5v14M5 12h14"></path></svg></span>
                </div>
                <div class="faq-answer">
                    <div class="faq-answer-inner">
                        <p>Due to the overwhelming amount of requests, Alan is unfortunately unable to personally autograph items sent to him by mail.</p>
                    </div>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>Where can I purchase or download the sheet music of Mr. Menken's songs?</span>
                    <span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 5v14M5 12h14"></path></svg></span>
                </div>
                <div class="faq-answer">
                    <div class="faq-answer-inner">
                        <p>Most of Alan's sheet music can be found online at authorized digital retailers such as Musicnotes or Hal Leonard.</p>
                    </div>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>May I record an Alan Menken song on my personal CD?</span>
                    <span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 5v14M5 12h14"></path></svg></span>
                </div>
                <div class="faq-answer">
                    <div class="faq-answer-inner">
                        <p>Yes, provided you secure the proper mechanical licensing rights through Harry Fox Agency or the respective publisher.</p>
                    </div>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>How can I learn about Mr. Menken's style and process of songwriting?</span>
                    <span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 5v14M5 12h14"></path></svg></span>
                </div>
                <div class="faq-answer">
                    <div class="faq-answer-inner">
                        <p>Alan frequently discusses his process in documentaries and interviews, many of which are available in our Documentary section.</p>
                    </div>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>Our theater company wants to do a show written by Mr. Menken. Where can I find information and resources on how to do that?</span>
                    <span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 5v14M5 12h14"></path></svg></span>
                </div>
                <div class="faq-answer">
                    <div class="faq-answer-inner">
                        <p>Theatrical licensing rights for Alan's musicals are handled by Music Theatre International (MTI). You can visit their website for details.</p>
                    </div>
                </div>
            </div>

            <div class="faq-item">
                <div class="faq-question">
                    <span>I've written a new play or piece of music and would love to share it with Mr. Menken. How can I do that?</span>
                    <span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 5v14M5 12h14"></path></svg></span>
                </div>
                <div class="faq-answer">
                    <div class="faq-answer-inner">
                        <p>For legal reasons, Alan and his team cannot accept or review unsolicited creative materials.</p>
                    </div>
                </div>
            </div>
            
            <div style="height: 10vh;"></div>
        </div>
    </main>
"""

    content = content[:main_start] + faq_html + content[footer_end:]
    
    # Update CSS
    style_end = content.find('</style>')
    faq_css = """
        /* FAQ Page CSS */
        body {
            overflow-y: auto; /* allow normal scrolling */
        }
        
        .faq-main {
            width: 100%;
            min-height: 100vh;
            padding-top: 15vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .faq-header-content {
            text-align: center;
            margin-bottom: 8vh;
        }

        .faq-title {
            font-family: 'Clearface', serif;
            font-size: 6rem;
            font-weight: 400;
            color: #1a1a1a;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }

        .faq-subtitle {
            font-family: 'Clearface', serif;
            font-size: 1.15rem;
            font-weight: 600;
            color: rgba(26, 26, 26, 0.6);
            letter-spacing: 0.02em;
        }

        .faq-list {
            width: 100%;
            max-width: 900px;
            padding: 0 2rem;
            display: flex;
            flex-direction: column;
        }

        .faq-item {
            border-bottom: 1px solid rgba(0,0,0,0.06);
            overflow: hidden;
        }

        .faq-item:first-child {
            border-top: 1px solid rgba(0,0,0,0.06);
        }

        .faq-question {
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 2.2rem 0;
            cursor: pointer;
            font-family: 'Clearface', serif;
            font-size: 1.4rem;
            font-weight: 700;
            color: #1a1a1a;
            transition: color 0.3s;
        }

        .faq-question:hover {
            color: #000;
        }
        
        .faq-question span:first-child {
            padding-right: 2rem;
            line-height: 1.4;
        }

        .faq-icon {
            width: 24px;
            height: 24px;
            flex-shrink: 0;
            transition: transform 0.4s cubic-bezier(0.77, 0, 0.175, 1);
        }

        .faq-item.active .faq-icon {
            transform: rotate(45deg); /* Turns + into x */
        }

        .faq-answer {
            height: 0;
            opacity: 0;
            font-family: 'Clearface', serif;
            font-size: 1.15rem;
            line-height: 1.5;
            color: rgba(26, 26, 26, 0.7);
        }
        
        .faq-answer-inner {
            padding-bottom: 2.2rem;
        }
"""
    content = content[:style_end] + faq_css + content[style_end:]

    # Ensure header is light theme (black icons) in FAQ
    # We will remove mix-blend-mode for faq because bg is solid color EBE8E0
    # Actually, mix-blend-mode: difference works fine on EBE8E0 (makes it dark grey).
    # But let's be safe and override for .faq-main's page.
    # Wait, the screenshot has black icons. mix-blend-mode: difference against #EBE8E0 makes it `#14171f`, which is a very dark grey/black. So it's perfect.
    
    # Replace Script block
    script_start = content.find('<script>')
    script_end = content.find('</script>', script_start) + len('</script>')
    
    faq_script = """<script>
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
        
        // Entrance animation
        gsap.from(".faq-header-content", { y: 30, opacity: 0, duration: 1, ease: "power3.out", delay: 0.2 });
        gsap.from(".faq-item", { y: 20, opacity: 0, duration: 0.8, ease: "power2.out", stagger: 0.1, delay: 0.4 });
    });
    </script>"""
    
    content = content[:script_start] + faq_script + content[script_end:]
    
    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_menu_links('index.html', 'home')
    update_menu_links('work.html', 'work')
    build_faq_html()
    update_menu_links('faq.html', 'faq')
