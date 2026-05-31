import cloudinary
import cloudinary.uploader
import cloudinary.api

# 1. Configure Cloudinary
# ← replace this (if you need to use placeholders: YOUR_CLOUD_NAME, YOUR_API_KEY, YOUR_API_SECRET)
cloudinary.config(
    cloud_name="dir57w3tf",
    api_key="868429686139485",
    api_secret="Qv4V70O3vHUSJirawOFn1U1PKb0",
    secure=True
)

print("--- Uploading an image ---")
# 2. Upload an image
upload_result = cloudinary.uploader.upload(
    "https://res.cloudinary.com/demo/image/upload/v1312461204/sample.jpg", 
    public_id="my_sample_image"
)
print(f"Secure URL: {upload_result['secure_url']}")
print(f"Public ID: {upload_result['public_id']}")

print("\n--- Image Details ---")
# 3. Get image details
print(f"Width: {upload_result['width']}px")
print(f"Height: {upload_result['height']}px")
print(f"Format: {upload_result['format']}")
print(f"File size: {upload_result['bytes']} bytes")

print("\n--- Transforming the image ---")
# 4. Transform the image
# f_auto: Automatically selects the most efficient image format based on the browser/device.
# q_auto: Automatically optimizes the image quality to reduce file size without visible degradation.
transformed_url, options = cloudinary.utils.cloudinary_url(
    "my_sample_image",
    fetch_format="auto",
    quality="auto"
)

print("Done! Click link below to see optimized version of the image. Check the size and the format.")
print(transformed_url)
