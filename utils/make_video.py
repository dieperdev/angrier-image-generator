import os
import subprocess

from pathlib import Path
from utils.generate_backgrounds import generate_backgrounds
from utils.generate_audio import generate_audio
from moviepy.editor import TextClip, ImageClip, AudioFileClip, VideoClip, CompositeVideoClip, concatenate_videoclips
from moviepy.config import change_settings
from dotenv import main

main.load_dotenv()

# Read .env.example for more info
change_settings({ 'IMAGEMAGICK_BINARY': os.getenv('IMAGEMAGICK_PATH') })

watermark_text = os.getenv('WATERMARK_TEXT')

def generate_video(video_data: list, output: str) -> str:
    Path('out').mkdir(parents=True, exist_ok=True)
    
    videos = []
    
    for data in video_data:
        prompt_image: ImageClip = ImageClip(data['prompt_image'])
        prompt_audio: AudioFileClip = AudioFileClip(data['prompt_audio'])
        
        prompt_image: ImageClip = prompt_image.set_audio(prompt_audio)
        prompt_image: ImageClip = prompt_image.set_position(('center', 'center'))
        prompt_image: ImageClip = prompt_image.set_duration(prompt_audio.duration)
        
        answer_image: ImageClip = ImageClip(data['answer_image'])
        answer_audio: AudioFileClip = AudioFileClip(data['answer_audio'])
        
        answer_image: ImageClip = answer_image.set_audio(answer_audio)
        answer_image: ImageClip = answer_image.set_position(('center', 'center'))
        answer_image: ImageClip = answer_image.set_duration(answer_audio.duration)
        
        query_video: VideoClip = concatenate_videoclips([prompt_image, answer_image])
        
        videos.append(query_video)
        
    videos_combined: VideoClip = concatenate_videoclips(videos)
    videos_combined: VideoClip = videos_combined.set_position(('center', 'center'))
    
    background_audio: AudioFileClip = generate_audio(duration=videos_combined.duration)
    background_videos: VideoClip = generate_backgrounds(duration=videos_combined.duration)
    background_videos: VideoClip = background_videos.set_audio(background_audio)
    produced_content_video: CompositeVideoClip = CompositeVideoClip([background_videos, videos_combined])
    
    if watermark_text:
        watermark: TextClip = TextClip(watermark_text, fontsize=40, font='fonts/The Bold Font.ttf', color='white', stroke_color='black', stroke_width=2)
        watermark: TextClip = watermark.set_opacity(0.5)
        watermark: TextClip = watermark.set_position(('center', (produced_content_video.size[1] * 0.85)))
        watermark: TextClip = watermark.set_duration(videos_combined.duration)
        
        final_produced_video: CompositeVideoClip = CompositeVideoClip([produced_content_video, watermark])
    else:
        final_produced_video: CompositeVideoClip = produced_content_video
    
    if os.path.exists(f'out/{str(output)}.mp4'):
        try:
            os.remove(f'out/{str(output)}.mp4')
        except:
            pass
    
    final_produced_video.write_videofile(f'out/{str(output)}.mp4', threads=8, fps=30, codec='libx264', audio_codec='aac')
    
    try:
        final_produced_video.close()
    except:
        pass
    
    print('Processing with ffmpeg...')
    
    command = ['ffmpeg', '-i', f'out/{str(output)}.mp4', '-vf', 'crop=480:720', f'out/{str(output)}-cropped.mp4']
    
    subprocess.run(command, stderr=subprocess.DEVNULL)
    
    try:
        os.remove(f'out/{str(output)}.mp4')
        os.rename(f'out/{str(output)}-cropped.mp4', f'out/{str(output)}.mp4')
    
        return f'out/{str(output)}.mp4'
    except:
        return f'out/{str(output)}-cropped.mp4'