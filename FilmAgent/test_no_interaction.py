from util import *
from LLMCaller import *
from typing import Dict, List, Union
import random
import copy
import os

ROOT_PATH = "/absolute/path/to/FilmAgent"
ID = 13

topics = [
    "Reconcilation in a friend reunion",
    "A quarrel and breakup scene",
    "Casual meet-up with an old friend",
    "Emergency meeting after a security breach",
    "Late night brainstorming for a startup",
    "Family argument during dinner",
    "Emotional farewell at the roadside",
    "Heated debate over investments in the office",
    "Heated family discussion ending in a heartfelt apology",
    "Office gossip turning into a major understanding",
    "Celebratory end of project cheers with team members",
    "Planning a secret escape from a mundane routine",
    "Unexpected guest crashes a small house party",
    "An employee's emotional breakdown after being terminated",
    "Confession of a long-held secret among close friends"
]

class FilmCrafter:
    def __init__(self, topic: str) -> None:
        self.topic = topic
        self.store_path = os.path.join(ROOT_PATH, "store", "no_interaction", f"{ID}")
        self.log_path = os.path.join(self.store_path, "prompt.txt")
        self.profile_path = os.path.join(self.store_path, "actors_profile.json")
        self.action_description_path = os.path.join(ROOT_PATH, "Locations", "actions.txt")
        self.shot_description_path = os.path.join(ROOT_PATH, "Locations", "shots.txt")
        # scenes
        self.scene_path = os.path.join(self.store_path, "scenes_1.json")
        # + lines
        self.scene_path_1 = os.path.join(self.store_path, "scenes_2.json")
        # + positions
        self.scene_path_2 = os.path.join(self.store_path, "scenes_3.json")
        # + actions
        self.scene_path_3 = os.path.join(self.store_path, "scenes_4.json")
        # + movement
        self.scene_path_4 = os.path.join(self.store_path, "scenes_5.json")
        # + shot (stage3_verify)
        self.scene_path_5 = os.path.join(self.store_path, "scenes_6.json")
        # The final script
        self.script_path = os.path.join(self.store_path, "script.json")

        # The maximum number of characters in a film
        self.character_limit = 4
        # The maximum number of scenes in a film
        self.scene_limit = 3
        # The maximum number of discussions between director and screenwriter
        self.stage1_verify_limit = 3
        # The maximum number of discussions between director, actor and screenwriter
        self.stage2_verify_limit = 3
        # The maximum number of discussions between director and cinematographer
        self.stage3_verify_limit = 3

        if not os.path.exists(self.store_path):
            os.makedirs(self.store_path)

    def call(self, identity: str, params: Dict, trans2json: bool = True) -> Union[str, dict, list]:
        prompt = read_prompt(os.path.join(ROOT_PATH, "Prompt", f"{identity}.txt"))
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
        male_characters = ", ".join(
            list(map(lambda x: x['name'], filter(lambda x: x['gender'].lower() == 'male', profile))))
        female_characters = ", ".join(
            list(map(lambda x: x['name'], filter(lambda x: x['gender'].lower() == 'female', profile))))

        params = {"{topic}": self.topic,
                  "{male_characters}": male_characters,
                  "{female_characters}": female_characters,
                  "{scene_limit}": self.scene_limit}
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
        for id, scene in enumerate(scenes):
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

            script_outline = script_outline + f"{id + 1}. **Scene {id + 1}**:\\\n   - topic: {topic}\\\n   - involved characters: {characters}\\\n   - plot: {plot}\\\n   - location: {location}\\\n   - dialogue goal: {goal}\\\n\\\n"

        params = {"{script_outline}": script_outline.strip()}
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

    def clean_script(self):
        '''
            Description: Only keep the necessary information in the script and perform certain checks to avoid errors when executing the script in Unity.
        '''
        scenes = read_json(self.scene_path_5)
        profiles = read_json(self.profile_path)
        v_characters = [item['name'] for item in profiles]
        data = []
        for scene in scenes:
            new_scene = {}
            scene_information_key = return_most_similar('scene_information', list(scene.keys()))
            new_scene['scene information'] = scene[scene_information_key]
            new_scene['scene'] = []
            for line in scene['dialogues']:
                new_line = {}
                if 'speaker' in line.keys():
                    new_line['speaker'] = return_most_similar(line['speaker'], v_characters)
                    new_line['content'] = line['content']
                new_scene['scene'].append(new_line)
            data.append(new_scene)
        write_json(self.script_path, data)


if __name__ == '__main__':
    f = FilmCrafter(topic=topics[ID - 1])
    print("Characters selecting >>>")
    f.casting()
    print("Scenes planning >>>")
    f.scenes_plan()
    print("Lines generating >>>")
    f.lines_generate()
    print("Script cleaning >>>")
    f.clean_script()
