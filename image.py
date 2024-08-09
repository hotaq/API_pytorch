import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dsui0fihb", 
    api_key = "661786462415869", 
    api_secret = "bENRCD3vp1pCnwuoHuV3kBKSSpE", # Click 'View Credentials' below to copy your API secret
    secure=True
)

# Upload an image
upload_result = cloudinary.uploader.upload("/Users/hootoo/Downloads/teachable_docker/1.jpg",
                                           public_id="shoes")
print(upload_result["secure_url"])

# Optimize delivery by resizing and applying auto-format and auto-quality
optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
print(optimize_url)

# Transform the image: auto-crop to square aspect_ratio
auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
print(auto_crop_url)