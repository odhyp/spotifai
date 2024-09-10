from openai import OpenAI


def generate_track_aimlapi(api_key: str, system_prompt: str, user_prompt: str):
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
