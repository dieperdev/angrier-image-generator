import random

from pathlib import Path
from glob import glob
from moviepy.editor import VideoClip, VideoFileClip, concatenate_videoclips

def generate_backgrounds(duration: float) -> VideoClip:
    Path('assets/background-videos').mkdir(parents=True, exist_ok=True)
    
    videos = []
    trimmed_videos = []
    
    for filename in glob('assets/background-videos/*.mp4'):
        video: VideoFileClip = VideoFileClip(filename)
        video: VideoFileClip = video.without_audio()
        
        videos.append(video)
        
    for video in videos:
        trim_start = random.uniform(60, (video.duration - 120))
        trim_end = min(video.duration, (trim_start + (duration / len(videos))))
        
        trimmed_video: VideoFileClip = video.subclip(trim_start, trim_end)
        
        trimmed_videos.append(trimmed_video)
    
    trimmed_videos_combined: VideoClip = concatenate_videoclips(trimmed_videos)
    
    return trimmed_videos_combined