from fastapi import FastAPI, HTTPException
from typing import List, Dict
import os
import json

# Initialize FastAPI app
app = FastAPI()

# Mock data paths (replace with actual paths in production)
SCRIPTS_PATH = "FilmAgent/scripts.json"
EPISODES_PATH = "FilmAgent/episodes.json"

# Utility function to load JSON data
def load_json(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return json.load(file)

# Load scripts and episodes data
scripts_data = load_json(SCRIPTS_PATH)
episodes_data = load_json(EPISODES_PATH)

@app.get("/")
def root():
    return {"message": "Welcome to the FilmAgent API!"}

# Endpoint to fetch all scripts
@app.get("/scripts", response_model=List[Dict])
def get_all_scripts():
    if not scripts_data:
        raise HTTPException(status_code=404, detail="No scripts found.")
    return scripts_data

# Endpoint to fetch a specific script by ID
@app.get("/scripts/{script_id}", response_model=Dict)
def get_script_by_id(script_id: int):
    for script in scripts_data:
        if script.get("id") == script_id:
            return script
    raise HTTPException(status_code=404, detail=f"Script with ID {script_id} not found.")

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
