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
