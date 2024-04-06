import os
from gtts import gTTS
import sys
import subprocess
import pygame

def text_to_speech(text, language='en', output_file='FinalSummary.wav'):
    if text:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(output_file)
        play_audio(output_file)
    else:
        print("No text to speak.")

def play_audio(audio_file):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing audio: {e}")

file_path = "FinalSummary.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        text_to_speech(content)
        subprocess.run(["xdg-open", "FinalSummary.wav"])
        sys.exit(0)
else:
    print(f"Error: File not found - {file_path}")
    sys.exit(1)
