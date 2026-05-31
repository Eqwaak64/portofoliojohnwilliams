import urllib.request
import threading
import time

urls = [
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161405/jaws_cut_cbxkzh.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161426/starwars_cut_edssz8.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161421/superman_cut_bmxfd6.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161420/et_cut_tqjchg.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161397/indianajones_cut_wpoqai.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161421/jurassicpark_cut_rtqsz8.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161388/schindlerlist_cut_gr7tzp.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161429/harrypotter_cut_eefn9w.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161369/homealone-cut_ratuyg.mp4",
    "https://res.cloudinary.com/dir57w3tf/video/upload/w_600,h_1000,c_fill,q_auto,f_auto/v1780161405/closeencounters_cut_zkooam.mp4"
]

def fetch_url(url):
    print(f"Starting {url}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=300) as resp:
            print(f"Done {url} - Status: {resp.status} - Size: {resp.headers['Content-Length']}")
    except Exception as e:
        print(f"Error {url}: {e}")

threads = []
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All prewarming requests finished.")
