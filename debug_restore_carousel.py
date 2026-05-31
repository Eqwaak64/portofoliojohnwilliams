import re

with open('awards.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old = r'''.awards-summary-wrapper {
            display: flex;
            justify-content: center;
            width: 100%;
            max-width: 1800px;
            margin-bottom: 4rem;
            position: relative;
        }

        .awards-summary {
            display: flex;
            gap: 2rem;
            justify-content: center;
            flex-wrap: wrap;
            width: 100%;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.6s ease, transform 0.6s ease;
            transform: translateX(20px);
        }

        .awards-summary.active {
            opacity: 1;
            pointer-events: auto;
            transform: translateX(0);
        }'''

css_new = r'''.awards-summary-wrapper {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 3rem;
            width: 100%;
            max-width: 1400px;
            margin-bottom: 2rem;
            position: relative;
        }

        .nav-circle-btn {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            border: 1px solid rgba(26,26,26,0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            background: transparent;
            cursor: pointer;
            color: #1a1a1a;
            transition: all 0.3s ease;
            flex-shrink: 0;
        }

        .nav-circle-btn:hover {
            background: #1a1a1a;
            color: #EBE8E0;
        }

        .nav-circle-btn svg {
            width: 20px;
            height: 20px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2;
        }

        .awards-summary-carousel {
            position: relative;
            flex: 1;
            height: 320px;
            max-width: 1200px;
        }

        .awards-summary {
            display: flex;
            gap: 2rem;
            justify-content: space-between;
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.6s ease, transform 0.6s ease;
            transform: translateX(20px);
        }

        .awards-summary.page-2 {
            justify-content: center;
            gap: 4rem;
        }

        .awards-summary.active {
            opacity: 1;
            pointer-events: auto;
            transform: translateX(0);
        }

        .carousel-dots {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 8rem;
        }

        .dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: rgba(26,26,26,0.2);
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
        }

        .dot.active {
            background-color: #1a1a1a;
            transform: scale(1.3);
        }'''
content = content.replace(css_old, css_new)

# 2. Update HTML
html_old = r'''        <!-- Summary Icons -->
        <div class="awards-summary-wrapper">
            <div class="awards-summary active">
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/afi_awards_sketch.png" alt="AFI" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">AFI Award</div>
                        <div class="summary-count"><strong>1</strong> / 1</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/bafta_awards_sketch.png" alt="BAFTA" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">BAFTA Award</div>
                        <div class="summary-count"><strong>7</strong> / 16</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/bmi_awards_sketch.png" alt="BMI" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">BMI Award</div>
                        <div class="summary-count"><strong>4</strong> / 4</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/emmy_awards_sketch.png" alt="Emmy" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">Emmy Award</div>
                        <div class="summary-count"><strong>3</strong> / 6</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/golden_globes_reward.png" alt="Golden Globes" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">Golden Globes</div>
                        <div class="summary-count"><strong>4</strong> / 27</div>
                    </div>
            </div>
        </div>'''

html_new = r'''        <!-- Summary Icons Carousel -->
        <div class="awards-summary-wrapper">
            <button class="nav-circle-btn prev-btn">
                <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
            </button>
            <div class="awards-summary-carousel">
                <!-- Page 1 -->
                <div class="awards-summary page-1 active">
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/afi_awards_sketch.png" alt="AFI" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">AFI Award</div>
                        <div class="summary-count"><strong>1</strong> / 1</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/bafta_awards_sketch.png" alt="BAFTA" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">BAFTA Award</div>
                        <div class="summary-count"><strong>7</strong> / 16</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/bmi_awards_sketch.png" alt="BMI" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">BMI Award</div>
                        <div class="summary-count"><strong>4</strong> / 4</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/emmy_awards_sketch.png" alt="Emmy" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">Emmy Award</div>
                        <div class="summary-count"><strong>3</strong> / 6</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/golden_globes_reward.png" alt="Golden Globes" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">Golden Globes</div>
                        <div class="summary-count"><strong>4</strong> / 27</div>
                    </div>
                </div>
                <!-- Page 2 -->
                <div class="awards-summary page-2">
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/grammy_awards_sketch.png" alt="Grammy" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">Grammy Award</div>
                        <div class="summary-count"><strong>26</strong> / 76</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/national_board_awards_sketch.png" alt="National Board" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">National Board</div>
                        <div class="summary-count"><strong>2</strong> / 2</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/academy_awards_sketch.png" alt="Academy Award" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">Academy Award</div>
                        <div class="summary-count"><strong>5</strong> / 54</div>
                    </div>
                    <div class="summary-item">
                        <div class="summary-icon">
                            <svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg>
                            <img src="assets/saturn_awards_sketch.png" alt="Saturn" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'">
                        </div>
                        <div class="summary-label">WINS/NOMINEES</div>
                        <div class="summary-name">Saturn Award</div>
                        <div class="summary-count"><strong>9</strong> / 23</div>
                    </div>
                </div>
            </div>
            <button class="nav-circle-btn next-btn">
                <svg viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
            </button>
        </div>
        <div class="carousel-dots">
            <span class="dot active" data-page="1"></span>
            <span class="dot" data-page="2"></span>
        </div>'''
content = content.replace(html_old, html_new)

# 3. Update JS
js_old = r'''        // Ensure summary is visible initially
        gsap.set(".awards-summary", {opacity: 1, x: 0});'''
js_new = r'''        // Carousel Pagination
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');
        const dots = document.querySelectorAll('.dot');
        const summaryPages = document.querySelectorAll('.awards-summary');
        
        let currentCarouselPage = 1;

        function setCarouselPage(page) {
            currentCarouselPage = page;
            
            // Update dots
            dots.forEach((dot, idx) => {
                dot.classList.toggle('active', idx + 1 === page);
            });
            
            // Update summary pages
            summaryPages.forEach((summary, idx) => {
                if(idx + 1 === page) {
                    summary.classList.add('active');
                    gsap.fromTo(summary, {opacity: 0, x: 20}, {opacity: 1, x: 0, duration: 0.6, ease: "power2.out"});
                } else {
                    summary.classList.remove('active');
                    gsap.set(summary, {opacity: 0, x: -20});
                }
            });
        }
        
        if (prevBtn && nextBtn) {
            prevBtn.addEventListener('click', () => {
                setCarouselPage(currentCarouselPage === 1 ? 2 : 1);
            });
            nextBtn.addEventListener('click', () => {
                setCarouselPage(currentCarouselPage === 2 ? 1 : 2);
            });
        }
        
        dots.forEach(dot => {
            dot.addEventListener('click', (e) => {
                const page = parseInt(e.target.getAttribute('data-page'));
                setCarouselPage(page);
            });
        });'''
content = content.replace(js_old, js_new)

js_hide_old = r'''            .to([".header", ".awards-subtitle", ".awards-summary-wrapper", ".awards-table-container"], {
                opacity: 1, duration: 1.2, stagger: 0.1, ease: "power2.out"'''
js_hide_new = r'''            .to([".header", ".awards-subtitle", ".awards-summary-wrapper", ".carousel-dots", ".awards-table-container"], {
                opacity: 1, duration: 1.2, stagger: 0.1, ease: "power2.out"'''
content = content.replace(js_hide_old, js_hide_new)

js_hide2_old = r'''        const hideElements = [".header", ".awards-subtitle", ".awards-summary-wrapper", ".awards-table-container"];'''
js_hide2_new = r'''        const hideElements = [".header", ".awards-subtitle", ".awards-summary-wrapper", ".carousel-dots", ".awards-table-container"];'''
content = content.replace(js_hide2_old, js_hide2_new)


with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
