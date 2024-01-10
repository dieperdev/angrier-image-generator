import os
import json

from pathlib import Path
from glob import glob
from yt_dlp import YoutubeDL

def download_assets() -> None:
    Path('assets/background-videos').mkdir(parents=True, exist_ok=True)
    Path('assets/background-audios').mkdir(parents=True, exist_ok=True)
    
    video_config_file = open('video_config.json', 'r')
    video_config_data = video_config_file.read()
    video_config_file.close()
    
    video_config_json = json.loads(video_config_data)
    
    background_videos = video_config_json['background_videos']
    background_audios = video_config_json['background_audios']
    
    if len(background_videos) != len(glob('assets/background-videos/*.mp4')):
        for i in range(len(background_videos)):
            ydl_opts = {
                'outtmpl': f'assets/background-videos/background-video-{str((i + 1))}.mp4',
                'format': 'best[height<=1080]/best[height<=720]/best/ext=mp4',
                'extract_audio': False,
            }
            
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(background_videos[i])

        print('Downloaded all background videos!')
    else:
        print('You already have all the background videos downloaded! Nice 😎.')
    
    if len(background_audios) != len(glob('assets/background-audios/*.mp3')):
        for i in range(len(background_audios)):
            ydl_opts = {
                'outtmpl': f'assets/background-audios/background-audio-{str((i + 1))}.%(ext)s',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'extract_audio': True
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(background_audios[i])

        print('Downloaded all background audios!')
    else:
        print('You already have all the background audios downloaded! Nice 😎.')