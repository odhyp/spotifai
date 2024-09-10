def clean_prompt(prompt: str):
    cleaned_prompt = prompt.strip('"""')
    cleaned_prompt = " ".join(line.strip() for line in cleaned_prompt.splitlines())
    cleaned_prompt = " ".join(cleaned_prompt.split())
    return f'"{cleaned_prompt}"'


def generate_prompt(track_config: dict):
    genre = track_config["genre"]
    era = track_config["era"]
    popularity = track_config["popularity"]
    artist = track_config["artist"]
    country = track_config["country"]
    mood = track_config["mood"]
    tempo = track_config["tempo"]

    main_prompt = f"""
        Generate just 1 (one) music recommendation for a {genre} song \
        released in the {era} by {popularity} {artist} from {country}, \
        focusing on {mood} mood with {tempo} tempo! Only the artist name and the track title please.
    """

    additional_prompt = """
        In addition, write a brief fact about the artist or the track itself, \
        and provide a "mood" which is a short sentence to describe on what ocassion \
        is suitable to listen to the song!
    """

    limitation_prompt = """Your resulting message should be separated between lines. \
        1st line Artist: artist_name, 2nd line Track: track_name, 3rd line Mood: mood, \
        4th line Fact: facts!
    """

    raw_prompt = f"{main_prompt}{additional_prompt}{limitation_prompt}"
    return clean_prompt(raw_prompt)
