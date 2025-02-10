# FilmAgent/README.md

# FilmAgent: Generating Unity-Compatible Prefabs

This document provides detailed instructions on how to generate Unity-compatible prefabs using the `PrefabGenerator` functionality in the FilmAgent framework. The generated prefabs can be seamlessly integrated into Unity for further development and visualization.

---

## 📖 Overview

The `PrefabGenerator` is a utility designed to convert finalized film scripts into Unity-compatible prefab data. This process involves extracting relevant information from the script, formatting it into a Unity-friendly structure, and saving it as a JSON file. The generated prefab data can then be imported into Unity to create dynamic scenes.

---

## 🚀 Steps to Generate Prefabs

Follow these steps to generate Unity-compatible prefabs:

### 1. **Prepare the Environment**

Ensure that the FilmAgent environment is set up correctly:
- Install all required dependencies by running:
  ```bash
  pip install -r requirements.txt
  ```
- Verify that the finalized script (`script.json`) is available in the `Script` directory.

### 2. **Run the Prefab Generator**

The `PrefabGenerator` class is responsible for generating the prefab data. To execute the prefab generation process:

1. Navigate to the FilmAgent directory:
   ```bash
   cd /path/to/FilmAgent
   ```

2. Run the `prefab_generator.py` script:
   ```bash
   python prefab_generator.py
   ```

3. The script will:
   - Read the finalized script from `Script/script.json`.
   - Extract scene, character, and action data.
   - Format the data into a Unity-compatible structure.
   - Save the output as `unity_prefabs.json` in the `Script` directory.

4. Upon successful execution, you will see a confirmation message:
   ```
   Unity prefab data generated and saved to /path/to/FilmAgent/Script/unity_prefabs.json
   ```

---

## 🎮 Integrating Prefabs into Unity

Once the prefab data is generated, follow these steps to integrate it into Unity:

### 1. **Import the Prefab Data**

1. Open your Unity project.
2. Copy the `unity_prefabs.json` file from the `Script` directory into your Unity project's `Assets` folder.

### 2. **Parse the Prefab Data**

Use a Unity script to parse the JSON file and create prefabs dynamically. Below is an example script:

```csharp
using UnityEngine;
using System.IO;

public class PrefabLoader : MonoBehaviour
{
    public string prefabDataPath = "Assets/unity_prefabs.json";

    void Start()
    {
        if (File.Exists(prefabDataPath))
        {
            string jsonData = File.ReadAllText(prefabDataPath);
            // Parse the JSON data and create prefabs
            Debug.Log("Prefab data loaded successfully.");
        }
        else
        {
            Debug.LogError("Prefab data file not found.");
        }
    }
}
```

### 3. **Visualize the Prefabs**

1. Attach the `PrefabLoader` script to a GameObject in your Unity scene.
2. Run the Unity project to visualize the prefabs.

---

## 🛠️ Customizing the Prefab Generation

The `PrefabGenerator` class can be customized to suit specific requirements. Key methods include:

- **`generate_prefabs()`**: Reads the script, extracts data, and formats it into Unity-compatible JSON.
- **`write_json()`**: Saves the formatted data to a file.

To modify the prefab structure, edit the `generate_prefabs` method in `FilmAgent/prefab_generator.py`.

---

## 📝 Example Script Structure

The `unity_prefabs.json` file contains structured data for Unity prefabs. Below is an example:

```json
[
    {
        "scene_information": "Scene 1: Introduction",
        "initial_position": [
            {"character": "John", "position": "Position 1"},
            {"character": "Alice", "position": "Position 2"}
        ],
        "dialogues": [
            {
                "speaker": "John",
                "content": "Welcome to the show!",
                "actions": ["Wave"],
                "shot": "Close-Up",
                "current_position": [{"character": "John", "position": "Position 1"}]
            }
        ]
    }
]
```

---

## 🔍 Troubleshooting

- **Error: Script file not found**  
  Ensure that the `script.json` file exists in the `Script` directory.

- **Error: Invalid JSON format**  
  Verify that the script file is correctly formatted as JSON.

- **Unity cannot parse prefab data**  
  Check the structure of `unity_prefabs.json` and ensure it matches Unity's requirements.

---

## 📚 Additional Resources

- [Unity JSON Serialization](https://docs.unity3d.com/Manual/JSONSerialization.html)
- [FilmAgent Documentation](https://github.com/HITsz-TMG/FilmAgent)

For further assistance, please refer to the FilmAgent repository or contact the development team.

---

## 🌟 Build Your own Film with FilmAgent

### For Windows 11 Users

1. Install Package
```cmd
conda create -n filmagent python==3.9.18
conda activate filmagent
pip install -r env.txt
```

2. Modify File Paths:
   - Replace all UNIX-style paths (e.g., `/path/to/`) in the scripts with Windows-style paths (e.g., `C:\path\to\`).
   - Example:
     ```python
     ROOT_PATH = "C:\\path\\to\\FilmAgent"
     ```

3. Ensure Compatibility:
   - Use double backslashes (`\\`) or raw strings (`r"C:\path\to\"`) in Python scripts to avoid escape sequence issues.
   - Update `.env` file paths accordingly.

4. Run the following commands to get the movie script created by the agents collaboratively:
```cmd
cd C:\path\to\FilmAgent
conda activate filmagent
python main.py
```

## 🌟 Generating Images for Video Sequences

This section provides a step-by-step guide to generate images for video sequences using the `image_generator.py` script.

### Prerequisites

1. **Install Required Packages**:
   Ensure you have installed the required Python packages as described in the "Build Your own Film with FilmAgent" section.

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

4. **Example Output**:
   - Below is an example of the generated images:
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

3. We use [ChatTTS](https://github.com/2noise/ChatTTS) to provide voice acting for the characters in the script. You need to download the [ChatTTS](https://github.com/2noise/ChatTTS) repository to the `TTS` directory. Then replace the absolute pathname with your specific Windows-style path in the `tts_main.py`. Run the following commands to deploy the text-to-speech service:
```cmd
cd C:\path\to\TTS
conda create -n tts python==3.9.18
conda activate tts
pip install -r tts_env.txt
python tts_main.py
```

4. Modify the `Script_path`, `actos_path`, `Audio_path`, and `url` in the `GenerateAudio.py` to use Windows-style paths. Run the following commands to get the audio files:
```cmd
cd C:\path\to\FilmAgent
conda activate filmagent
python GenerateAudio.py
```

## 🌟 Setting Up the ReactJS Frontend

To set up and run the ReactJS frontend application on Windows 11, follow these steps:

1. Navigate to the `client` directory:
   ```cmd
   cd client