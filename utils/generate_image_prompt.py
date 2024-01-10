import os

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype(font='fonts/Halbfett.ttf')

def generate_image_prompt(prompt: str, output: str) -> str:
    Path('assets/temp/prompts').mkdir(parents=True, exist_ok=True)
    
    if os.path.isfile(f'assets/temp/prompts/{str(output)}.png'):
        try:
            os.remove(f'assets/temp/prompts/{str(output)}.png')
        except:
            pass
    
    img = Image.new('RGB', (400, 50), color=(52, 53, 65))

    you_profile = Image.open('assets/you.jpg')
    you_profile = you_profile.resize(size=(24, 24))

    you = ImageDraw.Draw(img)
    you.text(xy=(40, 7), text='You', font=font, fill=(255, 255, 255))
    
    prompt_text = ImageDraw.Draw(img)
    prompt_text.text(xy=(40, 22), text=prompt, fill=(255, 255, 255))

    img.paste(you_profile, (10, 10))

    img.save(f'assets/temp/prompts/{str(output)}.png')
    
    return f'assets/temp/prompts/{str(output)}.png'