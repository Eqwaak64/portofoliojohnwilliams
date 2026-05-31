import re

with open('d:/alanmenken/awards.html', 'r', encoding='utf-8') as f:
    content = f.read()

scroll_trigger_logic = """
        // ScrollTrigger Animations
        gsap.registerPlugin(ScrollTrigger);

        // Sketch Images (Summary Items) Pop Up
        const summaryItems = document.querySelectorAll('.summary-item');
        if (summaryItems.length > 0) {
            gsap.from(summaryItems, {
                scrollTrigger: {
                    trigger: '.awards-summary',
                    start: 'top 80%',
                    toggleActions: 'play none none reverse'
                },
                y: 50,
                scale: 0.8,
                opacity: 0,
                duration: 0.8,
                stagger: 0.15,
                ease: 'back.out(1.7)'
            });
        }

        // Table Rows Slide Up
        const tableRows = document.querySelectorAll('.awards-row');
        if (tableRows.length > 0) {
            gsap.from(tableRows, {
                scrollTrigger: {
                    trigger: '.awards-table-container',
                    start: 'top 85%',
                    toggleActions: 'play none none reverse'
                },
                y: 50,
                opacity: 0,
                duration: 0.6,
                stagger: 0.1,
                ease: 'power2.out'
            });
        }
"""

# Insert scroll_trigger_logic before "// Hamburger Menu Logic"
content = content.replace('// Hamburger Menu Logic', scroll_trigger_logic + '\n        // Hamburger Menu Logic')

with open('d:/alanmenken/awards.html', 'w', encoding='utf-8') as f:
    f.write(content)
