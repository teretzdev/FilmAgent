from fastapi import FastAPI, HTTPException
from typing import List, Dict, Optional
import os
import json

def simulate_script_generation(prompt: str) -> Dict:
    """
    Simulate script generation based on a text prompt.

    Args:
        prompt (str): The text prompt.

    Returns:
        Dict: The generated script.
    """
    return {"script": f"Generated script for prompt: {prompt}"}

def simulate_image_generation(script_path: str) -> str:
    """
    Simulate image generation based on a script file.

    Args:
        script_path (str): Path to the script file.

    Returns:
        str: Path to the directory containing generated images.
    """
    output_dir = "./generated_images"
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
from pathlib import Path

# Initialize FastAPI app
app = FastAPI()

# Mock data paths (replace with actual paths in production)
SCRIPTS_PATH = "FilmAgent/scripts.json"
EPISODES_PATH = "FilmAgent/episodes.json"

# Utility function to load JSON data
def load_json(file_path: str) -> List[Dict]:
    try:
        if not Path(file_path).exists():
            return []
        with open(file_path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON data in file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading file: {str(e)}")

# Load scripts and episodes data
scripts_data = load_json(SCRIPTS_PATH)
episodes_data = load_json(EPISODES_PATH)

@app.get("/")
def root():
    return {"message": "Welcome to the FilmAgent API!"}

@app.post("/api/generate-script")
async def generate_script(prompt: Dict[str, str]):
    """
    Generate a script based on the provided text prompt.

    Args:
        prompt (Dict[str, str]): A dictionary containing the text prompt.

    Returns:
        JSON: The generated script or an error message.
    """
    try:
        if "prompt" not in prompt:
            raise HTTPException(status_code=400, detail="Missing 'prompt' in request body.")
        
        # Simulate script generation logic
        generated_script = {"script": f"Generated script for prompt: {prompt['prompt']}"}
        return generated_script
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating script: {str(e)}")

# Endpoint to fetch all scripts
@app.get("/scripts", response_model=List[Dict])
def get_all_scripts():
    if not scripts_data:
        raise HTTPException(status_code=404, detail="No scripts found.")
    return scripts_data

@app.post("/api/generate-images")
async def generate_images(file: Dict[str, str]):
    """
    Generate images based on the provided script file.

    Args:
        file (Dict[str, str]): A dictionary containing the script file path.

    Returns:
        JSON: The status and location of the generated images or an error message.
    """
    try:
        if "script_path" not in file:
            raise HTTPException(status_code=400, detail="Missing 'script_path' in request body.")
        
        # Simulate image generation logic
        image_output_dir = "./generated_images"
        return {"status": "success", "output_dir": image_output_dir}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating images: {str(e)}")

# Endpoint to fetch a specific script by ID
@app.get("/scripts/{script_id}", response_model=Dict)
async def get_script_by_id(script_id: int) -> Dict:
    try:
        scripts = load_json(SCRIPTS_PATH)
        script = next((s for s in scripts if s.get("id") == script_id), None)
        if not script:
            raise HTTPException(status_code=404, detail=f"Script with ID {script_id} not found")
        return script
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to fetch all episodes
@app.get("/episodes", response_model=List[Dict])
def get_all_episodes():
    if not episodes_data:
        raise HTTPException(status_code=404, detail="No episodes found.")
    return episodes_data

# Endpoint to fetch a specific episode by ID
@app.get("/episodes/{episode_id}", response_model=Dict)
def get_episode_by_id(episode_id: int):
    for episode in episodes_data:
        if episode.get("id") == episode_id:
            return episode
    raise HTTPException(status_code=404, detail=f"Episode with ID {episode_id} not found.")

# Run the application (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)