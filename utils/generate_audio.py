import random

from pathlib import Path
from glob import glob
from moviepy.editor import AudioFileClip

def generate_audio(duration: float) -> AudioFileClip:
    Path('assets/background-audios').mkdir(parents=True, exist_ok=True)
    
    random_audio = random.sample(glob('assets/background-audios/*.mp3'), 1)[0]
    random_audio_clip: AudioFileClip = AudioFileClip(random_audio)
    random_audio_clip: AudioFileClip = random_audio_clip.volumex(0.15)
    random_audio_clip: AudioFileClip = random_audio_clip.subclip(0, duration)

    return random_audio_clip