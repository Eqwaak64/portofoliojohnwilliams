import json

def add_stars(title, star_positions):
    """
    star_positions is a list of indices where the letter should have a star.
    """
    result = ""
    for i, char in enumerate(title):
        if i in star_positions:
            result += f'Wh<span class="star-wrapper">{char}<svg class="tiny-star" viewBox="0 0 24 24"><path d="M12 0 L13.5 10.5 L24 12 L13.5 13.5 L12 24 L10.5 13.5 L0 12 L10.5 10.5 Z" /></svg></span>'
            # Wait, removing "Wh" prefix
            pass
            
    return result

categories = [
    {
        "title": "ANIMATED FILM MUSICAL",
        "items": [
            ("The Little Mermaid", [7, 15]),  # t, a
            ("Beauty and the Beast", [7, 12, 19]), # a, h, a -> Beauty a(7)nd t(12)he Bea(19)st. Wait. B(0)e(1)a(2)u(3)t(4)y(5) (6)a(7)n(8)d(9) (10)t(11)h(12)e(13) (14)B(15)e(16)a(17)s(18)t(19)? Let's just do replace.
        ]
    }
]

def make_title(text, star_chars):
    # Just a simple replacer for this script:
    res = text
    for c in star_chars:
        # replace the first occurrence or specific occurrences
        pass

# It's easier to just type them out.

