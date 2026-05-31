import urllib.request
import urllib.parse
import re
import time
import os

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

def get_tmdb_backdrop(title):
    search_query = title
    if "Olympic" in title or "Concerto" in title or "Awards" in title or "Theme" in title or "Medal" in title or "Order" in title:
        return None
    
    query = urllib.parse.quote(search_query)
    url = f"https://www.themoviedb.org/search?query={query}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8')
        match = re.search(r'href="/movie/(\d+[^"]*)"', html)
        if match:
            movie_path = match.group(1)
            backdrop_url = f"https://www.themoviedb.org/movie/{movie_path}/images/backdrops"
            req2 = urllib.request.Request(backdrop_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            html2 = urllib.request.urlopen(req2, timeout=10).read().decode('utf-8')
            bg_matches = re.findall(r'href="(https://image.tmdb.org/t/p/original/[^"]+\.jpg)"', html2)
            if bg_matches:
                return bg_matches[0]
    except Exception as e:
        print(f"Error for {title}: {e}")
    return None

new_content = content
count = 0
for task in tasks:
    if "picsum.photos" not in task['current_bg']:
        continue # skip already processed
        
    print(f"Fetching: {task['clean_title']}")
    img_url = get_tmdb_backdrop(task['clean_title'])
    if img_url:
        old_tag = task['original_html']
        new_tag = f'<h2{task["prefix"]}data-bg="{img_url}"{task["suffix"]}>{task["inner_html"]}</h2>'
        new_content = new_content.replace(old_tag, new_tag)
        count += 1
        print(f" -> Found: {img_url}")
    else:
        print(" -> Not found.")
        
    time.sleep(1) # delay to avoid rate limit

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print(f"Done! Successfully updated {count} backgrounds with original movie backdrops.")
