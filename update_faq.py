import re

def create_faq_item(question, answer):
    return f'''            <div class="faq-item">
                <div class="faq-question">
                    <span>{question}</span>
                    <span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5"><line x1="4" y1="12" x2="20" y2="12"/><line class="vert-line" x1="12" y1="4" x2="12" y2="20"/></svg></span>
                </div>
                <div class="faq-answer">
                    <div class="faq-answer-inner">
                        <p>{answer}</p>
                    </div>
                </div>
            </div>'''

faqs = [
    (
        "How can I send fan mail or request an autograph from John Williams?",
        "Due to the volume of correspondence received, autograph and fan mail requests may not always be accommodated. Official announcements regarding public appearances, concerts, and signing opportunities are typically communicated through authorized organizations and event partners."
    ),
    (
        "Where can I listen to John Williams' music?",
        "John Williams' compositions are available through major music streaming platforms, physical releases, concert recordings, and official soundtrack albums. Many of his most celebrated works can also be experienced through live orchestral performances around the world."
    ),
    (
        "Does John Williams still compose new music?",
        "Yes. Even after decades of groundbreaking work in film music, John Williams has continued composing for select projects, concert works, and special commissions. Recent projects include music for major motion pictures and orchestral performances."
    ),
    (
        "What are John Williams' most famous film scores?",
        "Some of John Williams' most recognized scores include:<br><br>Star Wars, Indiana Jones, Jurassic Park, Harry Potter, E.T. the Extra-Terrestrial, Jaws, Superman, Schindler's List, Home Alone and Close Encounters of the Third Kind<br><br>These works have become some of the most iconic pieces of film music ever written."
    ),
    (
        "Has John Williams won any Academy Awards?",
        "Yes. John Williams is one of the most awarded and nominated composers in film history. Throughout his career, he has received multiple Academy Awards and has accumulated more Oscar nominations than almost any living individual in the entertainment industry."
    ),
    (
        "Does John Williams conduct his own music?",
        "John Williams has frequently conducted performances of his own compositions with leading orchestras around the world, including long-standing collaborations with major symphony orchestras and special concert events dedicated to his music."
    ),
    (
        "Can I perform or record a John Williams composition?",
        "Performance and recording rights depend on the specific work and intended use. Appropriate licenses may be required through music publishers, rights organizations, or copyright holders before recording, distributing, or publicly performing copyrighted material."
    ),
    (
        "Does John Williams write concert music in addition to film scores?",
        "Yes. In addition to his work for film and television, John Williams has composed numerous concert works, including symphonies, concertos, fanfares, chamber music, and pieces commissioned for major orchestras and solo performers."
    ),
    (
        "What orchestras has John Williams worked with?",
        "Throughout his career, John Williams has collaborated with many of the world's most prestigious orchestras, including:<br><br>Boston Pops Orchestra<br>Boston Symphony Orchestra<br>Vienna Philharmonic<br>London Symphony Orchestra<br>Los Angeles Philharmonic<br><br>and numerous ensembles across Europe, North America, and Asia."
    ),
    (
        "Where can I find upcoming concerts featuring John Williams' music?",
        "Upcoming performances can often be found through official orchestra websites, concert venues, film music festivals, and special events dedicated to the music of John Williams. Programs frequently feature selections from Star Wars, Harry Potter, Indiana Jones, and many other celebrated scores."
    )
]

new_faq_html = "\n".join(create_faq_item(q, a) for q, a in faqs)
new_faq_list = f'''        <div class="faq-list">
{new_faq_html}
            
            <div style="height: 10vh;"></div>
        </div>'''

with open('faq.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the faq-list div block
start_idx = content.find('<div class="faq-list">')
end_idx = content.find('</main>', start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_faq_list + "\n    " + content[end_idx:]
    with open('faq.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced faq-list successfully.")
else:
    print("Could not find faq-list block.")
