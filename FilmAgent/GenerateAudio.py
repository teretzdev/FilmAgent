import re
import os
import requests
import random
import logging
from util import *
from tqdm import tqdm
from LLMCaller import GPTTTS
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# TO DO
Script_path = os.path.join(os.path.dirname(__file__), "script.json")
actos_path = os.path.join(os.path.dirname(__file__), "actors_profile.json")
Audio_path = os.path.join(os.path.dirname(__file__), "audio_files")
logging.debug(f"Script path: {Script_path}, Actors path: {actos_path}, Audio path: {Audio_path}")
# TO DO
if not os.path.exists(Audio_path):
    logging.debug(f"Audio path '{Audio_path}' does not exist. Creating it.")
    os.makedirs(Audio_path)


# ChatTTS
url = "http://xxx.xxx.xxx.xxx:xxxx/" # The API path where the chattts service is deployed
Chat_Speaker_female = [0, 1, 2, 3, 4]
Chat_Speaker_male = [0, 1, 2, 3, 4]
random.shuffle(Chat_Speaker_female) 
random.shuffle(Chat_Speaker_male) 
invalid_characters_map = {
    "!": ".",
    "?": ".",
    "'": ",",
    ':': ',',
    ';': ',',
    '!': '.',
    '(': ',',
    ')': ',',
    '[': ',',
    ']': ',',
    '>': ',',
    '<': ',',
    '-': ','
}
# OpenAI TTS
GPT_Speaker_female = ["alloy", "fable", "nova", "shimmer"]
GPT_Speaker_male = ["echo","onyx" ]
random.shuffle(GPT_Speaker_female) 
random.shuffle(GPT_Speaker_male) 


# Clear all audio generated last time
logging.info("Clearing all previously generated audio files...")
for filename in os.listdir(Audio_path):
    file_path = os.path.join(Audio_path, filename)
    try:
        os.remove(file_path)
        logging.debug(f"Deleted file: {file_path}")
    except Exception as e:
        logging.error(f"Failed to delete file: {file_path}", exc_info=True)


# GPT: Assign a voice to each character
# name2gptspeaker = {}
# roles = read_json(actos_path)
# for role in roles:
#     if role['gender'].lower() == "male":
#         name2gptspeaker[role['name']] = GPT_Speaker_male[0]
#         GPT_Speaker_male.pop(0)
#     else:
#         name2gptspeaker[role['name']] = GPT_Speaker_female[0]
#         GPT_Speaker_female.pop(0)


# ChatTTS: Assign a voice to each character
name2chatspeaker = {}
try:
    roles = read_json(actos_path)
    logging.debug(f"Loaded roles from {actos_path}: {roles}")
except Exception as e:
    logging.error(f"Failed to load roles from {actos_path}", exc_info=True)
    raise
for role in roles:
    name2chatspeaker[role['name']] = {}
    if role['gender'].lower() == "male":
        name2chatspeaker[role['name']]['id'] = Chat_Speaker_male[0]
        name2chatspeaker[role['name']]['gender'] = "male"
        Chat_Speaker_male.pop(0)
    else:
        name2chatspeaker[role['name']]['id'] = Chat_Speaker_female[0]
        name2chatspeaker[role['name']]['gender'] = "female"
        Chat_Speaker_female.pop(0)
        


try:
    script = read_json(Script_path)
    logging.debug(f"Loaded script from {Script_path}: {script}")
except Exception as e:
    logging.error(f"Failed to load script from {Script_path}", exc_info=True)
    raise
lines = []
for scene in script:
    for event in scene['scene']:
        if "content" in event.keys():
            l = event["content"]
            if contains_digit(l):
                l = translate_digit(l)
            lines.append({"speaker": event["speaker"], "content": prompt_format(l, invalid_characters_map)+"[uv_break]"})


Flag = "ChatTTS" # GPT or ChatTTS

params_infer_code =  {'prompt':'[speed_3]', 'temperature':0.3,'top_P':0.9, 'top_K':1}
params_refine_text = {'prompt':'[oral_2][laugh_4][break_6]'}
logging.info(f"Assigned ChatTTS speakers: {name2chatspeaker}")

for line in tqdm(lines):
    # if Flag == "GPT":
    #     response = GPTTTS(line['content'], name2gptspeaker[line['speaker']])
    #     response.stream_to_file(cretae_new_path(Audio_path, "mp3"))
        
    if Flag == "ChatTTS":
        try:
            logging.info(f"Sending request to ChatTTS API for speaker: {line['speaker']}")
            response = requests.post(url, json={
                "gender": name2chatspeaker[line['speaker']]['gender'],
                "text": line['content'],
                "id": name2chatspeaker[line['speaker']]['id'],
                "params_infer_code": params_infer_code,
                "params_refine_text": params_refine_text
            })
            if response.status_code == 200:
                content_disposition = response.headers.get("Content-Disposition")
                filename = re.findall("filename=\"(.+)\"", content_disposition)
                filename = filename[0]
                file_path = os.path.join(Audio_path, filename)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                logging.info(f"Audio file saved: {file_path}")
            else:
                logging.error(f"Failed to create item. Status code: {response.status_code}, Response: {response.text}")
        except Exception as e:
            logging.error("Error during ChatTTS API call.", exc_info=True)