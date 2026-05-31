import cloudinary
import cloudinary.api
import cloudinary.uploader
import sys

# Konfigurasi disesuaikan dengan cloudinary_test.py
cloudinary.config(
  cloud_name = "dir57w3tf",
  api_key = "868429686139485",
  api_secret = "Qv4V70O3vHUSJirawOFn1U1PKb0"
)

try:
    print("Fetching Cloudinary videos...")
    response = cloudinary.api.resources(resource_type="video", max_results=100)
    videos = response.get('resources', [])
    
    print("\n--- SMALL VIDEOS (< 10 MB) ---")
    for v in videos:
        size_mb = v['bytes'] / (1024 * 1024)
        if size_mb < 15: # Filter for sizes less than 15MB
            print(f"- Public ID: {v['public_id']}")
            print(f"  Size: {size_mb:.2f} MB")
            print(f"  URL: {v['secure_url']}")
            print("-" * 30)

except Exception as e:
    print(f"Error: {e}")
