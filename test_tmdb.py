import urllib.request
import urllib.parse
import re

def get_tmdb_backdrop(movie_name):
    query = urllib.parse.quote(movie_name)
    url = f"https://www.themoviedb.org/search?query={query}"
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Find first movie link: /movie/1234
        match = re.search(r'href="/movie/(\d+[^"]*)"', html)
        if match:
            movie_path = match.group(1)
            backdrop_url = f"https://www.themoviedb.org/movie/{movie_path}/images/backdrops"
            req2 = urllib.request.Request(backdrop_url, headers={'User-Agent': 'Mozilla/5.0'})
            html2 = urllib.request.urlopen(req2).read().decode('utf-8')
            # Find first original image path
            bg_match = re.search(r'href="(https://image.tmdb.org/t/p/original/[^"]+\.jpg)"', html2)
            if bg_match:
                return bg_match.group(1)
    except Exception as e:
        print(e)
    return None

print("Star Wars:", get_tmdb_backdrop("Star Wars"))
print("Jaws:", get_tmdb_backdrop("Jaws"))
