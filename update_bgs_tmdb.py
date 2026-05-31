import urllib.request
import urllib.parse
import re
import os
from concurrent.futures import ThreadPoolExecutor

with open('d:/alanmenken/work.html', 'r', encoding='utf-8') as f:
    content = f.read()

matches = re.findall(r'<h2([^>]*)data-bg="([^"]*)"([^>]*)>(.*?)</h2>', content)

def get_clean_title(html_title):
    t = re.sub(r'<[^>]*>', '', html_title)
    return t.strip()

tasks = []
for m in matches:
    clean_title = get_clean_title(m[3])
    tasks.append({
        'original_html': f'<h2{m[0]}data-bg="{m[1]}"{m[2]}>{m[3]}</h2>',
        'clean_title': clean_title,
        'prefix': m[0],
        'suffix': m[2],
        'inner_html': m[3],
        'current_bg': m[1]
    })

print(f"Found {len(tasks)} titles to process.")

def get_tmdb_backdrop(title):
    # Some specific searches for tricky titles
    search_query = title
    if "Olympic" in title or "Concerto" in title or "Awards" in title or "Theme" in title:
        return None # Skip non-movies
    
    query = urllib.parse.quote(search_query)
    url = f"https://www.themoviedb.org/search?query={query}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, timeout=5).read().decode('utf-8')
        match = re.search(r'href="/movie/(\d+[^"]*)"', html)
        if match:
            movie_path = match.group(1)
            backdrop_url = f"https://www.themoviedb.org/movie/{movie_path}/images/backdrops"
            req2 = urllib.request.Request(backdrop_url, headers={'User-Agent': 'Mozilla/5.0'})
            html2 = urllib.request.urlopen(req2, timeout=5).read().decode('utf-8')
            # Find all original image paths and pick the first one
            bg_matches = re.findall(r'href="(https://image.tmdb.org/t/p/original/[^"]+\.jpg)"', html2)
            if bg_matches:
                return bg_matches[0]
    except Exception as e:
        pass
    return None

def process_task(task):
    img_url = get_tmdb_backdrop(task['clean_title'])
    if img_url:
        return task, img_url
    return task, None

new_content = content
count = 0
# Use 5 workers to be polite to TMDB
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(process_task, tasks)
    for task, img_url in results:
        if img_url:
            old_tag = task['original_html']
            new_tag = f'<h2{task["prefix"]}data-bg="{img_url}"{task["suffix"]}>{task["inner_html"]}</h2>'
            new_content = new_content.replace(old_tag, new_tag)
            count += 1
            print(f"Found bg for: {task['clean_title']}")

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print(f"Done! Successfully updated {count} backgrounds with original movie backdrops.")
