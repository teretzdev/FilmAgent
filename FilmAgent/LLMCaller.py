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
            except OpenAI.Error as api_error:
                last_error = api_error
                print(f"OpenAI API error during GPTCall: {api_error}")
            except Exception as e:
                last_error = e
                print(f"Unexpected error during GPTCall: {e}")
            finally:
                if counter < max_retries - 1:
                    time.sleep(delay * (2 ** counter))  # Exponential backoff
                counter += 1

    raise LLMError(f"Failed after {max_retries} attempts. Last error: {str(last_error)}")


def GPTTTS(text: str, role: str) -> Optional[bytes]:
    """
    Generate Text-to-Speech (TTS) audio using OpenAI's API.
    Args:
        text (str): The input text to convert to speech.
        role (str): The voice role to use for TTS.
    Returns:
        Optional[bytes]: The audio content in MP3 format, or None if an error occurs.
    """
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        organization = os.getenv('OPENAI_ORG')
        if not api_key or not organization:
            raise ValueError("API key or organization is not set in environment variables.")

        client = OpenAI(api_key=api_key, organization=organization)
        response = client.audio.speech.create(
            model="tts-1",
            voice=role,
            input=text,
            response_format="mp3"
        )
        return response
    except OpenAI.Error as api_error:
        print(f"OpenAI API error during GPTTTS: {api_error}")
    except Exception as e:
        print(f"Unexpected error during GPTTTS: {e}")
    return None