from fastapi import FastAPI, HTTPException
from typing import List, Dict, Optional
import os
import json
from pathlib import Path

# Initialize FastAPI app
app = FastAPI()

# Mock data paths (replace with actual paths in production)
SCRIPTS_PATH = "FilmAgent/scripts.json"
EPISODES_PATH = "FilmAgent/episodes.json"
CONTESTANTS_PATH = "FilmAgent/contestants.json"
PRIZES_PATH = "FilmAgent/prizes.json"

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

# Load scripts, episodes, contestants, and prizes data
scripts_data = load_json(SCRIPTS_PATH)
episodes_data = load_json(EPISODES_PATH)
contestants_data = load_json(CONTESTANTS_PATH)
prizes_data = load_json(PRIZES_PATH)

@app.get("/")
def root():
    return {"message": "Welcome to the FilmAgent API!"}

# Endpoint to fetch all scripts
@app.get("/scripts", response_model=List[Dict])
def get_all_scripts():
    if not scripts_data:
        raise HTTPException(status_code=404, detail="No scripts found.")
    return scripts_data

# Endpoint to fetch all contestants
@app.get("/contestants", response_model=List[Dict])
def get_all_contestants():
    if not contestants_data:
        raise HTTPException(status_code=404, detail="No contestants found.")
    return contestants_data

# Endpoint to fetch a specific contestant by ID
@app.get("/contestants/{contestant_id}", response_model=Dict)
def get_contestant_by_id(contestant_id: int):
    try:
        contestant = next((c for c in contestants_data if c.get("id") == contestant_id), None)
        if not contestant:
            raise HTTPException(status_code=404, detail=f"Contestant with ID {contestant_id} not found")
        return contestant
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to fetch available prizes
@app.get("/prizes", response_model=List[Dict])
def get_all_prizes():
    if not prizes_data:
        raise HTTPException(status_code=404, detail="No prizes found.")
    return prizes_data

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