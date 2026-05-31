import cloudinary
import cloudinary.api
import re

cloudinary.config(
    cloud_name='dir57w3tf',
    api_key='868429686139485',
    api_secret='Qv4V70O3vHUSJirawOFn1U1PKb0'
)

# Fetch images
res = cloudinary.api.resources(max_results=50, sort_by='created_at', direction='desc')
# The new images have very long random string IDs, typically > 50 characters.
# The user uploaded them recently, so they are at the top of the 'desc' list.
new_images = [r['public_id'] for r in res['resources'] if len(r['public_id']) > 100]

# If we fetched desc, let's reverse them so they are chronological (oldest to newest)
# Wait, if the user says "tahun 2010 keatas masukkin foto nya sudah tua", 
# it means the LAST sections should get the photos of him as an old man.
# If they uploaded a mix, and we sort by upload time (assuming they uploaded young photos first, then old photos last),
# then 'asc' (oldest upload to newest upload) would be young -> old.
# Let's just reverse the 'desc' list so it becomes 'asc'.
new_images.reverse()

print(f"Found {len(new_images)} new images.")

with open('biography.html', 'r', encoding='utf-8') as f:
    bio = f.read()

# Pattern to find the flex columns we inserted earlier
pattern = r'<div style="display: flex; flex-direction: column; gap: 20px;">.*?</div>'

def replacer(match):
    if not hasattr(replacer, 'index'):
        replacer.index = 0
    
    # We have 8 sections. 30 images / 8 sections = ~3.75 images per section.
    # Let's distribute them: some get 4, some get 3.
    # 8 * 3 = 24. So 6 sections get 4, 2 sections get 3.
    num_images = 4 if replacer.index < 6 else 3
    
    html = '<div style="display: flex; flex-direction: column; gap: 20px;">\n'
    for _ in range(num_images):
        if replacer.index_img < len(new_images):
            img_id = new_images[replacer.index_img]
            html += f'    <img src="https://res.cloudinary.com/dir57w3tf/image/upload/{img_id}.png" style="width: 100%; height: auto; object-fit: cover; display: block; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);" alt="Biography Event">\n'
            replacer.index_img += 1
    html += '</div>'
    
    replacer.index += 1
    return html

replacer.index = 0
replacer.index_img = 0

new_bio = re.sub(pattern, replacer, bio, flags=re.DOTALL)

with open('biography.html', 'w', encoding='utf-8') as f:
    f.write(new_bio)

print("Biography updated with new images.")
