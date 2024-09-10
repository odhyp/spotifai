"""Module to generates a random track configuration based on weighted attributes."""

import random


genres = {
    "any genre": 2,
    "rock": 0.3,
    "pop": 0.3,
    "jazz": 0.3,
    "blues": 0.3,
}

eras = {
    "current year": 1,
    "last year": 2,
}

popularity = {
    "popular": 5,
    "less popular": 1,
}

artists = {
    "solo artist": 1,
    "band": 5,
}

countries = {
    "any country": 10,
    "USA": 1,
    "UK": 1,
    "Indonesia": 1,
    "South Korea": 1,
    "Japan": 1,
}

moods = {
    "happy": 1,
    "sad": 1,
}

tempos = {
    "slow": 1,
    "medium": 1,
    "fast": 1,
    "normal": 5,
}


def weighted_random_choice(randomizer: dict):
    """Selects a random item from a dictionary based on weighted probabilities.

    Args:
        randomizer (dict): A dictionary with item and weight.

    Returns:
        str: The randomly selected item.
    """
    items = list(randomizer.keys())
    weights = list(randomizer.values())
    selected_item = random.choices(items, weights=weights, k=1)
    return selected_item[0]


def generate_track_config():
    """Generates a track configuration with random attributes.

    Returns:
        dict: A dictionary containing randomly selected attributes.
    """
    track_config = {
        "genre": weighted_random_choice(genres),
        "era": weighted_random_choice(eras),
        "popularity": weighted_random_choice(popularity),
        "artist": weighted_random_choice(artists),
        "country": weighted_random_choice(countries),
        "mood": weighted_random_choice(moods),
        "tempo": weighted_random_choice(tempos),
    }
    return track_config
