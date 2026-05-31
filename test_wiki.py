import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://en.wikipedia.org/w/api.php?action=query&prop=pageimages&titles=Star_Wars_(film)|Jaws_(film)|E.T._the_Extra-Terrestrial|Raiders_of_the_Lost_Ark|Jurassic_Park_(film)&format=json&pithumbsize=1920"

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as response:
        data = json.loads(response.read().decode('utf-8'))
        pages = data['query']['pages']
        for page_id, page_info in pages.items():
            print(f"Title: {page_info.get('title')}")
            if 'thumbnail' in page_info:
                print(f"Image: {page_info['thumbnail']['source']}")
except Exception as e:
    print("Error:", e)
