from g4f.client import Client
from g4f.Provider import Chatgpt4o, ChatgptFree, FreeChatgpt, FreeGpt, RetryProvider


def generate_track_basic(prompt: str):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def generate_track_rotate(prompt: str):
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
