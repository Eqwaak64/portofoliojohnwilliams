import cloudinary
import cloudinary.api

cloudinary.config(
    cloud_name="dir57w3tf",
    api_key="868429686139485",
    api_secret="Qv4V70O3vHUSJirawOFn1U1PKb0"
)

try:
    response = cloudinary.api.resources(resource_type="video", max_results=100)
    videos = response.get('resources', [])
    for v in videos:
        if 'long' in v['public_id'].lower():
            print(f"{v['public_id']} -> {v['secure_url']}")
except Exception as e:
    print(f"Error: {e}")
