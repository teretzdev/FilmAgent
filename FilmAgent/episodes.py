import os
import random
from util import read_json, write_json, read_prompt, prompt_format, log_prompt
from LLMCaller import GPTCall, clean_text, GPTResponse2JSON

ROOT_PATH = "/absolute/path/to/FilmAgent"

class GTARealityShow:
    def __init__(self, season_name: str, episodes_per_season: int = 10):
        self.season_name = season_name
        self.episodes_per_season = episodes_per_season
        self.log_path = os.path.join(ROOT_PATH, "Logs", f"{season_name}_log.txt")
        self.contestants_path = os.path.join(ROOT_PATH, "Script", "gta_contestants.json")
        self.episodes_path = os.path.join(ROOT_PATH, "Script", f"{season_name}_episodes.json")
        self.prizes_path = os.path.join(ROOT_PATH, "Script", f"{season_name}_prizes.json")
        self.crowd_votes_path = os.path.join(ROOT_PATH, "Script", f"{season_name}_crowd_votes.json")
        self.recurring_contestants = []
        self.unique_purposes = [
            "Heist a bank",
            "Win a high-speed race",
            "Survive a police chase",
            "Perform the most daring stunt",
            "Capture a rival gang's territory",
        ]
        self.locations = [
            "Police Station",
            "Gas Station",
            "Grove Street",
            "Airport",
            "Gun Store",
            "Beach",
            "Car Dealer",
            "Gang Territory",
        ]

    def call_ai_agent(self, identity: str, params: dict, trans2json: bool = True):
        prompt = read_prompt(os.path.join(ROOT_PATH, f"Prompt/GTA/{identity}.txt"))
        prompt = prompt_format(prompt, params)
        log_prompt(self.log_path, prompt)
        result = GPTCall(prompt)
        if trans2json:
            result = clean_text(result)
            result = GPTResponse2JSON(result)
        log_prompt(self.log_path, result)
        return result

    def load_contestants(self):
        if os.path.exists(self.contestants_path):
            self.recurring_contestants = read_json(self.contestants_path)
        else:
            raise FileNotFoundError("Contestants file not found. Please ensure the file exists.")

    def generate_episode(self, episode_number: int):
        if not self.recurring_contestants:
            self.load_contestants()

        unique_purpose = random.choice(self.unique_purposes)
        selected_contestants = random.sample(self.recurring_contestants, k=min(4, len(self.recurring_contestants)))

        selected_location = random.choice(self.locations)
        params = {
            "{episode_number}": episode_number,
            "{unique_purpose}": unique_purpose,
            "{selected_contestants}": ", ".join(selected_contestants),
            "{selected_location}": selected_location,
        }
        episode_plan = self.call_ai_agent("gta_director_2", params)
        episode_script = self.call_ai_agent("gta_screenwriter_2", params)

        return {
            "episode_number": episode_number,
            "unique_purpose": unique_purpose,
            "selected_contestants": selected_contestants,
            "plan": episode_plan,
            "script": episode_script,
        }

    def generate_season(self):
        season_data = []
        for episode_number in range(1, self.episodes_per_season + 1):
            episode_data = self.generate_episode(episode_number)
            season_data.append(episode_data)
        write_json(self.episodes_path, season_data)
        return season_data

    def generate_preview(self):
        """
        Generate a human-readable preview of the last two episodes and save it to a file.
        """
        episodes_file = os.path.join(ROOT_PATH, "Script", f"{self.season_name}_episodes.json")
        preview_file = os.path.join(ROOT_PATH, "Script", "episodes_preview.txt")

        if not os.path.exists(episodes_file):
            raise FileNotFoundError(f"Episodes file not found: {episodes_file}")

        episodes = read_json(episodes_file)
        if len(episodes) < 2:
            raise ValueError("Not enough episodes to generate a preview.")

        # Extract the last two episodes
        last_two_episodes = episodes[-2:]

        # Format the preview
        preview_lines = []
        for episode in last_two_episodes:
            preview_lines.append(f"Episode {episode['episode_number']}:")
            preview_lines.append(f"  Purpose: {episode['unique_purpose']}")
            preview_lines.append(f"  Contestants: {', '.join(episode['selected_contestants'])}")
            preview_lines.append(f"  Location: {episode['selected_location']}")
            preview_lines.append(f"  Plan: {episode['plan']}")
            preview_lines.append(f"  Script: {episode['script']}")
            preview_lines.append("")  # Add a blank line between episodes

        # Write the preview to the file
        with open(preview_file, "w") as f:
            f.write("\\n".join(preview_lines))

        print(f"Preview of the last two episodes saved to {preview_file}")

    def manage_crowd_votes(self):
        if not os.path.exists(self.crowd_votes_path):
            raise FileNotFoundError("Crowd votes file not found. Please ensure the file exists.")

        crowd_votes = read_json(self.crowd_votes_path)
        new_contestants = crowd_votes.get("new_contestants", [])
        advantages = crowd_votes.get("advantages", {})

        for contestant in new_contestants:
            if contestant not in self.recurring_contestants:
                self.recurring_contestants.append(contestant)

        return advantages

    def assign_prizes(self, episode_data):
        prizes = []
        for contestant in episode_data["selected_contestants"]:
            prize = random.choice(["Luxury Car", "In-game Currency", "Weapon Upgrade", "Immunity"])
            prizes.append({"contestant": contestant, "prize": prize})
        write_json(self.prizes_path, prizes)
        return prizes

    def run(self):
        self.load_contestants()
        season_data = self.generate_season()
        for episode in season_data:
            advantages = self.manage_crowd_votes()
            prizes = self.assign_prizes(episode)
            print(f"Episode {episode['episode_number']} completed with prizes: {prizes} and advantages: {advantages}")

        # Generate a preview of the last two episodes
        self.generate_preview()


if __name__ == "__main__":
    gta_show = GTARealityShow(season_name="GTA_Season_1")
    gta_show.run()# New file: FilmAgent/episodes.py

import os
import random
from util import read_json, write_json, read_prompt, prompt_format, log_prompt
from LLMCaller import GPTCall, clean_text, GPTResponse2JSON

ROOT_PATH = "/absolute/path/to/FilmAgent"

class GTARealityShow:
    def __init__(self, season_name: str, episodes_per_season: int = 10):
        self.season_name = season_name
        self.episodes_per_season = episodes_per_season
        self.log_path = os.path.join(ROOT_PATH, "Logs", f"{season_name}_log.txt")
        self.contestants_path = os.path.join(ROOT_PATH, "Script", "gta_contestants.json")
        self.episodes_path = os.path.join(ROOT_PATH, "Script", f"{season_name}_episodes.json")
        self.prizes_path = os.path.join(ROOT_PATH, "Script", f"{season_name}_prizes.json")
        self.crowd_votes_path = os.path.join(ROOT_PATH, "Script", f"{season_name}_crowd_votes.json")
        self.recurring_contestants = []
        self.unique_purposes = [
            "Heist a bank",
            "Win a high-speed race",
            "Survive a police chase",
            "Perform the most daring stunt",
            "Capture a rival gang's territory",
        ]
        self.locations = [
            "Police Station",
            "Gas Station",
            "Grove Street",
            "Airport",
            "Gun Store",
            "Beach",
            "Car Dealer",
            "Gang Territory",
        ]

    def call_ai_agent(self, identity: str, params: dict, trans2json: bool = True):
        prompt = read_prompt(os.path.join(ROOT_PATH, f"Prompt/GTA/{identity}.txt"))
        prompt = prompt_format(prompt, params)
        log_prompt(self.log_path, prompt)
        result = GPTCall(prompt)
        if trans2json:
            result = clean_text(result)
            result = GPTResponse2JSON(result)
        log_prompt(self.log_path, result)
        return result

    def load_contestants(self):
        if os.path.exists(self.contestants_path):
            self.recurring_contestants = read_json(self.contestants_path)
        else:
            raise FileNotFoundError("Contestants file not found. Please ensure the file exists.")

    def generate_episode(self, episode_number: int):
        if not self.recurring_contestants:
            self.load_contestants()

        unique_purpose = random.choice(self.unique_purposes)
        selected_contestants = random.sample(self.recurring_contestants, k=min(4, len(self.recurring_contestants)))

        selected_location = random.choice(self.locations)
        params = {
            "{episode_number}": episode_number,
            "{unique_purpose}": unique_purpose,
            "{selected_contestants}": ", ".join(selected_contestants),
            "{selected_location}": selected_location,
        }
        episode_plan = self.call_ai_agent("gta_director_2", params)
        episode_script = self.call_ai_agent("gta_screenwriter_2", params)

        return {
            "episode_number": episode_number,
            "unique_purpose": unique_purpose,
            "selected_contestants": selected_contestants,
            "plan": episode_plan,
            "script": episode_script,
        }

    def generate_season(self):
        season_data = []
        for episode_number in range(1, self.episodes_per_season + 1):
            episode_data = self.generate_episode(episode_number)
            season_data.append(episode_data)
        write_json(self.episodes_path, season_data)
        return season_data

    def manage_crowd_votes(self):
        if not os.path.exists(self.crowd_votes_path):
            raise FileNotFoundError("Crowd votes file not found. Please ensure the file exists.")

        crowd_votes = read_json(self.crowd_votes_path)
        new_contestants = crowd_votes.get("new_contestants", [])
        advantages = crowd_votes.get("advantages", {})

        for contestant in new_contestants:
            if contestant not in self.recurring_contestants:
                self.recurring_contestants.append(contestant)

        return advantages

    def assign_prizes(self, episode_data):
        prizes = []
        for contestant in episode_data["selected_contestants"]:
            prize = random.choice(["Luxury Car", "In-game Currency", "Weapon Upgrade", "Immunity"])
            prizes.append({"contestant": contestant, "prize": prize})
        write_json(self.prizes_path, prizes)
        return prizes

    def run(self):
        self.load_contestants()
        season_data = self.generate_season()
        for episode in season_data:
            advantages = self.manage_crowd_votes()
            prizes = self.assign_prizes(episode)
            print(f"Episode {episode['episode_number']} completed with prizes: {prizes} and advantages: {advantages}")


if __name__ == "__main__":
    gta_show = GTARealityShow(season_name="GTA_Season_1")
    gta_show.run()