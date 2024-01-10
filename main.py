import os
import random

from utils.clear_data import clear_data
from utils.pick_object import pick_random
from utils.pick_unavailable import pick_unavailable
from utils.download_assets import download_assets
from utils.generate_text import generate_text
from utils.generate_image import generate_image
from utils.generate_image_prompt import generate_image_prompt
from utils.generate_image_answer import generate_image_answer
from utils.generate_image_unavailable import generate_image_unavailable
from utils.tts import generate_audio
from utils.make_video import generate_video

os.system('cls' if os.name == 'nt' else 'clear')

clear_data()
download_assets()

def main():
    images_to_generate = random.randint(5, 7)
    data = []
    
    item = pick_random()
    
    angry_counter = 0

    for i in range(images_to_generate):
        if i == 0:
            image_generation_prompt = generate_text(prompt=f'Generate a prompt for an AI to show me an image of a {str(item)}. Include information about the thing being happy.')
            image_generation_answer = generate_text(prompt=f'Generate a response that an image generation AI would respond with like "Sure! Here\'s an image of a {str(item)}". The AI will respond to the prompt: "{str(image_generation_prompt)}"')
            image_generated = generate_image(prompt=image_generation_prompt, output=str(i))
            video_prompt_image = generate_image_prompt(prompt=image_generation_prompt, output=str(i))
            video_answer_image = generate_image_answer(image=image_generated, answer=image_generation_answer, output=str(i))
            
            image_generation_prompt_tts = generate_audio(text=image_generation_prompt, output=f'{str(i)}-prompt')
            image_generation_answer_tts = generate_audio(text=image_generation_answer, output=f'{str(i)}-answer')
            
            prompt_data = {
                'prompt': image_generation_prompt,
                'prompt_image': video_prompt_image,
                'prompt_audio': image_generation_prompt_tts,
                'answer': image_generation_answer,
                'answer_image': video_answer_image,
                'answer_audio': image_generation_answer_tts
            }
            
            data.append(prompt_data)
        elif i > 0 and i < (images_to_generate - 1):
            angry_counter += 1

            image_generation_prompt = generate_text(prompt=f'Generate a prompt for an AI to make an image of a {str(item)} angrier. The prompt must include "{str(item)}". Do not describe what should make the thing angry, rather express in a yelling manner about how angry you want the {str(item)} to be. Repeat the word "angrier" {str(angry_counter)} times in your prompt. The prompt should be short and concise enough that it should be able to be read in 5 seconds and on one line.')
            image_generation_answer = generate_text(prompt=f'Generate a response that an image generation AI would respond with like "Here\'s an image of a {str(item)} being very angry". The AI will respond to the prompt: "{str(image_generation_prompt)}". The AI\'s answer should include "{str(item)}" and describe the anger in a very short way. The AI\'s answer short and concise enough that it should be able to be read in 5 seconds and on one line.')
            image_generated = generate_image(prompt=image_generation_prompt, output=str(i))
            video_prompt_image = generate_image_prompt(prompt=image_generation_prompt, output=str(i))
            video_answer_image = generate_image_answer(image=image_generated, answer=image_generation_answer, output=str(i))
            
            image_generation_prompt_tts = generate_audio(text=image_generation_prompt, output=f'{str(i)}-prompt')
            image_generation_answer_tts = generate_audio(text=image_generation_answer, output=f'{str(i)}-answer')
            
            prompt_data = {
                'prompt': image_generation_prompt,
                'prompt_image': video_prompt_image,
                'prompt_audio': image_generation_prompt_tts,
                'answer': image_generation_answer,
                'answer_image': video_answer_image,
                'answer_audio': image_generation_answer_tts
            }
            
            data.append(prompt_data)
        elif i == (images_to_generate - 1):
            angry_counter += 1

            image_generation_prompt = generate_text(prompt=f'Generate a prompt for an AI to make an image of a {str(item)} angrier. Do not describe what should make the thing angry, rather express in a yelling manner about how angry you want the {str(item)} to be. Repeat the word "angrier" {str(angry_counter)} times in your prompt. The prompt should be short and concise enough that it should be able to be read in 5 seconds and on one line.')
            image_generation_answer = pick_unavailable(item=item)            
            video_prompt_image = generate_image_prompt(prompt=image_generation_prompt, output=str(i))
            video_answer_image = generate_image_unavailable(image_text=image_generation_answer, output=str(i))
            
            image_generation_prompt_tts = generate_audio(text=image_generation_prompt, output=f'{str(i)}-prompt')
            image_generation_answer_tts = generate_audio(text=image_generation_answer, output=f'{str(i)}-answer', fast=True)
            
            prompt_data = {
                'prompt': image_generation_prompt,
                'prompt_image': video_prompt_image,
                'prompt_audio': image_generation_prompt_tts,
                'answer': image_generation_answer,
                'answer_image': video_answer_image,
                'answer_audio': image_generation_answer_tts
            }
            
            data.append(prompt_data)
    
    saved_video = generate_video(video_data=data, output='output')
    
    print(f'Saved output video to {str(saved_video)}')

if __name__ == '__main__':
    main()