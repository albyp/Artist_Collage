import os
from PIL import Image, ImageDraw, ImageFont

ARTIST = "example"

def resize_and_crop(image, target_width, target_height):
    # Resize the image to fit the target size while maintaining aspect ratio
    image.thumbnail((target_width, target_height), Image.LANCZOS)

    # Calculate the cropping box (centered crop)
    left = (image.width - target_width) // 2
    top = (image.height - target_height) // 2
    right = (image.width + target_width) // 2
    bottom = (image.height + target_height) // 2

    return image.crop((left, top, right, bottom))


def create_artist_image(artist_name):
    # Paths based on the artist name
    folder_path = artist_name
    profile_img = os.path.join(folder_path, f"{artist_name}_pfp.jpg")
    id1_img = os.path.join(folder_path, f"{artist_name}_id1.jpg")
    id2_img = os.path.join(folder_path, f"{artist_name}_id2.jpg")
    text_file = os.path.join(folder_path, f"{artist_name}.txt")

    # Check if files exist
    if not all(os.path.exists(file) for file in [profile_img, id1_img, id2_img, text_file]):
        print(f"Error: Missing required files for {artist_name}")
        return
    
    # Create a new blank 1080x1080 image (dark grey background)
    img = Image.new('RGB', (1080, 1080), color=(50, 50, 50))

    # Open images
    profile = Image.open(profile_img)
    id1 = Image.open(id1_img)
    id2 = Image.open(id2_img)

    profile = resize_and_crop(profile, 540, 540)
    id1 = resize_and_crop(id1, 540, 540)
    id2 = resize_and_crop(id2, 540, 540)

    # Paste images into position
    img.paste(profile, (0, 0)) # Top-left
    img.paste(id1, (540, 0)) # Top-right
    img.paste(id2, (540, 540)) # Bottom-left

    # Add text from the .txt file to the bottom-right corner
    with open(text_file, 'r') as file:
        text = file.read()

    # Set up text drawing image
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", size=60)
    except IOError:
        font = ImageFont.load_default()
    
    # Get text size using textbbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Determine position for the text (bottom-right)
    text_x = 540 + (540 - text_width) // 2
    text_y = 540 + (540 - text_height) // 2

    # Draw text with color
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

    # Save or show the final image
    img.show()
    img.save(f"{artist_name}_collage.jpg")

if __name__ == '__main__':
    create_artist_image(ARTIST)
