import random
import json

from utils.generate_text import generate_text

video_config_file = open('video_config.json', 'r')
video_config_data = video_config_file.read()
video_config_file.close()

video_config_json = json.loads(video_config_data)

unavailable_texts = video_config_json['unavailable_texts']

def pick_unavailable(item: str) -> str:
    random_text = unavailable_texts[random.randint(0, (len(unavailable_texts) - 1))]
    random_text_formatted = random_text.replace('<INSERT_ITEM>', item)
    random_text_variation = generate_text(prompt=f'Generate a variation of this text while still maintaining it\'s meaning: {str(random_text_formatted)}')
    
    return random_text_variation