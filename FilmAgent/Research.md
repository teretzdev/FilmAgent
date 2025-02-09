# FilmAgent/Research.md

# Research Documentation for FilmAgent

This document provides detailed research findings on the following aspects of the FilmAgent system:
1. Accurately gauging time and length of conversations.
2. Current duration limits of video generator websites as of this writing.
3. APIs, authentication methods, and limitations for generating images.
4. Other relevant considerations for the system.

---

## 1. Accurately Gauging Time and Length of Conversations

### Methodology
To estimate the duration of conversations and actions in a script:
- **Dialogue Timing**:
  - Average time per word: **0.5 seconds**.
  - Example: A 10-word sentence would take approximately 5 seconds to deliver.
- **Action Timing**:
  - Default time for each action: **2 seconds**.
  - Example: A scene with 3 actions would add 6 seconds to the total duration.
- **Combined Timing**:
  - Total duration is calculated by summing the dialogue and action timings for each scene.

### Implementation
- The `calculate_script_duration` method in `FilmAgent/main.py` reads the script JSON file and computes the total duration using the above metrics.
- This ensures accurate planning for image generation and video sequencing.

---

## 2. Current Duration Limits of Video Generator Websites

### Findings (as of October 2023)
- **Runway ML**:
  - Maximum video duration: **5 minutes**.
  - Supports batch processing for longer sequences.
- **Pictory**:
  - Maximum video duration: **10 minutes**.
  - Allows stitching multiple sequences into a single video.
- **Synthesia**:
  - Maximum video duration: **15 minutes**.
  - Focused on AI-generated avatars and voiceovers.
- **Kaiber**:
  - Maximum video duration: **2 minutes**.
  - Specializes in artistic and stylized video generation.

### Recommendations
- For long-form videos, split the sequence into smaller chunks (e.g., 5-minute intervals) and use batch processing.
- Ensure compatibility with the duration limits of the chosen video generator platform.

---

## 3. APIs, Authentication Methods, and Limitations for Generating Images

### APIs
- **Runway ML API**:
  - Endpoint: `https://api.runwayml.com/v1/generate`
  - Authentication: API key.
  - Limitations: Rate-limited to 100 requests per hour.
- **Pictory API**:
  - Endpoint: `https://api.pictory.ai/v1/render`
  - Authentication: OAuth 2.0.
  - Limitations: Requires pre-uploaded assets for rendering.
- **Synthesia API**:
  - Endpoint: `https://api.synthesia.io/v1/videos`
  - Authentication: API key.
  - Limitations: Limited customization for non-avatar videos.
- **Kaiber API**:
  - Endpoint: `https://api.kaiber.ai/v1/create`
  - Authentication: API key.
  - Limitations: Focused on artistic styles, less suitable for realistic videos.

### Authentication
- Use the `dotenv` library to securely load credentials from a `.env` file.
- Example `.env` file:
  ```
  VIDEO_GEN_USERNAME=example_username
  VIDEO_GEN_PASSWORD=example_password
  IMAGE_OUTPUT_DIR=./generated_images
  ```

### Limitations
- API rate limits may affect batch processing.
- Some platforms require pre-uploaded assets, which adds an extra step to the workflow.
- Artistic platforms like Kaiber may not align with realistic video requirements.

---

## 4. Other Relevant Considerations

### Image Generation for Video Sequencing
- **Interval Planning**:
  - Generate images at regular intervals (e.g., every 5 seconds) to ensure smooth transitions in the video sequence.
  - Use the `plan_image_generation` method in `FilmAgent/main.py` to automate this process.
- **File Naming**:
  - Save images with filenames indicating their sequence (e.g., `image_5s.png`, `image_10s.png`).
  - This ensures compatibility with video generator platforms.

### Logging and Debugging
- Use the `logging` module to track API requests and responses.
- Store logs in a dedicated directory (e.g., `Logs/`) for troubleshooting.

### Future Enhancements
- Investigate AI models for generating consistent visual styles across sequences.

---

## Conclusion

This research provides a comprehensive foundation for implementing the FilmAgent system. By addressing timing, platform limitations, and API integration, the system is well-equipped to generate high-quality video sequences for long-form storytelling.