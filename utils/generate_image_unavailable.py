import os
import json

from pathlib import Path
from utils.split_string import split_string
from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype(font='fonts/Halbfett.ttf')

video_config_file = open('video_config.json', 'r')
video_config_data = video_config_file.read()
video_config_file.close()

video_config_json = json.loads(video_config_data)

unavailable_texts = video_config_json['unavailable_texts']

def generate_image_unavailable(image_text: str, output: str) -> str:
    Path('assets/temp/answers').mkdir(parents=True, exist_ok=True)
    
    if os.path.isfile(f'assets/temp/answers/{str(output)}.png'):
        try:
            os.remove(f'assets/temp/answers/{str(output)}.png')
        except:
            pass
    
    img = Image.new('RGB', (300, 110), color=(52, 53, 65))

    gpt4_profile = Image.open('assets/gpt4.png')
    gpt4_profile = gpt4_profile.resize(size=(15, 15))

    img.paste(gpt4_profile, (10, 10))
    
    gpt = ImageDraw.Draw(img)
    gpt.text(xy=(30, 3), text='ChatGPT', font=font, fill=(255, 255, 255))
    
    image_text_split = split_string(text=image_text, max_length=50)
    
    y_offset = 0

    for text in image_text_split:
        prompt_answer = ImageDraw.Draw(img)
        prompt_answer.text(xy=(30, (17 + y_offset)), text=text, fill=(255, 255, 255))
        
        y_offset += 15

    img.save(f'assets/temp/answers/{str(output)}.png')
    
    return f'assets/temp/answers/{str(output)}.png'