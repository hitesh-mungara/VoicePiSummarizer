from pydub import AudioSegment
import os
import sys

TEMP_DIR = "tempWAV"
MERGED_FILE = "speech.wav"

def merge_audio_files(directory):
    audio_files = [f for f in os.listdir(directory) if f.endswith(".wav")]

    if not audio_files:
        print("No audio files found in the directory.")
        return

    merged_audio = AudioSegment.silent()

    for audio_file in audio_files:
        file_path = os.path.join(directory, audio_file)
        sound = AudioSegment.from_wav(file_path)
        merged_audio += sound
        os.remove(file_path)

    merged_audio.export(MERGED_FILE, format="wav")
    print(f"Audio files merged successfully. Merged file saved as '{MERGED_FILE}'.")

merge_audio_files(TEMP_DIR)
sys.exit(0)