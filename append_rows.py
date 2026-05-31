data = [
    (1985, 'Academy Award', 'Indiana Jones and the Temple of Doom', 'Original Score', 'Nominee'),
    (1984, 'Saturn Award', 'Return of the Jedi', 'Original Score', 'Nominee'),
    (1983, 'Academy Award', 'E.T. the Extra-Terrestrial', 'Original Score', 'Winner'),
    (1983, 'Saturn Award', 'E.T. the Extra-Terrestrial', 'Original Score', 'Winner'),
    (1982, 'Academy Award', 'Raiders of the Lost Ark', 'Original Score', 'Nominee'),
    (1982, 'Saturn Award', 'Raiders of the Lost Ark', 'Original Score', 'Winner'),
    (1981, 'Academy Award', 'The Empire Strikes Back', 'Original Score', 'Nominee'),
    (1980, 'Grammy Award', 'Superman', 'Original Score', 'Winner'),
    (1979, 'Saturn Award', 'Superman', 'Original Score', 'Winner'),
    (1978, 'Academy Award', 'Star Wars', 'Original Score', 'Winner'),
    (1978, 'Grammy Award', 'Star Wars', 'Original Score', 'Winner'),
    (1978, 'Grammy Award', 'Main Title from Star Wars', 'Instrumental Composition', 'Winner'),
    (1978, 'Saturn Award', 'Star Wars', 'Original Score', 'Winner'),
    (1978, 'Saturn Award', 'Close Encounters of the Third Kind', 'Original Score', 'Winner'),
    (1977, 'Academy Award', 'Jaws', 'Original Score', 'Winner'),
    (1977, 'Grammy Award', 'Jaws', 'Original Score', 'Winner'),
    (1974, 'Academy Award', 'Cinderella Liberty', 'Nice to Be Around', 'Nominee'),
    (1974, 'Academy Award', 'Cinderella Liberty', 'Original Score', 'Nominee'),
    (1973, 'Emmy Award', 'Jane Eyre', 'Music Composition', 'Winner'),
    (1972, 'Academy Award', 'Images', 'Original Dramatic Score', 'Nominee'),
    (1972, 'Academy Award', 'The Poseidon Adventure', 'Original Dramatic Score', 'Nominee'),
    (1972, 'Academy Award', 'Fiddler on the Roof', 'Adaptation Score', 'Winner'),
    (1969, 'Emmy Award', 'Heidi', 'Musical Composition', 'Winner'),
    (1963, 'Emmy Award', 'Alcoa Premiere', 'Original Music', 'Nominee'),
    (1962, 'Emmy Award', 'Alcoa Premiere', 'Music Composition', 'Nominee'),
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

with open('awards.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<div style="height: 10vh;"></div>'
new_content = content.replace(target, html + target)

with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
