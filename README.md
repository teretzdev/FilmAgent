<p align="center">
    <img src="pics/cover_page.jpg" width="300" style="margin-bottom: 0.2;"/>
<p>

<h2 align="center"> <a href="https://github.com/HITsz-TMG/FilmAgent">FilmAgent: A Multi-Agent Framework for End-to-End Film Automation in Virtual 3D Spaces</a></h2>
<!-- <h5 align="center"> If you like our project, please consider giving us a star ⭐ on GitHub to stay updated with the latest developments.  </h2> -->
<h4 align="center">

<div align="center">
<img src="https://img.shields.io/badge/Version-1.0.0-blue.svg" alt="Version"> 
<img src="https://img.shields.io/badge/License-Apache%202.0-green.svg" alt="License">
<img src="https://img.shields.io/github/stars/HITsz-TMG/FilmAgent?color=yellow" alt="Stars">
<img src="https://img.shields.io/github/issues/HITsz-TMG/FilmAgent?color=red" alt="Issues">
<img src="https://img.shields.io/badge/python-3.8-purple.svg" alt="Python">

<!-- <img src="https://img.shields.io/github/stars/AIDC-AI/Marco-o1?color=yellow" alt="Stars"> -->

<!-- [![Project Page](https://img.shields.io/badge/Project_Page-FilmAgent-blue)](https://filmagent.github.io/)
[![Project Page](https://img.shields.io/badge/Paper-Arxiv-yellow)](https://arxiv.org/abs/2501.12909)
[![Project Page](https://img.shields.io/badge/Video-Youtube-red)](https://www.youtube.com/watch?v=hTI-0777iHU)
![Gitea Stars](https://img.shields.io/gitea/stars/HITsz-TMG/FilmAgent) -->

</h4>

<div align="center">

<!-- **Affiliations:** -->

_**Zhenran Xu, Longyue Wang, Jifang Wang, Zhouyi Li, Senbao Shi, Xue Yang, Yiyu Wang, Baotian Hu, Jun Yu, Min Zhang**_

🎯  [**Project Page**](https://filmagent.github.io)  :octocat:  [**Code**](https://github.com/HITsz-TMG/FilmAgent)  📝  [**Paper**](https://arxiv.org/abs/2501.12909) 🧑‍💻  [**Slides**](https://filmagent.github.io/static/SA24_FilmAgent.pdf)  📽️  [**Video**](https://www.youtube.com/watch?v=hTI-0777iHU)

</div>

#

**FilmAgent** is a multi-agent collaborative system for end-to-end film automation in 3D virtual spaces. 
FilmAgent simulates key crew roles—directors, screenwriters, actors, and cinematographers, and integrates efficient human workflows within a sandbox environment.

<div align=center><img src="https://github.com/HITsz-TMG/FilmAgent/blob/main/pics/intro.png" height="100%" width="85%"/></div>

## 🚀 Framework

Following the traditional film studio workflow, we divide the whole film automation process into three sequential stages: idea development, scriptwriting and cinematography, and apply the **Critique-Correct-Verify**, **Debate-Judge** collaboration strategies. After these stages, each line in the script is specified with the positions of the actors, their actions, their dialogue, and the chosen camera shots.

<div align=center><img src="https://github.com/HITsz-TMG/FilmAgent/blob/main/pics/framework.png" height="100%" width="85%"/></div>

## 🌟 Build Your own Film with FilmAgent

### Quickstart for Windows Users

For Windows-specific installation and setup instructions, please refer to the [**QUICKSTART-WINDOWS.md**](./QUICKSTART-WINDOWS.md) guide. This document provides a detailed step-by-step guide tailored for Windows environments.
```

## 🌟 Generating Images and Video Sequences

This section provides a detailed guide to generate images and video sequences using FilmAgent. It includes instructions for exporting images with sequential labels and showcases examples for various scenarios.

### Prerequisites

1. **Install Required Packages**:
   Ensure you have installed the required Python packages as described in the general installation instructions.

2. **Set Up Environment Variables**:
   - Create a `.env` file in the `FilmAgent` directory or use the provided `.env.example` file as a template.
   - Configure the following variables:
     ```env
     IMAGE_OUTPUT_DIR=./generated_images
     FONT_PATH=/path/to/font.ttf
     SCRIPT_PATH=./script.json
     IMAGE_INTERVAL=5
     ```

3. **Prepare the Script**:
   - Ensure you have a valid `script.json` file in the `FilmAgent` directory. This file contains the script details for generating images.

---

### Steps to Generate Images

1. **Run the Image Generator**:
   Execute the following command to generate images based on the script:
   ```bash
   python FilmAgent/image_generator.py
   ```
   - The images will be saved in the directory specified by the `IMAGE_OUTPUT_DIR` environment variable.
   - Each image will represent a specific timestamp in the script, spaced by the interval defined in `IMAGE_INTERVAL`.

2. **Export Images with Sequential Labels**:
   - The generated images will be automatically labeled with their sequence index in the filename (e.g., `image_1.png`, `image_2.png`).
   - This ensures the images are ordered correctly for video generation.

3. **Verify Generated Images**:
   - Check the `generated_images` directory to ensure all images are created correctly.
   - Example filenames:
     - `image_1.png`: Represents the first frame in the sequence.
     - `image_2.png`: Represents the second frame in the sequence.

---

### Example Scenarios and Results

#### Scenario 1: Short Script
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

#### Scenario 2: Long Script
- **Script Duration**: 60 seconds
- **Image Interval**: 10 seconds
- **Generated Images**:
  ```
  generated_images/
  ├── image_1.png
  ├── image_2.png
  ├── image_3.png
  ├── image_4.png
  ├── image_5.png
  ├── image_6.png
  ```
- **Description**: The script spans a minute, and six images are generated at 10-second intervals.

#### Scenario 3: Edge Cases
- **Zero Duration**: No images are generated.
- **Very Short Interval**: One image per second is generated.
- **Interval Longer than Duration**: No images are generated.

---

### Steps to Generate Video Sequences

1. **Upload Images to Video Generator**:
   - Use the video generator platform's API or web interface to upload the generated images.
   - Follow the platform's guidelines for creating video sequences.

2. **Configure Video Settings**:
   - Set the desired frame rate, resolution, and other video settings as per the platform's options.

3. **Generate and Download Video**:
   - Initiate the video generation process on the platform.
   - Once completed, download the video file to your local system.

### Steps to Generate Video Sequences

1. **Log into Video Generator Platform**:
   - Ensure your `.env` file contains valid credentials for the video generator platform.
   - The `login_to_video_generator` method in `FilmAgent/main.py` will handle authentication.

2. **Run Unit Tests for Image Generation**:
   - To verify the correctness of the image generation process, run the unit tests provided in the `FilmAgent/tests/test_image_generator.py` file.
   - Use the following command to execute the tests:
     ```bash
     pytest FilmAgent/tests/test_image_generator.py
     ```
   - These tests ensure that:
     - The output directory is created correctly.
     - Images are generated with the correct text and filenames.
     - Edge cases (e.g., zero duration, very short intervals) are handled properly.
   - Running these tests is crucial to validate the functionality and reliability of the image generation module.

3. **Upload Images to Video Generator**:
   - Use the video generator platform's API or web interface to upload the generated images.
   - Follow the platform's guidelines for creating video sequences.

3. **Configure Video Settings**:
   - Set the desired frame rate, resolution, and other video settings as per the platform's options.

4. **Generate and Download Video**:
   - Initiate the video generation process on the platform.
   - Once completed, download the video file to your local system.

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
- **Image Interval**: 10 seconds
- **Generated Images**:
  ```
  generated_images/
  ├── image_1.png
  ├── image_2.png
  ├── image_3.png
  ├── image_4.png
  ├── image_5.png
  ├── image_6.png
  ```
- **Description**: The script spans a minute, and six images are generated at 10-second intervals.

### Additional Notes

- **API Rate Limits**:
  Be mindful of API rate limits when using video generator platforms. Refer to the `Research.md` file for details on platform-specific limitations.

- **Future Enhancements**:
  In future phases, we plan to integrate Unity for VR experiences and automate video generation directly within FilmAgent.
```

2. Create `Script` and `Logs` folders in the Filmagent directory, then replace the absolute pathname '/path/to/' with your specific path and modify the `topic` in the `main.py`. Modify the api_key and organization number in `LLMCaller.py`. Run the following commands to get the movie script created by the agents collaboratively:
```bash
cd /path/to/FilmAgent
conda activate filmagent
python main.py
```

3. We use [ChatTTS](https://github.com/2noise/ChatTTS) to provide voice acting for the characters in the script. You need to download the [ChatTTS](https://github.com/2noise/ChatTTS) repository to the `TTS` directory. Then replace the absolute pathname '/path/to/' with your specific path in the `tts_main.py`. Run the following commands to deploy the text-to-speech service:
```bash
cd /path/to/TTS
conda create -n tts python==3.9.18
conda activate tts
pip install -r tts_env.txt
python tts_main.py
```

4. Modify the `Script_path`, `actos_path`, `Audio_path` and `url` in the `GenerateAudio.py`. Run the following commands to get the audio files:
```bash
cd /path/to/FilmAgent
conda activate filmagent
python GenerateAudio.py
```

<REMOVE ENTIRE SECTION>

5. For the tests on 15 topics in our experimental section, we provide three .py files: `test_full.py` (The full FilmAgent framework, utilizing multi-agent collaboration.), `test_no_interation.py` (A single agent is responsible for planning, scriptwriting, and cinematography, representing our FilmAgent framework without multi-agent collaboration algorithms.) and `test_cot.py` (A single agent generates the chain-of-thought rationale and the complete script).

## 🌟 Setting Up the ReactJS Frontend

To set up and run the ReactJS frontend application, follow these steps:

1. Navigate to the `client` directory:
   ```bash
   cd client
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

   This will start the ReactJS application, and it will be accessible at `http://localhost:3000` in your web browser.

4. To build the application for production, run:
   ```bash
   npm run build
   ```

   The production-ready files will be available in the `client/build` directory.

## 🌈 Case Study

### What does Multi-Agent Collaboration do?
The following table records some comparisons of the scripts and camera settings before (left) and after (right) multi-agent collaboration, with excerpts from their discussion process.

<div align=center><img src="https://github.com/HITsz-TMG/FilmAgent/blob/main/pics/cases.png" height="100%" width="70%"/></div>

Case #1 and #2 are from the Critique-Correct-Verify method in Scriptwriting #2 and #3 stages respectively. Case #3 and #4 are from the Debate-Judge method in Cinematography.
- **Case #1** shows that Director-Screenwriter discussion reduces hallucinations in non-existent actions (e.g., standing suggest), enhances plot coherence, and ensures consistency across scenes.
- **Case #2** shows that Actor-Director-Screenwriter discussion improves the alignment of dialogue with character profiles.
- **Case #3**, in the Debate-Judge method in cinematography, demonstrates the correction of an inappropriate dynamic shot, which is replaced with a medium shot to better convey body language.
- **Case #4** replaces a series of identical static shots with a mix of dynamic and static shots, resulting in a more diverse camera setup.

### Comparison with Sora

<div align=center><img src="https://github.com/HITsz-TMG/FilmAgent/blob/main/pics/sora.png" height="100%" width="70%"/></div>



https://github.com/user-attachments/assets/65bb4c12-cba0-4ee9-a673-63ea5103fd76



While Sora (the above video ⏫) shows great adaptability to diverse locations, characters and shots, it **struggles with consistency and narrative delivery**, along with **strange artifacts**. 

In contrast, FilmAgent requires pre-built 3D spaces, but it produces **coherent, physics-compliant** videos with strong **storytelling capabilities** (video at [Youtube](https://www.youtube.com/watch?v=yOOycdfolFY)).


## 📚 Citation

If you find FilmAgent useful for your research and applications, please cite using this BibTeX:
```bibtex
@misc{xu2025filmagent,
      title={FilmAgent: A Multi-Agent Framework for End-to-End Film Automation in Virtual 3D Spaces}, 
      author={Zhenran Xu and Longyue Wang and Jifang Wang and Zhouyi Li and Senbao Shi and Xue Yang and Yiyu Wang and Baotian Hu and Jun Yu and Min Zhang},
      year={2025},
      eprint={2501.12909},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.12909}, 
}
```