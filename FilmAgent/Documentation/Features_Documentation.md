# FilmAgent/Documentation/Features_Documentation.md

# Features Documentation for GTA Reality Show

This document outlines the features and capabilities of the system for planning scripts, episodes, seasons, and contestants for the GTA reality show. It includes sections like Seasons and Episodes, Contestants, Crowds and Voting, Prizes, Rules and Challenges, Film Crew and Cameraman, Script and Episode Planning Features, Integration of GTA Concepts, and System Capabilities.

## Generating Images for Longform Videos

The `GTARealityShow` class now includes functionality to generate images for longform videos. These images are exported with labels clearly showing their sequence index, making them suitable for creating video sequences.

### Prerequisites

1. **Install Required Libraries**:
   Ensure the following Python libraries are installed:
   - `Pillow` (for image generation)
   - `os` (for file handling)

   Install them using:
   ```bash
   pip install pillow
   ```

2. **Set Up Output Directory**:
   - Images will be saved in the `Generated_Images` directory under the root path of the project.
   - Ensure the directory exists or will be created automatically by the script.

### Steps to Generate Images

1. **Initialize the `GTARealityShow` Class**:
   - Create an instance of the `GTARealityShow` class with the desired season name and number of episodes.
   - Example:
     ```python
     from FilmAgent.episodes import GTARealityShow

     gta_show = GTARealityShow(season_name="GTA_Season_1", episodes_per_season=10)
     ```

2. **Generate a Season**:
   - Call the `generate_season()` method to create episodes and generate images for each episode.
   - Example:
     ```python
     gta_show.generate_season()
     ```

3. **Verify Generated Images**:
   - Images will be saved in the `Generated_Images` directory with filenames like `image_001.png`, `image_002.png`, etc.
   - Each filename includes a sequential index to indicate its order in the storyline.

### Using Images for Video Creation

1. **Sequence the Images**:
   - The images are labeled with sequential indices (e.g., `image_001.png`, `image_002.png`), making it easy to use them in order for video creation.

2. **Create a Video**:
   - Use video editing software or Python libraries like `moviepy` to combine the images into a video.
   - Example using `moviepy`:
     ```python
     from moviepy.editor import ImageSequenceClip

     image_folder = "./Generated_Images"
     fps = 24  # Frames per second

     # Get list of image files in sequence
     image_files = [f"{image_folder}/image_{i:03d}.png" for i in range(1, total_images + 1)]

     # Create video
     clip = ImageSequenceClip(image_files, fps=fps)
     clip.write_videofile("output_video.mp4", codec="libx264")
     ```

3. **Adjust Video Settings**:
   - Configure frame rate, resolution, and other settings as needed.

### Notes

- Ensure the `GTARealityShow` class is properly configured with contestants, locations, and unique purposes for episodes.
- The generated images can be used for previews, promotional content, or as part of a larger video production pipeline.