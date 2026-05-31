import re
import random

samples = [
    {
        'year': '2025', 'award': 'Emmy Award (Children\'s and Family)', 'presented': 'National Academy of Television Arts & Sciences',
        'project': 'Spellbound', 'category': 'Outstanding original song for a children\'s or young teen program',
        'song': 'The Way It Was Before', 'corecipient': 'Glenn Slater',
        'status': 'Nominee', 'type': 'Television'
    },
    {
        'year': '2024', 'award': 'Tony Awards', 'presented': 'American Theatre Wing',
        'project': 'Newsies', 'category': 'Best Original Score',
        'song': '', 'corecipient': '',
        'status': 'Winner', 'type': 'Stage'
    },
    {
        'year': '1993', 'award': 'Academy Awards', 'presented': 'Academy of Motion Picture Arts and Sciences',
        'project': 'Aladdin', 'category': 'Best Original Score',
        'song': '', 'corecipient': '',
        'status': 'Winner', 'type': 'Film'
    },
    {
        'year': '1993', 'award': 'Academy Awards', 'presented': 'Academy of Motion Picture Arts and Sciences',
        'project': 'Aladdin', 'category': 'Best Original Song',
        'song': 'A Whole New World', 'corecipient': 'Tim Rice',
        'status': 'Winner', 'type': 'Film'
    },
    {
        'year': '1992', 'award': 'Academy Awards', 'presented': 'Academy of Motion Picture Arts and Sciences',
        'project': 'Beauty and the Beast', 'category': 'Best Original Score',
        'song': '', 'corecipient': '',
        'status': 'Winner', 'type': 'Film'
    },
    {
        'year': '1990', 'award': 'Academy Awards', 'presented': 'Academy of Motion Picture Arts and Sciences',
        'project': 'The Little Mermaid', 'category': 'Best Original Score',
        'song': '', 'corecipient': '',
        'status': 'Winner', 'type': 'Film'
    }
]

def generate_row(data):
    song_block = f'''
                    <div class="primary-text">{data['song']}</div>
                    <div class="meta-block">
                        <div class="meta-label">{ 'Co-Recipient' if data['corecipient'] else '' }</div>
                        <div class="meta-value">{data['corecipient']}</div>
                    </div>'''
    
    return f'''
            <div class="awards-row">
                <div class="col-year">{data['year']}</div>
                <div class="col-award">
                    <div class="primary-text">{data['award']}</div>
                    <div class="meta-block">
                        <div class="meta-label">Presented by</div>
                        <div class="meta-value">{data['presented']}</div>
                    </div>
                </div>
                <div class="col-project">
                    <div class="primary-text">{data['project']}</div>
                    <div class="meta-block">
                        <div class="meta-label">Category</div>
                        <div class="meta-value">{data['category']}</div>
                    </div>
                </div>
                <div class="col-song">{song_block}
                </div>
                <div class="col-status">
                    <div class="primary-text">{data['status']}</div>
                    <div class="meta-block">
                        <div class="meta-label">Type</div>
                        <div class="meta-value">{data['type']}</div>
                    </div>
                </div>
            </div>'''

rows_html = []
for i in range(22):
    rows_html.append(generate_row(random.choice(samples)))

added_html = '\n'.join(rows_html)

for file in ['awards.html', 'build_awards.py']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pos = content.rfind('<div class="awards-row">')
    if pos != -1:
        end_pos = content.find('<div style="height: 10vh;"></div>', pos)
        
        if end_pos != -1:
            new_content = content[:end_pos] + added_html + '\n            ' + content[end_pos:]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated {file}')
        else:
            print(f'Could not find end of row in {file}')
    else:
        print(f'Could not find awards-row in {file}')
