"""This module provides functions to generate music recommendations using the G4F client."""

from g4f.client import Client
from g4f.Provider import Chatgpt4o, ChatgptFree, FreeChatgpt, FreeGpt, RetryProvider


def generate_track_basic(prompt: str):
    """Generates a music track recommendation using a basic GPT model.

    Args:
        prompt (str): The user prompt containing the details for the track recommendation.

    Returns:
        str: The AI-generated track recommendation.
    """
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def generate_track_rotate(prompt: str):
    """Generates a music track recommendation using a rotating selection of GPT models.

    Args:
        prompt (str): The user prompt containing the details for the track recommendation.

    Returns:
        str: The AI-generated track recommendation.
    """
    my_provider = RetryProvider(
        [Chatgpt4o, ChatgptFree, FreeChatgpt, FreeGpt], shuffle=True
    )
    client = Client(provider=my_provider)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        provider=my_provider,
    )
    return response.choices[0].message.content
