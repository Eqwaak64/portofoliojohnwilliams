data = [
    (2024, 'Academy Award', 'Indiana Jones and the Dial of Destiny', 'Original Score', 'Nominee'),
    (2024, 'Grammy Award', 'Indiana Jones and the Dial of Destiny', 'Score Soundtrack for Visual Media', 'Nominee'),
    (2024, 'Grammy Award', 'Indiana Jones and the Dial of Destiny', 'Helena\'s Theme', 'Winner'),
    (2023, 'Academy Award', 'The Fabelmans', 'Original Score', 'Nominee'),
    (2023, 'Grammy Award', 'The Fabelmans', 'Original Score', 'Nominee'),
    (2020, 'Grammy Award', 'Star Wars: Galaxy\'s Edge', 'Symphonic Suite', 'Winner'),
    (2020, 'Academy Award', 'Star Wars: The Rise of Skywalker', 'Original Score', 'Nominee'),
    (2018, 'BMI Film & TV Awards', 'Career Achievement', 'The John Williams Award', 'Winner'),
    (2016, 'AFI Life Achievement Award', 'Career Achievement', 'Lifetime Achievement', 'Winner'),
    (2016, 'Grammy Award', 'Star Wars: The Force Awakens', 'Original Score', 'Winner'),
    (2016, 'Academy Award', 'Star Wars: The Force Awakens', 'Original Score', 'Nominee'),
    (2014, 'Grammy Award', 'The Book Thief', 'Original Score', 'Winner'),
    (2013, 'Academy Award', 'Lincoln', 'Original Score', 'Nominee'),
    (2012, 'BAFTA Award', 'War Horse', 'Original Score', 'Nominee'),
    (2012, 'Academy Award', 'War Horse', 'Original Score', 'Nominee'),
    (2012, 'Academy Award', 'The Adventures of Tintin', 'Original Score', 'Nominee'),
    (2006, 'Golden Globe Award', 'Memoirs of a Geisha', 'Original Score', 'Winner'),
    (2006, 'BAFTA Award', 'Memoirs of a Geisha', 'Original Score', 'Winner'),
    (2006, 'Academy Award', 'Memoirs of a Geisha', 'Original Score', 'Winner'),
    (2006, 'Grammy Award', 'Memoirs of a Geisha', 'Original Score', 'Winner'),
    (2006, 'Academy Award', 'Munich', 'Original Score', 'Nominee'),
    (2005, 'Academy Award', 'Harry Potter and the Prisoner of Azkaban', 'Original Score', 'Nominee'),
    (2003, 'Academy Award', 'Catch Me If You Can', 'Original Score', 'Nominee'),
    (2002, 'Saturn Award', 'A.I. Artificial Intelligence', 'Original Score', 'Winner'),
    (2002, 'Academy Award', 'Harry Potter and the Sorcerer\'s Stone', 'Original Score', 'Nominee'),
    (2002, 'Academy Award', 'A.I. Artificial Intelligence', 'Original Score', 'Nominee'),
    (2001, 'National Board of Review', 'Career Achievement', 'Excellence in Film Music', 'Winner'),
    (2000, 'Academy Award', 'Angela\'s Ashes', 'Original Score', 'Nominee'),
    (2000, 'Academy Award', 'The Patriot', 'Original Score', 'Nominee'),
    (1999, 'Academy Award', 'Saving Private Ryan', 'Original Score', 'Nominee'),
    (1998, 'Academy Award', 'Amistad', 'Original Score', 'Nominee'),
    (1996, 'Academy Award', 'Sabrina', 'Moonlight', 'Nominee'),
    (1996, 'Academy Award', 'Sabrina', 'Original Score', 'Nominee'),
    (1996, 'Academy Award', 'Nixon', 'Original Score', 'Nominee'),
    (1994, 'Academy Award', 'Schindler\'s List', 'Original Score', 'Winner'),
    (1994, 'BAFTA Award', 'Schindler\'s List', 'Original Score', 'Winner'),
    (1994, 'Grammy Award', 'Schindler\'s List', 'Original Score', 'Winner'),
    (1992, 'Academy Award', 'Hook', 'When You\'re Alone', 'Nominee'),
    (1992, 'Academy Award', 'JFK', 'Original Score', 'Nominee'),
    (1991, 'Academy Award', 'Home Alone', 'Somewhere in My Memory', 'Nominee'),
    (1991, 'Academy Award', 'Home Alone', 'Original Score', 'Nominee'),
    (1990, 'Academy Award', 'Born on the Fourth of July', 'Original Score', 'Nominee'),
    (1990, 'Academy Award', 'Indiana Jones and the Last Crusade', 'Original Score', 'Nominee'),
    (1989, 'Academy Award', 'The Accidental Tourist', 'Original Score', 'Nominee'),
    (1988, 'Academy Award', 'Empire of the Sun', 'Original Score', 'Nominee'),
    (1988, 'Academy Award', 'The Witches of Eastwick', 'Original Score', 'Nominee'),
    (1985, 'Academy Award', 'The River', 'Original Score', 'Nominee'),
]

html = ''
for year, award, proj, song, status in data:
    html += f'''            <div class="awards-row">
                <div class="col-year">{year}</div>
                <div class="col-award">
                    <div class="primary-text">{award}</div>
                </div>
                <div class="col-project">
                    <div class="primary-text">{proj}</div>
                </div>
                <div class="col-song">
                    <div class="primary-text">{song}</div>
                </div>
                <div class="col-status">
                    <div class="primary-text">{status}</div>
                </div>
            </div>\n'''

with open('new_rows.html', 'w') as f:
    f.write(html)
