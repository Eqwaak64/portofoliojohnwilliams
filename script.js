const fs = require('fs');
const content = fs.readFileSync('d:/alanmenken/biography.html', 'utf8');

const newContent = 
            <aside class="bio-sidebar">
                <nav class="bio-timeline">
                    <a href="#summary" class="timeline-link active">JOHN WILLIAMS<br>SUMMARY</a>
                    <a href="#early-life" class="timeline-link">EARLY LIFE & MUSICAL FOUNDATIONS<br>1932 &mdash; 1950</a>
                    <a href="#apprentice" class="timeline-link">HOLLYWOOD APPRENTICE YEARS<br>1955 &mdash; 1969</a>
                    <a href="#spielberg-lucas" class="timeline-link">THE SPIELBERG-LUCAS REVOLUTION<br>1971 &mdash; 1979</a>
                    <a href="#golden-era" class="timeline-link">THE GOLDEN ERA<br>1980 &mdash; 1993</a>
                    <a href="#legacy-expands" class="timeline-link">THE LEGACY EXPANDS<br>1994 &mdash; 2004</a>
                    <a href="#summit" class="timeline-link">THE MASTER AT THE SUMMIT<br>2005 &mdash; 2015</a>
                    <a href="#legend" class="timeline-link">THE LIVING LEGEND<br>2016 &mdash; Present</a>
                </nav>
            </aside>
            
            <div class="bio-sections">
                <!-- Summary Section -->
                <section id="summary" class="bio-section">
                    <p class="section-label">Summary</p>
                    <h2 class="section-title">Biography of John Williams</h2>
                    <div class="section-header-split">
                        <div class="header-left">
                            <h3 class="section-subtitle">The Soundtrack of Modern Cinema</h3>
                            <p class="section-desc">John Towner Williams stands as one of the most influential composers in the history of music and film. Across more than seven decades, his work has shaped the emotional language of modern cinema, creating some of the most recognizable themes ever written. From the terror of Jaws and the wonder of E.T. to the mythology of Star Wars and the adventure of Indiana Jones, Williams transformed film scoring into an art form capable of defining entire generations. His music transcends movies, becoming part of global culture itself.</p>
                        </div>
                        <div class="header-right">
                            <div style="width: 100%; height: 400px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
                
                <!-- Early Life Section -->
                <section id="early-life" class="bio-section">
                    <p class="section-date">1932 &mdash; 1950</p>
                    <h2 class="section-title">E<span class="bio-a-star">a<svg viewBox="0 0 24 24"><path d="M12 2 C12 9, 15 12, 22 12 C15 12, 12 15, 12 22 C12 15, 9 12, 2 12 C9 12, 12 9, 12 2 Z"/></svg></span>rly Life & Musical Foundations</h2>
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">1932</p>
                            <p class="section-text-small">John Towner Williams was born on February 8, 1932, in Flushing, Queens, New York. Music surrounded him from the very beginning. His father, Johnny Williams, was a professional percussionist with the CBS Radio Orchestra, exposing young John to the world of professional musicians long before he considered a career of his own. Growing up in a musical household, Williams quickly developed a fascination with instruments, composition, and orchestral sound.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1940s</p>
                            <p class="section-text-small">During the 1940s, he studied piano while also learning trumpet, trombone, and clarinet. Unlike many young musicians, Williams was not content merely to perform music; he wanted to understand how it worked. He spent countless hours analyzing scores and experimenting with his own compositions, laying the foundation for the sophisticated orchestral language that would later define his career.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1948</p>
                            <p class="section-text-small">In 1948, the Williams family relocated to Los Angeles. The move proved life-changing. Surrounded by the growing film industry, Williams found himself closer to the creative world that would eventually make him famous. He studied composition with Mario Castelnuovo-Tedesco, one of Hollywood's most respected teachers, while also attending UCLA.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1950s</p>
                            <p class="section-text-small">Military service interrupted his studies in the early 1950s, but it also provided valuable experience. While serving in the United States Air Force, Williams arranged music for military ensembles and developed skills as a conductor and orchestrator. After completing his service, he moved to New York and enrolled at the Juilliard School, studying piano under the legendary Rosina Lhévinne. These years strengthened both his technical mastery and artistic discipline, preparing him for the extraordinary career that lay ahead.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <div style="width: 100%; height: 500px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
                
                <!-- Apprentice Section -->
                <section id="apprentice" class="bio-section">
                    <p class="section-date">1955 &mdash; 1969</p>
                    <h2 class="section-title">Hollywood Apprentice Years</h2>
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">1950s</p>
                            <p class="section-text-small">Returning to Los Angeles in the mid-1950s, Williams entered Hollywood not as a famous composer, but as a hardworking pianist and orchestrator. He became one of the industry's most respected studio musicians, performing on numerous landmark productions while learning from masters such as Alfred Newman, Bernard Herrmann, Henry Mancini, Elmer Bernstein, and Jerry Goldsmith. Every recording session became an education in orchestration, storytelling, and musical craftsmanship.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1960s</p>
                            <p class="section-text-small">Throughout the 1960s, Williams established himself as one of Hollywood's most versatile musical talents. He performed on classics including West Side Story, Breakfast at Tiffany's, To Kill a Mockingbird, and Some Like It Hot. At the same time, he began composing extensively for television, writing music for series such as Lost in Space, Gilligan's Island, and Wagon Train. The demanding pace of television production forced him to develop speed, efficiency, and versatility—skills that would later prove invaluable when scoring major motion pictures.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1967</p>
                            <p class="section-text-small">A major breakthrough arrived in 1967 when Williams received his first Academy Award nomination for Valley of the Dolls. While he was not yet a household name, industry insiders increasingly recognized him as one of the most promising composers working in Hollywood. The apprenticeship years were ending, and a new chapter was about to begin.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <div style="width: 100%; height: 500px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
                
                <!-- Spielberg-Lucas Section -->
                <section id="spielberg-lucas" class="bio-section">
                    <p class="section-date">1971 &mdash; 1979</p>
                    <h2 class="section-title">The Spielberg-Lucas Revolution</h2>
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">1970s</p>
                            <p class="section-text-small">The 1970s transformed John Williams from a respected composer into an international phenomenon. The decade began with his first Academy Award victory for Fiddler on the Roof in 1971, demonstrating his ability to adapt and elevate existing musical material. Yet even greater achievements were still ahead.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1975</p>
                            <p class="section-text-small">Everything changed in 1975 with Jaws. Working with a young Steven Spielberg, Williams created one of the simplest and most effective musical ideas in film history: the now-legendary two-note shark motif. The score generated immense tension and became inseparable from the film itself, earning Williams his second Academy Award.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1977</p>
                            <p class="section-text-small">Only two years later came Star Wars. At a time when many science-fiction films relied on contemporary or electronic sounds, Williams proposed a grand symphonic score inspired by classical composers such as Holst, Korngold, and Wagner. The result revolutionized film music. Themes such as the Main Title, Princess Leia's Theme, and The Force Theme became instantly iconic and helped define an entire cinematic universe. The score won another Academy Award and remains one of the most influential soundtracks ever composed.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">By the end of the decade, collaborations with Spielberg and George Lucas had positioned Williams at the center of modern cinema. His music helped revive the large symphonic orchestra in Hollywood and established a new standard for blockbuster filmmaking.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <div style="width: 100%; height: 500px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
                
                <!-- Golden Era Section -->
                <section id="golden-era" class="bio-section">
                    <p class="section-date">1980 &mdash; 1993</p>
                    <h2 class="section-title">The Golden Era</h2>
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">1980s</p>
                            <p class="section-text-small">The 1980s and early 1990s are often regarded as the golden age of John Williams' career. Having already transformed film music through Star Wars and Jaws, he entered a period of extraordinary creative productivity that produced some of the most beloved scores in cinematic history. During these years, Williams became more than a composer—he became one of the defining voices of modern storytelling.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">In 1980, Williams was appointed conductor of the Boston Pops Orchestra, a position that elevated him beyond Hollywood and into the broader world of American musical culture. Through television broadcasts, recordings, and international tours, he introduced orchestral music to millions of listeners who might never have attended a symphony concert.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1982</p>
                            <p class="section-text-small">The same era saw the release of some of his most celebrated works. The Empire Strikes Back introduced The Imperial March and Yoda's Theme, while Raiders of the Lost Ark gave the world the unforgettable Raiders March. In 1982, Williams composed the score for E.T. the Extra-Terrestrial, a work whose emotional power helped transform Spielberg's film into a timeless classic. The score earned Williams his fourth Academy Award and remains one of the most admired achievements in film music.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">Throughout the decade, Williams expanded his influence beyond cinema through compositions written for the Olympic Games. His ceremonial works, particularly Olympic Fanfare and Theme, became symbols of international celebration and achievement. Few composers have successfully moved between Hollywood blockbusters and global cultural events with such ease.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1993</p>
                            <p class="section-text-small">The period reached its artistic peak in 1993 with two masterpieces released in the same year. Jurassic Park captured wonder, discovery, and adventure through one of Williams' most uplifting themes, while Schindler's List revealed an entirely different side of his artistry. Built around a haunting violin melody performed by Itzhak Perlman, the score conveyed profound sorrow and humanity. Williams later remarked that Spielberg's film deserved a better composer than himself; Spielberg famously replied that all the better composers were dead. The score earned Williams his fifth Academy Award and is widely regarded as one of the greatest film scores ever written.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">By the early 1990s, Williams had already secured his place among the most important composers in film history. Yet remarkably, another major chapter of his career was just beginning.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <div style="width: 100%; height: 500px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
                
                <!-- Legacy Expands Section -->
                <section id="legacy-expands" class="bio-section">
                    <p class="section-date">1994 &mdash; 2004</p>
                    <h2 class="section-title">The Legacy Expands</h2>
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">1994</p>
                            <p class="section-text-small">Following the extraordinary success of Jurassic Park and Schindler's List, many might have expected Williams to slow down. Instead, he entered another period of remarkable creativity, producing scores that would define a new generation of audiences while simultaneously expanding his reputation as a concert composer and conductor.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1995</p>
                            <p class="section-text-small">During the mid-1990s, Williams devoted increasing attention to orchestral concert works. His collaborations with world-renowned musicians such as Yo-Yo Ma demonstrated that his ambitions extended well beyond film scoring. While continuing to compose for Hollywood, he also strengthened his presence in the concert hall, earning recognition as a serious composer in both worlds.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">1999</p>
                            <p class="section-text-small">The late 1990s brought several major achievements. Saving Private Ryan showcased a restrained and deeply emotional approach to war drama, while Amistad and Angela's Ashes revealed his gift for lyrical and historical storytelling. Yet perhaps the most significant moment arrived in 1999 when Williams returned to the galaxy far, far away with Star Wars: Episode I – The Phantom Menace. The score introduced Duel of the Fates, a composition whose powerful choir and dramatic orchestration instantly became one of the most recognizable pieces of film music ever created.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2001</p>
                            <p class="section-text-small">A new millennium brought another cultural phenomenon. In 2001, Williams was tasked with creating the musical identity of the Harry Potter universe. The result was Hedwig's Theme, a melody so iconic that it became synonymous with the franchise itself. Like the themes of Star Wars, Indiana Jones, and Jurassic Park, it entered popular culture and remains instantly recognizable around the world.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">Between 2001 and 2004, Williams balanced work on Harry Potter, Star Wars, A.I. Artificial Intelligence, Minority Report, and Catch Me If You Can. These projects demonstrated extraordinary versatility, moving effortlessly between fantasy, science fiction, suspense, drama, and comedy. During the same period, he received the Olympic Order and the Kennedy Center Honors, affirming his status as one of America's most influential artistic figures.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2004</p>
                            <p class="section-text-small">By the end of 2004, Williams had achieved what few artists ever accomplish: he had successfully reinvented himself for a new generation while preserving the excellence that had defined his earlier work.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <div style="width: 100%; height: 500px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
                
                <!-- Summit Section -->
                <section id="summit" class="bio-section">
                    <p class="section-date">2005 &mdash; 2015</p>
                    <h2 class="section-title">The Master at the Summit</h2>
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">2005</p>
                            <p class="section-text-small">Entering the twenty-first century's second decade, Williams had already become a living legend. Yet rather than relying on past achievements, he continued producing music of remarkable sophistication and emotional depth.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">One of the defining works of this period was Memoirs of a Geisha (2005). Collaborating with Yo-Yo Ma and Itzhak Perlman, Williams created one of the most elegant and refined scores of his career. Blending orchestral textures with Japanese influences, the music earned widespread critical acclaim and demonstrated his continuing artistic evolution after more than four decades in the industry.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2008</p>
                            <p class="section-text-small">The following years saw Williams continue his long partnership with Steven Spielberg through films such as The Adventures of Tintin, War Horse, and Lincoln. Rather than emphasizing spectacle, many of these scores displayed maturity, restraint, and emotional subtlety. Particularly in Lincoln, Williams focused on humanity and character rather than patriotic grandeur, creating one of the most thoughtful scores of his later career.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2013</p>
                            <p class="section-text-small">In 2013, The Book Thief further showcased his ability to communicate intimacy and hope through music. At an age when most composers had long retired, Williams remained one of the industry's most sought-after creative voices. His influence could be heard throughout Hollywood, inspiring a new generation of composers who had grown up listening to his music.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2015</p>
                            <p class="section-text-small">The era culminated in 2015 with Star Wars: The Force Awakens. Returning once again to the saga that helped define his career, Williams introduced memorable new themes such as Rey's Theme and March of the Resistance. Rather than simply revisiting old material, he expanded the musical language of Star Wars for a new generation of audiences.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">At more than eighty years old, Williams remained at the peak of his profession—a rare achievement in any artistic field.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <div style="width: 100%; height: 500px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
                
                <!-- Legend Section -->
                <section id="legend" class="bio-section">
                    <p class="section-date">2016 &mdash; Present</p>
                    <h2 class="section-title">The Living Legend</h2>
                    <div class="content-split">
                        <div class="split-left">
                            <p class="section-date-small">2016</p>
                            <p class="section-text-small">By the mid-2010s, John Williams had already achieved virtually every honor available to a composer. His music had shaped generations of filmmakers, inspired countless musicians, and become part of the cultural fabric of modern society. Yet even after six decades of professional success, Williams continued to create, perform, and inspire.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">In 2016, he received the prestigious AFI Life Achievement Award, joining a select group of artists whose influence extends far beyond their own profession. The honor recognized not only his extraordinary body of work but also his role in shaping the emotional language of modern cinema. By this point, themes such as The Imperial March, Hedwig's Theme, Raiders March, and the Jurassic Park Theme had become instantly recognizable around the world.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2019</p>
                            <p class="section-text-small">Williams returned once again to the Star Wars universe with The Last Jedi (2017) and The Rise of Skywalker (2019). These scores demonstrated that, even after more than forty years with the franchise, he remained capable of introducing fresh ideas while honoring the musical traditions he had established decades earlier. The conclusion of the Skywalker Saga marked the end of one of the most significant composer-franchise collaborations in entertainment history.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2022</p>
                            <p class="section-text-small">The next major milestone came in 2022 with Steven Spielberg's The Fabelmans. As a semi-autobiographical story reflecting Spielberg's own childhood and artistic journey, the film required music of great intimacy and emotional sensitivity. Williams responded with one of the most elegant scores of his later years, earning yet another Academy Award nomination and extending a record that already placed him among the most nominated individuals in Oscar history.</p>
                            
                            <p class="section-date-small" style="margin-top: 2rem;">2023</p>
                            <p class="section-text-small">In 2023, Williams revisited another beloved franchise with Indiana Jones and the Dial of Destiny. More than forty years after first introducing audiences to the adventurous spirit of Indiana Jones, he once again demonstrated the melodic brilliance that had defined his entire career. The score served as both a celebration of the franchise and a reminder that his creative voice remained as distinctive as ever.</p>
                            <p class="section-text-small" style="margin-top: 1rem;">Today, Williams continues to be celebrated worldwide through concerts, retrospectives, recordings, documentaries, and academic studies. His music remains a living part of contemporary culture rather than merely a historical achievement. Few artists in any field have maintained such relevance across so many generations.</p>
                        </div>
                        <div class="split-right" style="background-color: transparent;">
                            <div style="width: 100%; height: 500px; background-color: rgba(0,0,0,0.05); border: 2px dashed #ccc; display: flex; align-items: center; justify-content: center; color: #888; font-family: 'Graphik', sans-serif; letter-spacing: 0.1em; text-transform: uppercase;">Photo Placeholder</div>
                        </div>
                    </div>
                </section>
            </div>
\;

const startMarker = '<aside class="bio-sidebar">';
const endMarker = '</main>';

const startIdx = content.indexOf(startMarker);
const endIdx = content.indexOf(endMarker);

if (startIdx !== -1 && endIdx !== -1) {
    const updated = content.substring(0, startIdx) + newContent + '        </div>\n    ' + content.substring(endIdx);
    fs.writeFileSync('d:/alanmenken/biography.html', updated, 'utf8');
    console.log('Successfully replaced content');
} else {
    console.log('Could not find markers');
}
