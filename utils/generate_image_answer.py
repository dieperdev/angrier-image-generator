import os

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype(font='fonts/Halbfett.ttf')

def generate_image_answer(image: str, answer: str, output: str) -> str:
    Path('assets/temp/answers').mkdir(parents=True, exist_ok=True)
    
    if os.path.isfile(f'assets/temp/answers/{str(output)}.png'):
        try:
            os.remove(f'assets/temp/answers/{str(output)}.png')
        except:
            pass
    
    img = Image.new('RGB', (315, 345), color=(52, 53, 65))

    gpt4_profile = Image.open('assets/gpt4.png')
    gpt4_profile = gpt4_profile.resize(size=(15, 15))

    img.paste(gpt4_profile, (10, 10))
    
    gpt = ImageDraw.Draw(img)
    gpt.text(xy=(30, 3), text='ChatGPT', font=font, fill=(255, 255, 255))
    
    prompt_answer = ImageDraw.Draw(img)
    prompt_answer.text(xy=(30, 17), text=answer, fill=(255, 255, 255))

    image_generated = Image.open(image)
    image_generated = image_generated.resize(size=(300, 300))

    img.paste(image_generated, (10, 40))
    
    img.save(f'assets/temp/answers/{str(output)}.png')
    
    return f'assets/temp/answers/{str(output)}.png'