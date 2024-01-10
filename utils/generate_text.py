import os
import openai

from dotenv import main

main.load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def generate_text(prompt: str) -> str:
    return openai.completions.create(
        model='gpt-3.5-turbo-instruct',
		temperature=0,
		prompt=prompt,
		max_tokens=1000,
		n=1,
		stop=None
    ).choices[0].text.strip().replace('"', '')