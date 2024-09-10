"""Module that provides functionality to generate music recommendations using the AIML API."""

from openai import OpenAI


def generate_track_aimlapi(api_key: str, system_prompt: str, user_prompt: str):
    """Generates a music track recommendation using the AIML API.

    Args:
        api_key (str): The API key used to authenticate with the AIML API.
        system_prompt (str): System prompt that sets the context for the AI model.
        user_prompt (str): User prompt that specifies the details of the music recommendation.

    Returns:
        str: The content of the AI-generated track recommendation.
    """
    base_url = "https://api.aimlapi.com/v1"
    api = OpenAI(api_key=api_key, base_url=base_url)

    completion = api.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=256,
    )
    return completion.choices[0].message.content
