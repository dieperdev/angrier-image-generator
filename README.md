# Angrier Image Generator

### Have you ever seen videos like [this one](https://youtube.com/watch?v=aipPMzSCL3w)? They pop up very frequently and have often become very annoying. I decided to create this to automate it (without GPT-4).

### Note: The program doesn't support multiple line images. Prompts are kind of janky, so prompt answers are sometimes long.

# Requirements
- Python
- FFmpeg (https://www.ffmpeg.org/download.html)
- OpenAI API Key
- Optional: ElevenLabs API Key

# Setup
- Clone the repository
- Run `pip install -r requirements.txt`
- Configure environment variables (rename `.env.example` to `.env`)
- Choose an image to go into `assets/you.jpg`
- Optional: You can add a watermark to your video by using the `watermark_text` environment variable

# Execution
### Run `python main.py`. The output video should be in `out/output.mp4` (default)