import cloudinary
import cloudinary.api

cloudinary.config(
    cloud_name="dir57w3tf",
    api_key="868429686139485",
    api_secret="Qv4V70O3vHUSJirawOFn1U1PKb0",
    secure=True
)

try:
    print("Fetching videos from Cloudinary...")
    # Get up to 50 videos
    response = cloudinary.api.resources(resource_type="video", max_results=50)
    videos = response.get("resources", [])
    
    if not videos:
        print("No videos found in Cloudinary.")
    else:
        print(f"Found {len(videos)} videos:")
        for v in videos:
            print(f"- Public ID: {v['public_id']}")
            print(f"  Format: {v['format']}")
            print(f"  Size: {v.get('bytes', 0) / (1024*1024):.2f} MB")
            # Create q_auto URL
            optimized_url = v['secure_url'].replace('/upload/', '/upload/q_auto/')
            print(f"  URL (Optimized): {optimized_url}")
            print("")
except Exception as e:
    print(f"Error: {e}")
