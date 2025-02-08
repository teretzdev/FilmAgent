import os
import time
from openai import OpenAI
from typing import Optional

class LLMError(Exception):
    pass
def GPTCall(prompt: str, max_retries: int = 3, delay: float = 1.0) -> str:
def GPTCall(prompt: str, max_retries: int = 3, delay: float = 1.0) -> str:
    counter = 0
    last_error = None

    while counter < max_retries:
        try:
            client = OpenAI(
                api_key=os.getenv('OPENAI_API_KEY'),
                organization=os.getenv('OPENAI_ORG')
            )
            completion = client.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return completion.choices[0].message.content
        except Exception as e:
            last_error = e
            print(f"Error during GPTCall: {e}")
            if counter < max_retries - 1:
                time.sleep(delay * (2 ** counter))  # Exponential backoff
            counter += 1

    raise LLMError(f"Failed after {max_retries} attempts. Last error: {str(last_error)}")


def GPTTTS(text, role):
    
    openai.api_key = api_key
    openai.organization = organization
    client = OpenAI(api_key = api_key, organization = organization)
    response = client.audio.speech.create(
        model = "tts-1",
        voice = role,
        input = text,
        response_format = "mp3"
    )
    
    return response