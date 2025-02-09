import os
from util import *
from LLMCaller import *
from typing import Dict, List, Union
import random
import copy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from FilmAgent.api import app as api_app

# Load environment variables
load_dotenv()

# Use environment variable with fallback
ROOT_PATH = os.getenv('FILM_AGENT_ROOT', "/absolute/path/to/FilmAgent")

class FilmCrafter:
    
    def __init__(self, topic: str, scenario: str = "default") -> None:
        self.topic = topic
        self.scenario = scenario
        self.log_path = cretae_new_path(os.path.join(ROOT_PATH, "Logs"), "txt")

    def calculate_script_duration(self, script_path: str) -> float:
        """
        Calculate the total duration of a script based on dialogue and action timings.

        Args:
            script_path (str): Path to the script JSON file.

        Returns:
            float: Total duration of the script in seconds.
        """
        script = read_json(script_path)
        total_duration = 0.0
        avg_word_time = 0.5  # Average time per word in seconds
        action_time = 2.0    # Default time for each action in seconds

        for scene in script:
            for line in scene.get("scene", []):
                if "content" in line:
                    word_count = len(line["content"].split())
                    total_duration += word_count * avg_word_time
                if "actions" in line:
                    total_duration += len(line["actions"]) * action_time

        return total_duration
        if self.scenario == "GTA Reality Show":
            self.profile_path = os.path.join(ROOT_PATH, "Script\\gta_contestants.json")
        else:
            self.profile_path = os.path.join(ROOT_PATH, "Script\\actors_profile.json")
        self.action_description_path = os.path.join(ROOT_PATH, "Locations\\actions.txt")
        self.shot_description_path = os.path.join(ROOT_PATH, "Locations\\shots.txt")
        # scenes
        self.scene_path = os.path.join(ROOT_PATH, "Script\scenes_1.json") 
        # + lines
        self.scene_path_1 = os.path.join(ROOT_PATH, "Script\scenes_2.json") 
        # + positions
        self.scene_path_2 = os.path.join(ROOT_PATH, "Script\scenes_3.json") 
        # + actions
        self.scene_path_3 = os.path.join(ROOT_PATH, "Script\scenes_4.json")
        # stage1_verify
        self.scene_path_4 = os.path.join(ROOT_PATH, "Script\scenes_5.json")
        # stage2_verify
        self.scene_path_5 = os.path.join(ROOT_PATH, "Script\scenes_6.json") 
        # + movement
        self.scene_path_6 = os.path.join(ROOT_PATH, "Script\scenes_7.json") 
        # + shot (stage3_verify)
        self.scene_path_7 = os.path.join(ROOT_PATH, "Script\scenes_8.json") 
        # The final script
        self.script_path = cretae_new_path(os.path.join(ROOT_PATH, "Script\script"), "json")
        
        # director's shot annotation
        self.director_shot_path = os.path.join(ROOT_PATH, "Script\\director_shot.json")
        # cinematographer's shot annotation
        self.cinematographer_shot_path = os.path.join(ROOT_PATH, "Script\\cinematographer_shot.json")

    def plan_image_generation(self, script_path: str, interval: int = 5) -> List[str]:
        """
        Plan image generation at specified intervals.

        Args:
            script_path (str): Path to the script JSON file.
            interval (int): Time interval in seconds between images.

        Returns:
            List[str]: List of filenames for the generated images.
        """
        script = read_json(script_path)
        total_duration = self.calculate_script_duration(script_path)
        num_images = int(total_duration // interval)
        image_filenames = []

        for i in range(num_images):
            filename = f"image_{i * interval}s.png"
            image_filenames.append(filename)

        return image_filenames

        # The maximum number of characters in a film
        self.character_limit = 4
        # The maximum number of scenes in a film
        self.scene_limit = 3
        # The maximum number of discussions between director and screenwriter
        self.stage1_verify_limit = 3
        # The maximum number of discussions between director, actor and screenwriter
        self.stage2_verify_limit = 3
        # The maximum number of discussions between director and cinematographer
        self.stage3_verify_limit = 4

    def login_to_video_generator(self) -> bool:
        """
        Log into the video generator website using credentials from the .env file.

        Returns:
            bool: True if login is successful, False otherwise.
        """
        username = os.getenv("VIDEO_GEN_USERNAME")
        password = os.getenv("VIDEO_GEN_PASSWORD")

        if not username or not password:
            raise ValueError("Missing VIDEO_GEN_USERNAME or VIDEO_GEN_PASSWORD in .env file.")

        # Simulate login process (replace with actual API call if available)
        print(f"Logging in with username: {username}")
        # Example: response = requests.post("https://video-generator.com/api/login", data={"username": username, "password": password})
        # return response.status_code == 200
        return True
        

    def call(self, identity: str, params: Dict, trans2json: bool = True) -> Union[str, dict, list]:
        if self.scenario == "GTA Reality Show":
            prompt = read_prompt(os.path.join(ROOT_PATH, f"Prompt\\GTA\\{identity}.txt"))
        else:
            prompt = read_prompt(os.path.join(ROOT_PATH, f"Prompt\{identity}.txt"))
        prompt = prompt_format(prompt, params)
        log_prompt(self.log_path, prompt)
        result = GPTCall(prompt)
        if trans2json:
            result = clean_text(result)
            result = GPTResponse2JSON(result)
        log_prompt(self.log_path, result)
        return result

    
    def casting(self):
        '''
            Role: Director

            Behavior: Create the main characters and their bios for the film script.
        '''
        params = {"{topic}": self.topic, "{character_limit}": self.character_limit}
        if self.scenario == "GTA Reality Show":
            result = self.call("gta_director_1", params)
        else:
            result = self.call("director_1", params)
        write_json(self.profile_path, result)
        
        
    def scenes_plan(self):
        '''
            Role: Director

            Behavior:
                Plan the outline of script, include:
                1. The number of scenes.
                2. The characters, location and main plot of each scene.
        '''
        profile = read_json(self.profile_path)
        male_characters = ", ".join(list(map(lambda x: x['name'], 
                                             filter(lambda x: x['gender'].lower() == 'male', profile))))
        female_characters = ", ".join(list(map(lambda x: x['name'], 
                                               filter(lambda x: x['gender'].lower() == 'female', profile))))
        
        params = {"{topic}": self.topic, 
                  "{male_characters}": male_characters,
                  "{female_characters}": female_characters,
                  "{scene_limit}": self.scene_limit}
        if self.scenario == "GTA Reality Show":
            result = self.call("gta_director_2", params)
        else:
            if self.scenario == "GTA Reality Show":
                result = self.call("gta_director_2", params)
            else:
                result = self.call("director_2", params)
        write_json(self.scene_path, result)
        
        
    def lines_generate(self):
        '''
            Role: Screenwriter

            Behavior: Write lines for the script.
        '''
        scenes = read_json(self.scene_path)
        script_outline = ""
        who = []
        where = []
        what = []
        for id,scene in enumerate(scenes):
            selected_roles = scene[return_most_similar("selected-characters", list(scene.keys()))]
            selected_location = scene[return_most_similar("selected-location", list(scene.keys()))]
            story_plot = scene[return_most_similar("story-plot", list(scene.keys()))]
            who.append(selected_roles)
            where.append(selected_location)
            what.append(story_plot)

            topic = scene[return_most_similar("sub-topic", list(scene.keys()))]
            characters = ", ".join(selected_roles)
            plot = story_plot
            location = selected_location
            goal = scene[return_most_similar("dialogue-goal", list(scene.keys()))]

            script_outline = script_outline + f"{id + 1}. **Scene {id + 1}**:\\\\\\\\n   - topic: {topic}\\\\\\\\n   - involved characters: {characters}\\\\\\\\n   - plot: {plot}\\\\\\\\n   - location: {location}\\\\\\\\n   - dialogue goal: {goal}\\\\\\\\n\\\\\\\\n"
    
        params = {"{script_outline}": script_outline.strip()}
        if self.scenario == "GTA Reality Show":
            result = self.call("gta_screenwriter_1", params)
        else:
            result = self.call("screenwriter_1", params)
        
        lines = []
        assert len(result) == len(scenes)
        for j in range(len(scenes)):
            line = {}
            line['scene_information'] = {}
            line['scene_information']['who'] = who[j]
            line['scene_information']['where'] = where[j]
            line['scene_information']['what'] = what[j]
            line['dialogues'] = result[j][return_most_similar("scene-dialogue", list(result[j].keys()))]
            lines.append(line)
        write_json(self.scene_path_1, lines)

                
                
    def position_mark(self):
        '''
            Role: Screenwriter

            Behavior: Choose an appropriate initial position for each character in each scene of the script.
        '''
        scenes = read_json(self.scene_path_1)
        script_information = ""
        optional_positions = ""
        for id,scene in enumerate(scenes):
            i = id + 1
            who = scene['scene_information']['who']
            where = scene['scene_information']['where']
            what = scene['scene_information']['what']

            script_information = script_information + f"{i}. **Scene {i}**:\\\\\\\\n   - characters: {who}\\\\\\\\n   - location: {where}\\\\\\\\n   - plot: {what}\\\\\\\\n\\\\\\\\n"
            
            position_path = os.path.join(ROOT_PATH, f"Locations\{where}\position.json")
            positions = read_json(position_path)
            normal_position = [item for item in positions if item['fixed_angle'] == False]
            # This "if judgment" is related to the position, and camera settings in Unity.
            if len(who) >= len(positions) - len(normal_position) + 2:
                p = ""
                for it,position in enumerate(positions):
                    j = it + 1
                    p = p + f"   - Position {j}: " + position['description'] + '\\\\\\\\n'
            else:
                p = ""
                for it,position in enumerate(normal_position):
                    j = it + 1
                    p = p + f"   - Position {j}: " + position['description'] + '\\\\\\\\n'                    
            optional_positions = optional_positions + f"{i}. **Positions in {where}**:\\\\\\\\n{p}\\\\\\\\n"
                
        params = {"{script_information}": script_information.strip(), 
                        "{optional_positions}": optional_positions.strip()}
        if self.scenario == "GTA Reality Show":
            result = self.call("gta_screenwriter_2", params)
        else:
            result = self.call("screenwriter_2", params)
        
        assert len(result) == len(scenes)
        for j in range(len(scenes)):
            scenes[j]["initial position"] = result[j][return_most_similar("scene-position", list(result[j].keys()))]
        write_json(self.scene_path_2, scenes)



# Example usage of new methods
crafter = FilmCrafter(topic="Sample Topic")
script_path = crafter.script_path

# Calculate script duration
duration = crafter.calculate_script_duration(script_path)
print(f"Total script duration: {duration} seconds")

# Plan image generation
image_plan = crafter.plan_image_generation(script_path)
print(f"Image generation plan: {image_plan}")

# Log into video generator
if crafter.login_to_video_generator():
    print("Logged into video generator successfully.")