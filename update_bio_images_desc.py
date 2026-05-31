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
# Get the 30 new images (long IDs)
new_images = [r['public_id'] for r in res['resources'] if len(r['public_id']) > 100]

# Do NOT reverse. Use 'desc' order. 
# Newest uploads go to Early Life (top of page). Oldest uploads go to Living Legend (bottom of page).
print(f"Found {len(new_images)} new images. Not reversing this time.")

with open('biography.html', 'r', encoding='utf-8') as f:
    bio = f.read()

pattern = r'<div style="display: flex; flex-direction: column; gap: 20px;">.*?</div>'

def replacer(match):
    if not hasattr(replacer, 'index'):
        replacer.index = 0
    
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

print("Biography updated with desc images.")
