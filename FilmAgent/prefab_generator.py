import os
import json
from util import read_json, write_json

ROOT_PATH = "/absolute/path/to/FilmAgent"

class PrefabGenerator:
    """
    A class to generate Unity-compatible prefab data from the finalized script.
    """

    def __init__(self, script_path: str, output_path: str):
        """
        Initialize the PrefabGenerator with paths for the script and output.

        :param script_path: Path to the finalized script JSON file.
        :param output_path: Path to save the generated prefab data.
        """
        self.script_path = script_path
        self.output_path = output_path

    def generate_prefabs(self):
        """
        Generate Unity-compatible prefab data from the finalized script.

        This method reads the finalized script JSON file, extracts relevant
        information (e.g., characters, positions, actions, shots), and formats
        it into a structure suitable for Unity prefab creation.

        The formatted data is saved as a JSON file for Unity integration.
        """
        # Load the finalized script
        script = read_json(self.script_path)

        # Prepare prefab data structure
        prefab_data = []
        for scene in script:
            scene_data = {
                "scene_information": scene["scene information"],
                "initial_position": scene["initial position"],
                "dialogues": []
            }
            for dialogue in scene["scene"]:
                dialogue_data = {
                    "speaker": dialogue.get("speaker", ""),
                    "content": dialogue.get("content", ""),
                    "actions": dialogue.get("actions", []),
                    "shot": dialogue.get("shot", ""),
                    "current_position": dialogue.get("current position", [])
                }
                if "move" in dialogue:
                    dialogue_data["move"] = dialogue["move"]
                scene_data["dialogues"].append(dialogue_data)
            prefab_data.append(scene_data)

        # Save prefab data to a JSON file
        write_json(self.output_path, prefab_data)
        print(f"Unity prefab data generated and saved to {self.output_path}")


if __name__ == "__main__":
    # Define paths
    script_path = os.path.join(ROOT_PATH, "Script", "script.json")
    output_path = os.path.join(ROOT_PATH, "Script", "unity_prefabs.json")

    # Generate prefabs
    generator = PrefabGenerator(script_path, output_path)
    generator.generate_prefabs()
```

### Step 4: Review the code
- **Functionality**:
  - The `PrefabGenerator` class reads the finalized script JSON file.
  - It extracts relevant data (scene information, initial positions, dialogues, actions, shots).
  - It formats the data into a Unity-compatible structure and saves it as a JSON file.
- **Conventions**:
  - The code uses `read_json` and `write_json` utilities, consistent with the codebase.
  - Paths are constructed using `os.path.join`, ensuring cross-platform compatibility.
- **Completeness**:
  - The implementation is complete and functional.
  - It includes a `__main__` block for standalone execution.

### Final Output
```
import os
import json
from util import read_json, write_json

ROOT_PATH = "/absolute/path/to/FilmAgent"

class PrefabGenerator:
    """
    A class to generate Unity-compatible prefab data from the finalized script.
    """

    def __init__(self, script_path: str, output_path: str):
        """
        Initialize the PrefabGenerator with paths for the script and output.

        :param script_path: Path to the finalized script JSON file.
        :param output_path: Path to save the generated prefab data.
        """
        self.script_path = script_path
        self.output_path = output_path

    def generate_prefabs(self):
        """
        Generate Unity-compatible prefab data from the finalized script.

        This method reads the finalized script JSON file, extracts relevant
        information (e.g., characters, positions, actions, shots), and formats
        it into a structure suitable for Unity prefab creation.

        The formatted data is saved as a JSON file for Unity integration.
        """
        # Load the finalized script
        script = read_json(self.script_path)

        # Prepare prefab data structure
        prefab_data = []
        for scene in script:
            scene_data = {
                "scene_information": scene["scene information"],
                "initial_position": scene["initial position"],
                "dialogues": []
            }
            for dialogue in scene["scene"]:
                dialogue_data = {
                    "speaker": dialogue.get("speaker", ""),
                    "content": dialogue.get("content", ""),
                    "actions": dialogue.get("actions", []),
                    "shot": dialogue.get("shot", ""),
                    "current_position": dialogue.get("current position", [])
                }
                if "move" in dialogue:
                    dialogue_data["move"] = dialogue["move"]
                scene_data["dialogues"].append(dialogue_data)
            prefab_data.append(scene_data)

        # Save prefab data to a JSON file
        write_json(self.output_path, prefab_data)
        print(f"Unity prefab data generated and saved to {self.output_path}")


if __name__ == "__main__":
    # Define paths
    script_path = os.path.join(ROOT_PATH, "Script", "script.json")
    output_path = os.path.join(ROOT_PATH, "Script", "unity_prefabs.json")

    # Generate prefabs
    generator = PrefabGenerator(script_path, output_path)
    generator.generate_prefabs()
