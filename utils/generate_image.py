import os
import requests
import openai

from pathlib import Path
from dotenv import main

main.load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def generate_image(prompt: str, output: str) -> str:
    Path('assets/temp/images').mkdir(parents=True, exist_ok=True)
    
    if os.path.isfile(f'assets/temp/images/{str(output)}.png'):
        try:
            os.remove(f'assets/temp/images/{str(output)}.png')
        except:
            pass

    image = openai.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1
    ).data[0].url
    
    request = requests.get(image)
    image_data = request.content
    image_file = open(f'assets/temp/images/{str(output)}.png', 'wb')
    image_file.write(image_data)
    image_file.close()
    
    return f'assets/temp/images/{str(output)}.png'