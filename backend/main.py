"""
This module generates a music track recommendation based on a randomly generated configuration. 
It fetches the AI model API key from environment variables, constructs a prompt, and uses AI to 
get a recommendation.
"""

import os
from dotenv import load_dotenv

from scripts.generate_prompt import generate_prompt
from scripts.generate_track_g4f import generate_track_basic, generate_track_rotate
from scripts.generate_randomizer import generate_track_config
from scripts.generate_track_aimlapi import generate_track_aimlapi

load_dotenv()


def main():
    """
    Main function that generates a music track recommendation.

    The function:
    1. Loads the AIML API key from environment variables.
    2. Generates a random track configuration.
    3. Creates a prompt based on the generated track configuration.
    4. Sends the prompt to the AIML API with a system message to act as a music expert.
    5. Returns the AI-generated music track recommendation.
    """
    api_key = os.getenv("AIML_API_KEY")

    track_config = generate_track_config()
    user_prompt = generate_prompt(track_config)

    system_prompt = "You're an expert in music."
    result = generate_track_aimlapi(api_key, system_prompt, user_prompt)
    print(result)


if __name__ == "__main__":
    main()
