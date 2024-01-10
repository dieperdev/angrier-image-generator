from pathlib import Path
from pydub import AudioSegment

def speed_up_audio(input: str) -> str:
    Path('assets/temp/audio').mkdir(parents=True, exist_ok=True)

    audio = AudioSegment.from_file(f'assets/temp/audio/{str(input)}.mp3', format='mp3')
    audio = audio.speedup(playback_speed=2.0)

    # export to mp3
    audio.export(f'assets/temp/audio/{str(input)}-speedup.mp3', format='mp3')

    return f'assets/temp/audio/{str(input)}-speedup.mp3'