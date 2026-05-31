import re

def refine_faq_answers():
    with open('faq.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update the + SVG to use two lines so we can animate it to a minus
    # Current SVG: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5"><path d="M12 5v14M5 12h14"></path></svg>
    # We want: <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5"><line x1="5" y1="12" x2="19" y2="12"/><line class="vert-line" x1="12" y1="5" x2="12" y2="19"/></svg>
    content = re.sub(
        r'<path d="M12 5v14M5 12h14"></path>',
        r'<line x1="4" y1="12" x2="20" y2="12"/><line class="vert-line" x1="12" y1="4" x2="12" y2="20"/>',
        content
    )

    # 2. Update CSS for animation and answers
    # Find .faq-item.active .faq-icon
    old_active_icon = r'\.faq-item\.active \.faq-icon\s*\{[^}]*\}'
    new_active_icon = """.faq-item.active .faq-icon {
            /* no rotation, we just hide the vertical line */
        }
        
        .vert-line {
            transition: transform 0.4s cubic-bezier(0.77, 0, 0.175, 1), opacity 0.4s;
            transform-origin: center;
        }

        .faq-item.active .vert-line {
            transform: scaleY(0);
            opacity: 0;
        }"""
    
    content = re.sub(old_active_icon, new_active_icon, content)
    
    # .faq-icon transition: remove rotation if it was on the whole icon
    content = content.replace("transition: transform 0.4s cubic-bezier(0.77, 0, 0.175, 1);", "")

    # Update .faq-answer styles
    # We need to set color, font-size, line-height, max-width
    content = re.sub(
        r'(\.faq-answer\s*\{[^}]*font-size:\s*)1\.15rem([^}]*color:\s*)rgba\(26,\s*26,\s*26,\s*0\.7\)',
        r'\g<1>1.25rem\g<2>#4a4a4a',
        content
    )
    
    # Update .faq-answer-inner spacing
    content = re.sub(
        r'(\.faq-answer-inner\s*\{[^}]*padding-bottom:\s*)2\.2rem',
        r'\g<1>4rem;\n            padding-top: 1rem;\n            max-width: 48%;',
        content
    )
    
    # Add link styles
    link_styles = """
        .faq-answer a {
            color: inherit;
            text-decoration: none;
            border-bottom: 1px solid currentColor;
            padding-bottom: 1px;
            transition: opacity 0.3s;
        }
        .faq-answer a:hover {
            opacity: 0.6;
        }
"""
    content = content.replace('</style>', link_styles + '</style>')

    # 3. Update Text content for the first 3 answers
    # Answer 1
    content = re.sub(
        r'<p>Due to the overwhelming amount of requests.*?</p>',
        r'<p>Due to personal and logistical reasons, Alan is no longer able to accept or respond to fan mail or autograph requests. This wasn’t an easy decision, but as the volume has grown, it’s become difficult to manage in a meaningful way. Please know that every kind word has been deeply appreciated, and he carries that appreciation with him always.</p>',
        content
    )
    
    # Answer 2
    content = re.sub(
        r'<p>Most of Alan\'s sheet music can be found online.*?</p>',
        r'<p>Head to <a href="http://www.musicnotes.com" target="_blank">www.musicnotes.com</a> to find a full catalogue of Alan\'s music.</p>',
        content
    )
    
    # Answer 3
    content = re.sub(
        r'<p>Yes, provided you secure the proper mechanical licensing rights.*?</p>',
        r'<p>If a song has been recorded already, anyone may apply for a mechanical license to record their own version. Please contact the publisher for more details.</p>',
        content
    )

    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    refine_faq_answers()
