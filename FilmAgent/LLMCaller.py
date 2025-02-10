import os
import time
from openai import OpenAI
from typing import Optional

class LLMError(Exception):
    pass
def GPTCall(prompt: str, max_retries: int = 3, delay: float = 1.0) -> str:
    """
    Calls the GPT model with the given prompt and retries on failure.

    Args:
        prompt (str): The input prompt for the GPT model.
        max_retries (int): Maximum number of retries on failure.
        delay (float): Delay between retries in seconds.

    Returns:
        str: The response from the GPT model.
    """
    import os
    from openai import OpenAI
    import time

    last_error = None
    counter = 0

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
            print(f"Error: {e}")
            if counter < max_retries - 1:
                time.sleep(delay * (counter + 1))  # Exponential backoff
            counter += 1

    raise LLMError(f"Failed after {max_retries} attempts. Last error: {str(last_error)}")
        
            last_error = e
            print(e)
            if counter < max_retries:
                time.sleep(delay * counter)  # Exponential backoff
            counter += 1
    raise LLMError(f"Failed after {max_retries} attempts. Last error: {str(last_error)}")
    return result


def GPTTTS(text, role):
    
    def GPTTTS(text: str, role: str) -> bytes:
        """
        Generates text-to-speech audio using GPT.

        Args:
            text (str): The input text to convert to speech.
            role (str): The voice role for the TTS.

        Returns:
            bytes: The audio content in MP3 format.
        """
        import os
        from openai import OpenAI

        client = OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            organization=os.getenv('OPENAI_ORG')
        )
        response = client.audio.speech.create(
            model="tts-1",
            voice=role,
            input=text,
            response_format="mp3"
        )
        return response.content
    
    return response