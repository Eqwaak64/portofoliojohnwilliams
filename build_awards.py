import re

def build_awards_page():
    with open('awards.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the main tag and replace it
    main_start = content.find('<main class="faq-main">')
    if main_start == -1:
        print("Could not find main tag")
        return
        
    footer_end = content.find('</footer>')
    if footer_end != -1:
        footer_end += len('</footer>')
    else:
        # if there's no footer, find the end of main
        main_end = content.find('</main>') + len('</main>')
        footer_end = main_end

    awards_html = """
    <main class="awards-main">
        <!-- Hero Slices -->
        <div class="awards-hero">
            <div class="hero-slice slice-1"><img src="assets/emmy_ph.jpg" alt="Emmy"></div>
            <div class="hero-slice slice-2"><img src="assets/globe_ph.jpg" alt="Golden Globe"></div>
            <div class="hero-slice slice-3"><img src="assets/grammy_ph.jpg" alt="Grammy"></div>
            <div class="hero-slice slice-4"><img src="assets/oscar_ph.jpg" alt="Oscar"></div>
            <div class="hero-slice slice-5"><img src="assets/tony_ph.jpg" alt="Tony"></div>
        </div>

        <!-- Title -->
        <div class="awards-title-sec">
            <h1 class="awards-title">Aw<span class="star-wrapper">a<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>rds</h1>
            <p class="awards-subtitle">See the full list of all the awards that Alan has won.</p>
        </div>

        <!-- Summary Icons -->
        <div class="awards-summary">
            <div class="summary-item">
                <div class="summary-icon"><svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><img src="assets/1.png" alt="Emmy Icon" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'"></div>
                <div class="summary-label">WINS/NOMINEES</div>
                <div class="summary-name">Emmy Awards</div>
                <div class="summary-count"><strong>1</strong> / 4</div>
            </div>
            <div class="summary-item">
                <div class="summary-icon"><svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><img src="assets/2.png" alt="Globe Icon" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'"></div>
                <div class="summary-label">WINS/NOMINEES</div>
                <div class="summary-name">Golden Globes</div>
                <div class="summary-count"><strong>7</strong> / 16</div>
            </div>
            <div class="summary-item">
                <div class="summary-icon"><svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><img src="assets/3.png" alt="Grammy Icon" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'"></div>
                <div class="summary-label">WINS/NOMINEES</div>
                <div class="summary-name">Grammy Awards</div>
                <div class="summary-count"><strong>11</strong> / 26</div>
            </div>
            <div class="summary-item">
                <div class="summary-icon"><svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><img src="assets/4.png" alt="Oscar Icon" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'"></div>
                <div class="summary-label">WINS/NOMINEES</div>
                <div class="summary-name">Academy Awards</div>
                <div class="summary-count"><strong>8</strong> / 19</div>
            </div>
            <div class="summary-item">
                <div class="summary-icon"><svg class="sparkle sp-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-2" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><svg class="sparkle sp-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg><img src="assets/5.png" alt="Tony Icon" onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/4/4b/Trophy_icon.svg'"></div>
                <div class="summary-label">WINS/NOMINEES</div>
                <div class="summary-name">Tony Awards</div>
                <div class="summary-count"><strong>1</strong> / 5</div>
            </div>
        </div>

        <!-- Awards Table -->
        <div class="awards-table-container">
            <div class="awards-header-row">
                <div class="col-year">YEAR <svg width="8" height="6" viewBox="0 0 8 6"><path d="M4 0L8 6H0L4 0Z" fill="currentColor"/></svg></div>
                <div class="col-award">AWARD</div>
                <div class="col-project">PROJECT</div>
                <div class="col-song">SONG</div>
                <div class="col-status">STATUS</div>
            </div>
            
            <div class="awards-row">
                <div class="col-year">2025</div>
                <div class="col-award">
                    <div class="primary-text">Emmy Award (Children's and Family)</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">National Academy of Television Arts & Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Spellbound</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Outstanding music direction and composition for an animated program</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Music Director, Michael Kosarin and Music Supervisors, Celeste Chada and Brett Swain</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Nominee</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Television</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">2025</div>
                <div class="col-award">
                    <div class="primary-text">Emmy Award (Children's and Family)</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">National Academy of Television Arts & Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Spellbound</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Outstanding original song for a children's or young teen program</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">The Way It Was Before</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Glenn Slater</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Nominee</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Television</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1983</div>
                <div class="col-award">
                    <div class="primary-text">Outer Critics Circle Award</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Outer Critics Circle</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Little Shop of Horrors</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Stage</div>
                    </div>
                </div>
            </div>
            
            
            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Song</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">A Whole New World</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Tim Rice</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1992</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Beauty and the Beast</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">2024</div>
                <div class="col-award">
                    <div class="primary-text">Tony Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">American Theatre Wing</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Newsies</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Stage</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">2024</div>
                <div class="col-award">
                    <div class="primary-text">Tony Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">American Theatre Wing</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Newsies</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Stage</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1992</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Beauty and the Beast</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">2024</div>
                <div class="col-award">
                    <div class="primary-text">Tony Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">American Theatre Wing</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Newsies</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Stage</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1992</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Beauty and the Beast</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1992</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Beauty and the Beast</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">2025</div>
                <div class="col-award">
                    <div class="primary-text">Emmy Award (Children's and Family)</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">National Academy of Television Arts & Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Spellbound</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Outstanding original song for a children's or young teen program</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">The Way It Was Before</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Glenn Slater</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Nominee</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Television</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Song</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">A Whole New World</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Tim Rice</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Song</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">A Whole New World</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Tim Rice</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">2025</div>
                <div class="col-award">
                    <div class="primary-text">Emmy Award (Children's and Family)</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">National Academy of Television Arts & Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Spellbound</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Outstanding original song for a children's or young teen program</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">The Way It Was Before</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Glenn Slater</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Nominee</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Television</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">2025</div>
                <div class="col-award">
                    <div class="primary-text">Emmy Award (Children's and Family)</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">National Academy of Television Arts & Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Spellbound</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Outstanding original song for a children's or young teen program</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">The Way It Was Before</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Glenn Slater</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Nominee</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Television</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Song</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text">A Whole New World</div>
                    <div class="meta-block">
                        <div class="meta-label">Co-Recipient</div>
                        <div class="meta-value">Tim Rice</div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1990</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">The Little Mermaid</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1992</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Beauty and the Beast</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1993</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Aladdin</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1990</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">The Little Mermaid</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>

            <div class="awards-row">
                <div class="col-year">1992</div>
                <div class="col-award">
                    <div class="primary-text">Academy Awards</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">Academy of Motion Picture Arts and Sciences</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">Beauty and the Beast</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">Best Original Score</div>
                    </div>
                </div>
                <div class="col-song">
                    <div class="primary-text"></div>
                    <div class="meta-block">
                        <div class="meta-label"></div>
                        <div class="meta-value"></div>
                    </div>
                </div>
                <div class="col-status">
                    <div class="primary-text">Winner</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">Film</div>
                    </div>
                </div>
            </div>
            <div style="height: 10vh;"></div>
        </div>
    </main>
"""

    content = content[:main_start] + awards_html + content[footer_end:]

    # Now add CSS
    style_end = content.find('</style>')
    
    # We will strip out .faq-* specific styles to keep it clean, but it's okay to just append.
    # To be clean, let's just append .awards-* styles
    
    awards_css = """
        /* Awards Page CSS */
        .awards-main {
            width: 100%;
            min-height: 100vh;
            padding-top: 32vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .awards-hero {
            display: flex;
            gap: 1.2vw;
            height: 65vh;
            justify-content: center;
            margin-bottom: 6rem;
        }

        .hero-slice {
            width: 6.5vw;
            height: 100%;
            background-color: #111;
            position: relative;
        }

        .hero-slice img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .slice-1 { transform: translateY(3vh); }
        .slice-2 { transform: translateY(-2vh); }
        .slice-3 { transform: translateY(-4vh); }
        .slice-4 { transform: translateY(2vh); }
        .slice-5 { transform: translateY(0vh); }

        .awards-title-sec {
            text-align: center;
            margin-bottom: 6rem;
        }

        .awards-title {
            font-family: 'ITC Clearface', 'Clearface', 'Cormorant Garamond', serif;
            font-size: 5rem;
            font-weight: 700;
            letter-spacing: -0.01em;
            margin-bottom: 1rem;
            color: #1a1a1a;
            -webkit-text-stroke: 1px currentColor;
        }

        .awards-subtitle {
            font-family: 'Clearface', serif;
            font-size: 1.4rem;
            font-weight: 600;
            color: rgba(26,26,26,0.7);
        }

        .awards-summary {
            display: flex;
            gap: 4rem;
            justify-content: center;
            margin-bottom: 8rem;
            width: 100%;
            max-width: 1200px;
        }

        .summary-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            flex: 1;
        }

        .summary-icon {
            height: 160px;
            width: 160px;
            position: relative;
            margin-bottom: 1.5rem;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .summary-icon img {
            height: 100%;
            width: auto;
            object-fit: contain;
            position: relative;
            z-index: 1;
        }

        @keyframes twinkle-a {
            0%   { transform: scale(1) rotate(0deg); opacity: 1; filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
            1%   { transform: scale(1.6) rotate(15deg); filter: drop-shadow(0 2px 5px rgba(0,0,0,0.2)); }
            3%   { transform: scale(1) rotate(0deg); opacity: 1; filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes twinkle-b {
            0%   { transform: scale(1) rotate(0deg); opacity: 1; }
            2%   { transform: scale(1); opacity: 1; }
            3%   { transform: scale(1.5) rotate(-20deg) translateY(-2px); filter: drop-shadow(0 4px 8px rgba(0,0,0,0.15)); }
            5%   { transform: scale(1) rotate(0deg) translateY(0); opacity: 1; filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes twinkle-c {
            0%   { transform: scale(1) rotate(0deg); opacity: 1; }
            4%   { transform: scale(1); opacity: 1; }
            5%   { transform: scale(1.7) rotate(45deg); filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2)); }
            7%   { transform: scale(1) rotate(0deg); opacity: 1; filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes twinkle-d {
            0%   { transform: scale(1) rotate(0deg); opacity: 1; }
            6%   { transform: scale(1); opacity: 1; }
            7%   { transform: scale(1.4) rotate(-10deg) translateY(2px); filter: drop-shadow(0 2px 5px rgba(0,0,0,0.1)); }
            9%   { transform: scale(1) rotate(0deg) translateY(0); opacity: 1; filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes twinkle-e {
            0%   { transform: scale(1) rotate(0deg); opacity: 1; }
            8%   { transform: scale(1); opacity: 1; }
            9%   { transform: scale(1.8) rotate(30deg); filter: drop-shadow(0 3px 6px rgba(0,0,0,0.2)); }
            11%  { transform: scale(1) rotate(0deg); opacity: 1; filter: drop-shadow(0 0 0 rgba(0,0,0,0)); }
            100% { transform: scale(1); opacity: 1; }
        }

        .sparkle {
            position: absolute;
            color: rgba(26,26,26,0.85);
            will-change: transform, filter;
            z-index: 2;
        }

        .sp-1 { animation: twinkle-a 10s infinite; }
        .sp-2 { animation: twinkle-b 10s infinite; }
        .sp-3 { animation: twinkle-c 10s infinite; }
        .sp-4 { animation: twinkle-d 10s infinite; }
        .sp-5 { animation: twinkle-e 10s infinite; }
        .sp-6 { animation: twinkle-b 10s infinite; }

        .summary-item:nth-child(2) .summary-icon {
            top: 15px;
        }

        .summary-item:nth-child(1) .sp-1 { top: 18%; left: 32%; width: 10px; height: 10px; }
        .summary-item:nth-child(1) .sp-2 { top: 22%; right: 28%; width: 14px; height: 14px; }
        .summary-item:nth-child(1) .sp-3 { top: 45%; left: 28%; width: 8px; height: 8px; }
        .summary-item:nth-child(1) .sp-4 { top: 52%; right: 30%; width: 12px; height: 12px; }
        .summary-item:nth-child(1) .sp-5 { bottom: 25%; left: 35%; width: 10px; height: 10px; }
        .summary-item:nth-child(1) .sp-6 { bottom: 20%; right: 32%; width: 12px; height: 12px; }

        .summary-item:nth-child(2) .sp-1 { top: 15%; left: 35%; width: 12px; height: 12px; }
        .summary-item:nth-child(2) .sp-2 { top: 20%; right: 38%; width: 10px; height: 10px; }
        .summary-item:nth-child(2) .sp-3 { top: 40%; left: 30%; width: 8px; height: 8px; }
        .summary-item:nth-child(2) .sp-4 { top: 45%; right: 32%; width: 14px; height: 14px; }
        .summary-item:nth-child(2) .sp-5 { bottom: 22%; left: 35%; width: 10px; height: 10px; }
        .summary-item:nth-child(2) .sp-6 { bottom: 15%; right: 30%; width: 8px; height: 8px; }

        .summary-item:nth-child(3) .sp-1 { top: 12%; left: 38%; width: 14px; height: 14px; }
        .summary-item:nth-child(3) .sp-2 { top: 25%; right: 32%; width: 10px; height: 10px; }
        .summary-item:nth-child(3) .sp-3 { top: 48%; left: 35%; width: 12px; height: 12px; }
        .summary-item:nth-child(3) .sp-4 { top: 40%; right: 28%; width: 14px; height: 14px; }
        .summary-item:nth-child(3) .sp-5 { bottom: 18%; left: 30%; width: 8px; height: 8px; }
        .summary-item:nth-child(3) .sp-6 { bottom: 22%; right: 35%; width: 10px; height: 10px; }

        .summary-item:nth-child(4) .sp-1 { top: 22%; left: 32%; width: 10px; height: 10px; }
        .summary-item:nth-child(4) .sp-2 { top: 15%; right: 30%; width: 14px; height: 14px; }
        .summary-item:nth-child(4) .sp-3 { top: 38%; left: 35%; width: 8px; height: 8px; }
        .summary-item:nth-child(4) .sp-4 { top: 45%; right: 32%; width: 12px; height: 12px; }
        .summary-item:nth-child(4) .sp-5 { bottom: 28%; left: 28%; width: 10px; height: 10px; }
        .summary-item:nth-child(4) .sp-6 { bottom: 20%; right: 35%; width: 8px; height: 8px; }

        .summary-item:nth-child(5) .sp-1 { top: 18%; left: 35%; width: 12px; height: 12px; }
        .summary-item:nth-child(5) .sp-2 { top: 25%; right: 30%; width: 10px; height: 10px; }
        .summary-item:nth-child(5) .sp-3 { top: 50%; left: 28%; width: 10px; height: 10px; }
        .summary-item:nth-child(5) .sp-4 { top: 45%; right: 35%; width: 14px; height: 14px; }
        .summary-item:nth-child(5) .sp-5 { bottom: 22%; left: 38%; width: 8px; height: 8px; }
        .summary-item:nth-child(5) .sp-6 { bottom: 18%; right: 32%; width: 12px; height: 12px; }

        .summary-item:nth-child(1) .sparkle { animation-delay: 0s; }
        .summary-item:nth-child(2) .sparkle { animation-delay: 2s; }
        .summary-item:nth-child(3) .sparkle { animation-delay: 4s; }
        .summary-item:nth-child(4) .sparkle { animation-delay: 6s; }
        .summary-item:nth-child(5) .sparkle { animation-delay: 8s; }

        .summary-label {
            font-family: 'Graphik', sans-serif;
            font-size: 0.85rem;
            font-weight: 500;
            letter-spacing: 0.15em;
            color: rgba(26,26,26,0.4);
            margin-bottom: 0.5rem;
        }

        .summary-name {
            font-family: 'ITC Clearface', 'Clearface', 'Cormorant Garamond', serif;
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            color: #1a1a1a;
        }

        .summary-count {
            font-family: 'ITC Clearface', 'Clearface', serif;
            font-size: 1.5rem;
            color: rgba(26,26,26,0.6);
        }

        .summary-count strong {
            color: #1a1a1a;
            font-weight: 700;
            font-size: 1.6rem;
        }

        /* Table */
        .awards-table-container {
            width: 100%;
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 4rem;
        }

        .awards-header-row {
            display: grid;
            grid-template-columns: 0.8fr 2.5fr 3fr 3fr 1fr;
            padding-bottom: 0.8rem;
            border-bottom: 1px solid rgba(0,0,0,0.1);
            margin-bottom: 0.5rem;
            font-family: 'Graphik', sans-serif;
            font-size: 0.95rem;
            letter-spacing: 0.15em;
            color: rgba(26,26,26,0.5);
            font-weight: 500;
            text-transform: uppercase;
            align-items: center;
        }
        
        .awards-header-row > div {
            font-family: inherit;
            font-size: inherit;
            font-weight: inherit;
            color: inherit;
        }
        
        .awards-header-row .col-year svg {
            margin-left: 5px;
            transform: translateY(-1px);
        }

        .awards-row {
            display: grid;
            grid-template-columns: 0.8fr 2.5fr 3fr 3fr 1fr;
            padding: 2.2rem 0;
            border-bottom: 1px solid rgba(0,0,0,0.06);
            align-items: start;
        }

        .col-year {
            font-family: 'ITC Clearface', 'Clearface', 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: #1a1a1a;
        }

        .primary-text {
            font-family: 'ITC Clearface', 'Clearface', 'Cormorant Garamond', serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: #1a1a1a;
            line-height: 1.2;
            min-height: 1.5rem;
        }

        .meta-block {
            margin-top: 1.4rem;
        }

        .meta-label {
            font-family: 'ITC Clearface', 'Clearface', serif;
            font-size: 1.15rem;
            color: rgba(26,26,26,0.4);
            margin-bottom: 0.1rem;
            font-weight: 400;
        }

        .meta-value {
            font-family: 'ITC Clearface', 'Clearface', serif;
            font-size: 1.2rem;
            color: rgba(26,26,26,0.6);
            line-height: 1.3;
            max-width: 90%;
            font-weight: 400;
        }
"""
    content = content[:style_end] + awards_css + content[style_end:]

    with open('awards.html', 'w', encoding='utf-8') as f:
        f.write(content)

    # We also need to update navigation to link to awards.html. 
    # But for now, we just build the page.

if __name__ == '__main__':
    build_awards_page()
