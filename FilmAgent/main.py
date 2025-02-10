import os
import logging
from util import *
from LLMCaller import *
from FilmAgent.image_generator import generate_images_from_script
from FilmAgent.scripts.generate_actor_scripts import generate_actor_scripts
from typing import Dict, List, Union
import random
import copy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from FilmAgent.api import app as api_app

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()
logging.debug("Environment variables loaded.")

# Use environment variable with fallback
ROOT_PATH = os.getenv('FILM_AGENT_ROOT', "/absolute/path/to/FilmAgent")

class FilmCrafter:
    def __init__(self, topic: str, scenario: str = "default") -> None:

    def regenerate_images(self, script_path: str, output_dir: str, interval: int = 5) -> None:
        """
        Regenerate images based on the script JSON file.

        Args:
            script_path (str): Path to the script JSON file.
            output_dir (str): Directory where the regenerated images will be saved.
            interval (int): Time interval in seconds between images.

        Returns:
            None
        """
        logging.info("Starting image regeneration...")
        try:
            image_filenames = self.plan_image_generation(script_path, interval)
            logging.debug(f"Planned image filenames: {image_filenames}")
            self.export_images_with_labels(image_filenames, output_dir)
            logging.info(f"Images regenerated successfully and saved to {output_dir}.")
        except Exception as e:
            logging.error("Error during image regeneration.", exc_info=True)

    def regenerate_scripts(self, input_file: str, output_dir: str) -> None:
        """
        Regenerate actor scripts using text prompts from the input file.

        Args:
            input_file (str): Path to the input file containing text prompts.
            output_dir (str): Directory where the regenerated scripts will be saved.

        Returns:
            None
        """
        logging.info("Starting script regeneration...")
        try:
            generate_actor_scripts(input_file, output_dir)
            logging.info(f"Scripts regenerated successfully and saved to {output_dir}.")
        except Exception as e:
            logging.error("Error during script regeneration.", exc_info=True)

    def export_images_with_labels(self, image_filenames: List[str], output_dir: str) -> None:
        """
        Export images with filenames clearly indicating their sequence index.

        Args:
            image_filenames (List[str]): List of image filenames to be exported.
            output_dir (str): Directory where the images will be saved.

        Returns:
            None
        """
        if not os.path.exists(output_dir):
            logging.debug(f"Output directory '{output_dir}' does not exist. Creating it.")
            os.makedirs(output_dir)

        for idx, filename in enumerate(image_filenames, start=1):
            # Simulate image creation and save with sequential labels
            image_path = os.path.join(output_dir, filename)
            with open(image_path, 'w') as f:
                f.write(f"Image {idx}")  # Placeholder for actual image content
            logging.debug(f"Exported image: {image_path}")
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
            List[str]: List of filenames for the generated images, labeled sequentially.
        """
        script = read_json(script_path)
        total_duration = self.calculate_script_duration(script_path)
        num_images = int(total_duration // interval)
        image_filenames = []

        for i in range(num_images):
            filename = f"image_{i + 1}.png"  # Sequential labeling starts from 1
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

        # Image generation configuration
        self.image_interval = int(os.getenv("IMAGE_INTERVAL", 5))

    def generate_images(self) -> None:
        """
        Generate images for the script at specified intervals.

        Returns:
            None
        """
        logging.info("Starting image generation...")
        try:
            generated_images = generate_images_from_script(self.script_path, self.image_interval)
            logging.info(f"Generated images: {generated_images}")
        except Exception as e:
            logging.error("Error during image generation.", exc_info=True)
        

    def call(self, identity: str, params: Dict, trans2json: bool = True) -> Union[str, dict, list]:
        if self.scenario == "GTA Reality Show":
            prompt = read_prompt(os.path.join(ROOT_PATH, f"Prompt\\GTA\\{identity}.txt"))
        else:
            prompt = read_prompt(os.path.join(ROOT_PATH, f"Prompt\{identity}.txt"))
        prompt = prompt_format(prompt, params)
        logging.debug(f"Logging prompt to {self.log_path}: {prompt}")
        log_prompt(self.log_path, prompt)
        try:
            result = GPTCall(prompt)
            logging.debug(f"Raw GPT result: {result}")
            if trans2json:
                result = clean_text(result)
                result = GPTResponse2JSON(result)
            logging.debug(f"Processed GPT result: {result}")
        except Exception as e:
            logging.error("Error during GPT call.", exc_info=True)
            raise
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
        logging.info(f"Writing actor profiles to {self.profile_path}.")
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
        logging.info(f"Writing scenes plan to {self.scene_path}.")
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

            script_outline = script_outline + f"{id + 1}. **Scene {id + 1}**:\\\\\\\\\\\\n   - topic: {topic}\\\\\\\\\\\\n   - involved characters: {characters}\\\\\\\\\\\\n   - plot: {plot}\\\\\\\\\\\\n   - location: {location}\\\\\\\\\\\\n   - dialogue goal: {goal}\\\\\\\\\\\\n\\\\\\\\\\\\n"
    
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
        logging.info(f"Writing generated lines to {self.scene_path_1}.")
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

            script_information = script_information + f"{i}. **Scene {i}**:\\\\\\\\\\\\n   - characters: {who}\\\\\\\\\\\\n   - location: {where}\\\\\\\\\\\\n   - plot: {what}\\\\\\\\\\\\n\\\\\\\\\\\\n"
            
            position_path = os.path.join(ROOT_PATH, f"Locations\{where}\position.json")
            positions = read_json(position_path)
            normal_position = [item for item in positions if item['fixed_angle'] == False]
            # This "if judgment" is related to the position, and camera settings in Unity.
            if len(who) >= len(positions) - len(normal_position) + 2:
                p = ""
                for it,position in enumerate(positions):
                    j = it + 1
                    p = p + f"   - Position {j}: " + position['description'] + '\\\\\\\\\\\\n'
            else:
                p = ""
                for it,position in enumerate(normal_position):
                    j = it + 1
                    p = p + f"   - Position {j}: " + position['description'] + '\\\\\\\\\\\\n'                    
            optional_positions = optional_positions + f"{i}. **Positions in {where}**:\\\\\\\\\\\\n{p}\\\\\\\\\\\\n"
                
        params = {"{script_information}": script_information.strip(), 
                        "{optional_positions}": optional_positions.strip()}
        if self.scenario == "GTA Reality Show":
            result = self.call("gta_screenwriter_2", params)
        else:
            result = self.call("screenwriter_2", params)
        
        assert len(result) == len(scenes)
        for j in range(len(scenes)):
            scenes[j]["initial position"] = result[j][return_most_similar("scene-position", list(result[j].keys()))]
        logging.info(f"Writing initial positions to {self.scene_path_2}.")
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

# Generate images for the script
self.generate_images()

# Log into video generator
if crafter.login_to_video_generator():
    print("Logged into video generator successfully.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="FilmAgent CLI for regenerating scripts and images.")
    parser.add_argument("--regenerate-scripts", nargs=2, metavar=("INPUT_FILE", "OUTPUT_DIR"),
                        help="Regenerate actor scripts using the specified input file and output directory.")
    parser.add_argument("--regenerate-images", nargs=3, metavar=("SCRIPT_PATH", "OUTPUT_DIR", "INTERVAL"),
                        help="Regenerate images using the specified script path, output directory, and interval.")

    args = parser.parse_args()

    if args.regenerate_scripts:
        input_file, output_dir = args.regenerate_scripts
        crafter = FilmCrafter(topic="Sample Topic")
        crafter.regenerate_scripts(input_file, output_dir)

    if args.regenerate_images:
        script_path, output_dir, interval = args.regenerate_images
        crafter = FilmCrafter(topic="Sample Topic")
        crafter.regenerate_images(script_path, output_dir, int(interval))