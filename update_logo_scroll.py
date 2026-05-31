import os
import glob
import re

html_files = glob.glob("*.html")

scroll_script = """
    <!-- Global Logo Scroll Logic -->
    <script>
    document.addEventListener("DOMContentLoaded", () => {
        const logoEl = document.querySelector('.logo-text');
        if (!logoEl) return;
        
        let isLogoHiddenFlag = false;
        
        function checkLogoVisibility() {
            let totalScroll = 0;
            const sc = document.querySelector('.work-scroll-container');
            const wl = document.querySelector('.work-list');
            
            if (sc) totalScroll += sc.scrollTop;
            if (wl) {
                try {
                    const yVal = (typeof gsap !== 'undefined') ? gsap.getProperty(wl, "y") : 0;
                    totalScroll += Math.abs(parseFloat(yVal) || 0);
                } catch(e) {}
            }
            totalScroll += window.scrollY || document.documentElement.scrollTop || 0;
            
            if (totalScroll > 50 && !isLogoHiddenFlag) {
                isLogoHiddenFlag = true;
                logoEl.classList.add('hidden-logo');
            } else if (totalScroll <= 50 && isLogoHiddenFlag) {
                isLogoHiddenFlag = false;
                logoEl.classList.remove('hidden-logo');
            }
            
            requestAnimationFrame(checkLogoVisibility);
        }
        
        requestAnimationFrame(checkLogoVisibility);
    });
    </script>
"""

for file in html_files:
    if file.startswith("scratch") or file.startswith("temp") or file.startswith("test"):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # ensure .hidden-logo is in the CSS if not already
    if '.logo-text.hidden-logo' not in content:
        css_addition = """
        .logo-text.hidden-logo {
            opacity: 0 !important;
            transform: translateY(-50px) rotate(-2deg) !important;
            pointer-events: none !important;
        }
        """
        # Inject before </style> or </head>
        if '</style>' in content:
            content = content.replace("</style>", css_addition + "\n    </style>", 1)
        else:
            content = content.replace("</head>", "<style>" + css_addition + "</style>\n</head>", 1)

    # remove old inline logic from work.html if exists
    old_logic_pattern = r'// Logo hide on scroll.*?\/\/ Start the robust loop\s*requestAnimationFrame\(checkLogoVisibilityLoop\);'
    content = re.sub(old_logic_pattern, '', content, flags=re.DOTALL)

    if "Global Logo Scroll Logic" not in content:
        content = content.replace("</body>", scroll_script + "\n</body>")
    else:
        # replace it
        content = re.sub(r'<!-- Global Logo Scroll Logic -->.*?</script>', scroll_script.strip(), content, flags=re.DOTALL)

    # In index.html, there might be other scroll containers. E.g. `#smooth-content` or just `window`.
    # The logic handles window.scrollY already.

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated logo scroll logic in all HTML files.")
