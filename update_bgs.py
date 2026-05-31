import re
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from duckduckgo_search import DDGS

bg_dir = "d:/alanmenken/assets/img/bg"
if not os.path.exists(bg_dir):
    os.makedirs(bg_dir)

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

def fetch_and_download(task):
    title = task['clean_title']
    query = f"{title} movie wallpaper 1920x1080"
    if "Olympic" in title or "Medal" in title or "Awards" in title or "Concerto" in title:
        query = f"John Williams {title} wallpaper 1920x1080"
        
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '', title.replace(' ', '_')) + ".jpg"
    local_path_rel = f"assets/img/bg/{safe_name}"
    local_path_abs = os.path.join(bg_dir, safe_name)
    
    # If already downloaded, just return it
    if os.path.exists(local_path_abs) and os.path.getsize(local_path_abs) > 10000:
        return task, local_path_rel
        
    try:
        with DDGS() as ddgs:
            results = list(ddgs.images(
                query,
                region="wt-wt",
                safesearch="moderate",
                size="Wallpaper",
                max_results=3
            ))
            if results:
                for res in results:
                    img_url = res['image']
                    try:
                        req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req, timeout=5) as response, open(local_path_abs, 'wb') as out_file:
                            out_file.write(response.read())
                        return task, local_path_rel
                    except Exception as e:
                        continue
    except Exception as e:
        pass
    return task, None

new_content = content
count = 0
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(fetch_and_download, tasks)
    for task, local_path_rel in results:
        if local_path_rel:
            old_tag = task['original_html']
            new_tag = f'<h2{task["prefix"]}data-bg="{local_path_rel}"{task["suffix"]}>{task["inner_html"]}</h2>'
            new_content = new_content.replace(old_tag, new_tag)
            count += 1
            print(f"Downloaded: {task['clean_title']}")

with open('d:/alanmenken/work.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print(f"Done! Successfully updated {count} backgrounds locally.")
