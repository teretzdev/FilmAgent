import os
from typing import List
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
OUTPUT_DIR = os.getenv("IMAGE_OUTPUT_DIR", "./generated_images")
FONT_PATH = os.getenv("FONT_PATH", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
FONT_SIZE = 24

def create_output_directory():
    """
    Ensure the output directory exists.
    """
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generate_image_with_text(text: str, filename: str):
    """
    Generate an image with the given text and save it to the specified filename.

    Args:
        text (str): The text to display on the image.
        filename (str): The filename to save the image as.
    """
    # Image dimensions
    width, height = 800, 600
    background_color = (255, 255, 255)  # White background
    text_color = (0, 0, 0)  # Black text

    # Create a blank image
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Load font
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        raise RuntimeError(f"Font not found at {FONT_PATH}. Please ensure the font path is correct.")

    # Calculate text position
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Draw text on the image
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # Save the image
    image.save(filename)

def generate_images_from_script(script_path: str, interval: int = 5) -> List[str]:
    """
    Generate images based on the script at specified intervals.

    Args:
        script_path (str): Path to the script JSON file.
        interval (int): Time interval in seconds between images.

    Returns:
        List[str]: List of filenames for the generated images.
    """
    import json

    # Read the script
    with open(script_path, "r") as file:
        script = json.load(file)

    # Calculate total duration and number of images
    total_duration = sum(scene.get("duration", 0) for scene in script)
    num_images = total_duration // interval

    # Generate images
    image_filenames = []
    for i in range(num_images):
        timestamp = i * interval
        text = f"Timestamp: {timestamp}s"
        filename = os.path.join(OUTPUT_DIR, f"image_{timestamp}s.png")
        generate_image_with_text(text, filename)
        image_filenames.append(filename)

    return image_filenames

if __name__ == "__main__":
    # Example usage
    create_output_directory()
    script_path = os.getenv("SCRIPT_PATH", "./script.json")
    interval = int(os.getenv("IMAGE_INTERVAL", 5))

    try:
        generated_images = generate_images_from_script(script_path, interval)
        print(f"Generated images: {generated_images}")
    except Exception as e:
        print(f"Error: {e}")
