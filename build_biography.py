import re

def build_biography():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    bio_css = """
        /* Biography Specific Styles */
        html:has(body.bio-page),
        body.bio-page {
            overflow: auto !important;
            height: auto !important;
            min-height: 100vh;
        }
        
        /* Navbar static when scrolled */
        .bio-page .header {
            position: absolute;
        }
        
        .bio-main {
            display: flex;
            flex-direction: column;
            width: 100%;
            padding-top: 15vh;
        }

        /* Hero Section */
        .bio-hero {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            width: 100%;
            position: relative;
            padding-bottom: 2rem;
            min-height: 85vh;
        }

        .bio-title {
            font-family: 'Clearface', serif;
            font-size: 8rem;
            font-weight: 400;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
            position: relative;
            z-index: 2;
        }

        .bio-subtitle {
            font-family: 'Clearface', serif;
            font-size: 1.2rem;
            color: #555;
            font-weight: 500;
            z-index: 2;
        }

        .bio-o-star, .bio-e-star, .bio-a-star {
            position: relative;
            display: inline-block;
        }

        .bio-o-star svg, .bio-e-star svg, .bio-a-star svg {
            position: absolute;
            top: 20%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 0.4em;
            height: 0.4em;
            fill: none;
            stroke: currentColor;
            stroke-width: 1.5;
        }
        
        .bio-hero-scene {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100vw;
            height: 60vh;
            pointer-events: none;
            z-index: 1;
        }

        .hero-alan {
            position: absolute;
            bottom: -2vw;
            left: 2vw;
            width: 38vw;
            min-width: 380px;
            object-fit: contain;
            mix-blend-mode: multiply;
            z-index: 2;
        }

        .hero-piano {
            position: absolute;
            bottom: 0;
            left: 8vw;
            width: 85vw;
            min-width: 800px;
            object-fit: contain;
            z-index: 1;
        }

        .hero-notes {
            position: absolute;
            bottom: 14vw;
            left: 36vw;
            width: 15vw;
            min-width: 150px;
            object-fit: contain;
            z-index: 3;
            transform: rotate(26deg);
        }

        /* Content Layout */
        .bio-content-wrapper {
            display: flex;
            width: 100%;
            max-width: 1800px;
            margin: 0 auto;
            padding: 4rem 4rem;
            position: relative;
            z-index: 5;
            background-color: transparent;
        }

        /* Tapering black separator at bottom of hero */
        .bio-separator {
            width: 100%;
            height: 150px;
            background-color: #000;
            clip-path: polygon(0 100%, 100% 100%, 80% 0, 20% 0);
            margin-top: -100px;
            z-index: 2;
            position: relative;
        }
        
        /* Just completely hiding the background under the sidebar and main section since the hero img spans the left side */
        .bio-content-wrapper::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to bottom, transparent, var(--bg-color) 150px);
            z-index: -1;
        }

        /* Sidebar Navigation */
        .bio-sidebar {
            width: 280px;
            flex-shrink: 0;
            position: sticky;
            top: 150px;
            align-self: flex-start;
            padding-right: 2rem;
            margin-top: 4rem;
        }

        .bio-timeline {
            display: flex;
            flex-direction: column;
            gap: 2.5rem;
        }

        .timeline-link {
            font-family: 'Graphik', sans-serif;
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: #888;
            text-decoration: none;
            line-height: 1.6;
            font-weight: 700;
            transition: color 0.3s;
        }

        .timeline-link:hover, .timeline-link.active {
            color: #1a1a1a;
        }

        /* Main Content Area */
        .bio-sections {
            flex: 1;
            padding-left: 6rem;
            padding-bottom: 15rem; /* space for footer */
            margin-top: 4rem;
        }

        .bio-section {
            margin-bottom: 8rem;
        }

        .section-label {
            font-family: 'Graphik', sans-serif;
            font-size: 0.85rem;
            color: #666;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 1.5rem;
        }

        .section-date {
            font-family: 'Graphik', sans-serif;
            font-size: 0.85rem;
            color: #666;
            letter-spacing: 0.15em;
            margin-bottom: 1.5rem;
        }

        .section-title {
            font-family: 'Clearface', serif;
            font-size: 6.5rem;
            font-weight: 400;
            line-height: 1.1;
            margin-bottom: 2.5rem;
        }

        .bio-e-star svg { top: -10%; left: 80%; transform: translate(-50%, 0); }
        .bio-a-star svg { top: 10%; left: 100%; transform: translate(-50%, 0); }

        .section-text-large {
            font-family: 'Clearface', serif;
            font-size: 2.2rem;
            line-height: 1.4;
            font-weight: 500;
            margin-bottom: 3rem;
            max-width: 900px;
        }

        .section-text-small {
            font-family: 'Clearface', serif;
            font-size: 1.25rem;
            line-height: 1.6;
            max-width: 750px;
            color: #111;
        }

        /* Section Layouts */
        .section-header-split {
            display: flex;
            gap: 4rem;
            margin-bottom: 6rem;
            align-items: flex-start;
        }

        .header-left {
            flex: 1;
            max-width: 400px;
        }
        
        .section-subtitle {
            font-family: 'Clearface', serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
        }

        .section-desc {
            font-family: 'Clearface', serif;
            font-size: 1.1rem;
            line-height: 1.6;
        }

        .header-right {
            flex: 2;
        }

        .video-container {
            position: relative;
            width: 100%;
            background: #000;
            overflow: hidden;
            cursor: pointer;
        }

        .video-container img {
            width: 100%;
            display: block;
            opacity: 0.8;
            transition: opacity 0.3s;
        }

        .video-container:hover img {
            opacity: 1;
        }

        .play-overlay {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 60px;
            height: 60px;
            border-radius: 50%;
            border: 1px solid #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #fff;
            transition: transform 0.3s;
        }

        .video-container:hover .play-overlay {
            transform: translate(-50%, -50%) scale(1.1);
            background: rgba(255,255,255,0.1);
        }

        .play-overlay svg {
            width: 20px;
            height: 20px;
            margin-left: 4px;
        }

        .content-split {
            display: flex;
            gap: 4rem;
            margin-bottom: 4rem;
            align-items: flex-start;
        }

        .split-left {
            flex: 1;
            max-width: 400px;
        }

        .section-date-small {
            font-family: 'Graphik', sans-serif;
            font-size: 0.75rem;
            color: #666;
            letter-spacing: 0.15em;
            margin-bottom: 1rem;
        }

        .split-right {
            flex: 1.5;
            display: flex;
            justify-content: center;
            background-color: transparent;
            padding: 2rem;
            mix-blend-mode: multiply;
        }

        .split-right img {
            width: 100%;
            height: auto;
            object-fit: contain;
        }

        .section-divider {
            border: none;
            border-top: 1px solid #ccc;
            margin: 4rem 0;
            width: 100%;
            max-width: 400px;
        }
        
        .bio-page .footer {
            position: relative;
            background-color: var(--bg-color);
        }
    """

    bio_html = """
    <main class="bio-main">
        <div class="bio-hero">
            <h1 class="bio-title">Bi<span class="bio-o-star">o<svg viewBox="0 0 24 24"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg></span>graphy</h1>
            <p class="bio-subtitle">Alan's life from the start till present</p>
            <div class="bio-hero-scene">
                <img src="assets/piano.png" class="hero-piano" alt="Piano">
                <img src="assets/alan.png" class="hero-alan" alt="Alan">
                <img src="assets/notes.png" class="hero-notes" alt="Notes">
            </div>
        </div>
        
        <div class="bio-separator"></div>
        
        <div class="bio-content-wrapper">
            <aside class="bio-sidebar">
                <nav class="bio-timeline">
                    <a href="#summary" class="timeline-link active">ALAN MENKEN<br>SUMMARY</a>
                    <a href="#early-years" class="timeline-link">EARLY YEARS<br>1949 &mdash; 1966</a>
                    <a href="#college-years" class="timeline-link">COLLEGE YEARS<br>1967 &mdash; 1971</a>
                    <a href="#early-career" class="timeline-link">EARLY CAREER<br>1972 &mdash; 1980</a>
                    <a href="#little-shop" class="timeline-link">LITTLE SHOP AND OFF-<br>BROADWAY<br>1982 &mdash; 1987</a>
                    <a href="#disney" class="timeline-link">DISNEY ANIMATION YEARS<br>1988 &mdash; 1997</a>
                    <a href="#millennium" class="timeline-link">A NEW MILLENNIUM<br>1998 &mdash; 2007</a>
                    <a href="#screen-to-stage" class="timeline-link">FROM SCREEN TO STAGE<br>2008 &mdash; 2015</a>
                </nav>
            </aside>
            
            <div class="bio-sections">
                <!-- Summary Section -->
                <section id="summary" class="bio-section">
                    <p class="section-label">Summary</p>
                    <h2 class="section-title">Alan Menk<span class="bio-e-star">e<svg viewBox="0 0 24 24"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg></span>n</h2>
                    <div class="section-text-large">
                        Legendary composer Alan Menken has created some of the most beloved songs and musical scores of our time, with his unique voice as a composer capturing the imagination of audiences for over 35 years.
                    </div>
                    <div class="section-text-small">
                        <p>Known for his music on stage and screen, he is noted for his multiple works with the Walt Disney company (The Little Mermaid, Beauty and the Beast, Aladdin), as well as Broadway stage musicals Sister Act and Little Shop of Horrors. With eight Academy Awards, Alan has received more Oscars than any living person, and is the recipient of numerous other awards including Golden Globes, Grammys, Drama Desk Awards, and a Tony Award.</p>
                    </div>
                </section>
                
                <!-- Early Years Section -->
                <section id="early-years" class="bio-section">
                    <div class="section-header-split">
                        <div class="header-left">
                            <p class="section-label">This is</p>
                            <h3 class="section-subtitle">Alan Menken</h3>
                            <p class="section-desc">Learn about his life from the early years all the way through till today. You can explore photos, videos and sound clips.</p>
                        </div>
                        <div class="header-right">
                            <div class="video-container">
                                <img src="assets/bio_alan_video_thumb.png" alt="Alan playing piano" style="width:100%">
                                <div class="play-overlay"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="currentColor"/></svg></div>
                            </div>
                        </div>
                    </div>
                    
                    <p class="section-date">1949 &mdash; 1966</p>
                    <h2 class="section-title">E<span class="bio-a-star">a<svg viewBox="0 0 24 24"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg></span>rly Years</h2>
                    <div class="section-text-small">
                        <p>Alan Menken was born July 22nd, 1949 at French Hospital in New York City, to young aspiring actress/playwright, Judy Menken and young aspiring dentist, Norman Menken. According to family lore, he was originally named “Gus” until it was discovered that no name beginning with “G” was available and his name was quickly changed to Alan.</p>
                    </div>
                </section>
                
                <!-- College Years Section -->
                <section id="college-years" class="bio-section">
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">September 1967</p>
                            <h3 class="section-subtitle">Welcome NYU</h3>
                            <p class="section-text-small">Alan drifted from Pre-Med to Anthropology to Philosophy to finally graduating with a degree in Musicology (despite the family's Dental legacy).</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <img src="assets/bio_nyu_logo.png" alt="NYU Logo" style="max-width:350px;">
                        </div>
                    </div>
                    <hr class="section-divider">
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">December 1968</p>
                            <h3 class="section-subtitle">Alan Writes His First Musical</h3>
                            <p class="section-text-small">His first full musical, "Separate Ways", for which Alan wrote both music and lyrics, was produced at NYU. A fellow student, Elyce Wakerman, wrote the book; a rock musical about hippies living in an apartment building with more conservative residents. It was moderately successful.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <img src="assets/bio_separate_ways.png" alt="Separate Ways" style="width:100%;">
                        </div>
                    </div>
                </section>
            </div>
        </div>
    </main>
    """

    content = re.sub(r'<body[^>]*>', '<body class="bio-page">', content)
    
    # Safely replace overflow: hidden; ONLY for body, html block
    content = re.sub(r'(body,\s*html\s*\{[^}]*)overflow:\s*hidden;', r'\1overflow: auto !important;', content)

    # Recalculate positions after length changes
    main_start = content.find('<main class="main-content">')
    footer_start = content.find('<footer class="footer">')
    css_insert_point = content.find('</style>')
    
    new_content = content[:css_insert_point] + bio_css + content[css_insert_point:main_start] + bio_html + content[footer_start:]

    with open('biography.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    build_biography()
