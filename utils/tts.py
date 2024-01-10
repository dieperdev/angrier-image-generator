import os
import string

from pathlib import Path
from utils.speed_audio import speed_up_audio
from dotenv import main
from gtts import gTTS
from elevenlabs import Voice, VoiceSettings, generate, save, set_api_key

main.load_dotenv()

elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')

if elevenlabs_api_key:
	set_api_key(elevenlabs_api_key)

def generate_audio(text: str, output: str, fast: bool = False) -> str:
	Path('assets/temp/audio').mkdir(parents=True, exist_ok=True)

	if os.path.isfile(f'assets/temp/audio/{str(output)}.mp3'):
		try:
			os.remove(f'assets/temp/audio/{str(output)}.mp3')
		except:
			pass

	spedup_path = None
	cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

	if elevenlabs_api_key:
		audio = generate(
			text=cleaned_text,
			voice=Voice(
				voice_id='pNInz6obpgDQGcFmaJgB',
				settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
			)
		)

		if fast:
			save(audio, f'assets/temp/audio/{str(output)}.mp3')

			spedup_path = speed_up_audio(input=output)
		else:
			save(audio, f'assets/temp/audio/{str(output)}.mp3')
	else:
		audio = gTTS(cleaned_text)

		if fast:
			audio.save(f'assets/temp/audio/{str(output)}.mp3')

			spedup_path = speed_up_audio(input=output)
		else:
			audio.save(f'assets/temp/audio/{str(output)}.mp3')

	if spedup_path:
		return spedup_path

	return f'assets/temp/audio/{str(output)}.mp3'