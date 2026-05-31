import cloudinary
import cloudinary.api
import re
import math

cloudinary.config(
    cloud_name='dir57w3tf',
    api_key='868429686139485',
    api_secret='Qv4V70O3vHUSJirawOFn1U1PKb0'
)

# Fetch images
res = cloudinary.api.resources(max_results=50, sort_by='created_at', direction='desc')
new_images = [r['public_id'] for r in res['resources'] if len(r['public_id']) > 100]

print(f"Total new images available: {len(new_images)}")

# We will use exactly 12 images to prevent overflowing the text height.
# Distribution across the 8 sections (0 to 7):
image_counts = [
    1, # 0: Summary
    1, # 1: Early Life
    1, # 2: Apprentice
    1, # 3: Spielberg
    2, # 4: Golden Era
    2, # 5: Legacy
    2, # 6: Summit
    2  # 7: Legend
]

total_needed = sum(image_counts)

# Evenly sample exactly 'total_needed' images from the 30 available
selected_images = []
for i in range(total_needed):
    idx = int(math.floor(i * len(new_images) / total_needed))
    selected_images.append(new_images[idx])

with open('biography.html', 'r', encoding='utf-8') as f:
    bio = f.read()

pattern = r'<div style="display: flex; flex-direction: column; gap: 20px;">.*?</div>'

def replacer(match):
    if not hasattr(replacer, 'section_idx'):
        replacer.section_idx = 0
        replacer.img_idx = 0
        
    num_images = image_counts[replacer.section_idx]
    
    html = '<div style="display: flex; flex-direction: column; gap: 20px;">\n'
    for _ in range(num_images):
        if replacer.img_idx < len(selected_images):
            img_id = selected_images[replacer.img_idx]
            html += f'    <img src="https://res.cloudinary.com/dir57w3tf/image/upload/{img_id}.png" style="width: 100%; height: auto; object-fit: cover; display: block; border-radius: 4px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);" alt="Biography Event">\n'
            replacer.img_idx += 1
    html += '</div>'
    
    replacer.section_idx += 1
    return html

new_bio = re.sub(pattern, replacer, bio, flags=re.DOTALL)

with open('biography.html', 'w', encoding='utf-8') as f:
    f.write(new_bio)

print("Biography updated with fewer, evenly sampled images.")
