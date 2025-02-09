# FilmAgent/Documentation/Features_Documentation.md

# Features Documentation for GTA Reality Show

This document outlines the features and capabilities of the system for planning scripts, episodes, seasons, and contestants for the GTA reality show. It includes sections like Seasons and Episodes, Contestants, Crowds and Voting, Prizes, Rules and Challenges, Film Crew and Cameraman, Script and Episode Planning Features, Integration of GTA Concepts, System Capabilities, and Generating Images for Long-Form Videos.

## Generating Images for Long-Form Videos

This section provides a detailed guide on generating images for long-form videos, ensuring they are labeled sequentially for easy integration into video generation workflows.

### Steps to Generate Images

1. **Run the Image Generator**:
   - Use the `image_generator.py` script to generate images based on the script.
   - Execute the following command:
     ```bash
     python FilmAgent/image_generator.py
     ```
   - Images will be saved in the directory specified by the `IMAGE_OUTPUT_DIR` environment variable.

2. **Export Images with Sequential Labels**:
   - The generated images are automatically labeled with their sequence index in the filename (e.g., `image_1.png`, `image_2.png`).
   - This ensures the images are ordered correctly for video generation.

3. **Verify Generated Images**:
   - Check the `generated_images` directory to ensure all images are created correctly.
   - Example filenames:
     - `image_1.png`: Represents the first frame in the sequence.
     - `image_2.png`: Represents the second frame in the sequence.

### Example Output

Below is an example of the generated images:
```
generated_images/
├── image_1.png
├── image_2.png
├── image_3.png
└── ...
```

### Case Scenarios and Results

#### Scenario 1: Generating Images for a Short Script
- **Script Duration**: 15 seconds
- **Image Interval**: 5 seconds
- **Generated Images**:
  ```
  generated_images/
  ├── image_1.png
  ├── image_2.png
  ├── image_3.png
  ```
- **Description**: The script contains three key timestamps, and the images are labeled sequentially.

#### Scenario 2: Generating Images for a Long Script
- **Script Duration**: 60 seconds
- **Image Interval**: 5 seconds
- **Generated Images**:
  ```
  generated_images/
  ├── image_1.png
  ├── image_2.png
  ├── image_3.png
  ├── image_4.png
  ├── image_5.png
  ├── image_6.png
  ├── image_7.png
  ├── image_8.png
  ├── image_9.png
  ├── image_10.png
  ├── image_11.png
  ├── image_12.png
  ```
- **Description**: The script spans a minute, and twelve images are generated at 5-second intervals.

### Additional Notes

- **API Rate Limits**:
  Be mindful of API rate limits when using video generator platforms. Refer to the `Research.md` file for details on platform-specific limitations.

- **Future Enhancements**:
  In future phases, we plan to integrate Unity for VR experiences and automate video generation directly within FilmAgent.