import threading
from pydub import AudioSegment
import pyaudio
import os
import sys

recording = True

FRAME_RATE = 16000
CHANNELS = 2
audionumber = 1

p = pyaudio.PyAudio()

recording = True

TEMP_DIR = "tempWAV"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

def get_valid_input_device():
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_info.get('maxInputChannels', 0) >= CHANNELS:
            return i
    return None

input_device_index = get_valid_input_device()

def record_and_save_audio(seconds=10, chunk=1024, audio_format=pyaudio.paInt16):
    global audionumber, recording, input_device_index

    while recording:
        try:
            stream = p.open(format=audio_format, channels=CHANNELS, rate=FRAME_RATE, input=True, frames_per_buffer=chunk, input_device_index=input_device_index)
            frames = []

            for i in range(0, int(FRAME_RATE / chunk * seconds)):
                data = stream.read(chunk)
                frames.append(data)

            stream.stop_stream()
            stream.close()

            sound = AudioSegment(
                data=b''.join(frames),
                sample_width=p.get_sample_size(audio_format),
                frame_rate=FRAME_RATE,
                channels=CHANNELS
            )

            filename = os.path.join(TEMP_DIR, f"temp{audionumber}.wav")
            sound.export(filename, format="wav")
            audionumber += 1

        except Exception as e:
            print(f"Error: {e}")

def stop_recording():
    global recording
    recording = False

print("Start speaking...")

recording_thread = threading.Thread(target=record_and_save_audio)

try:
    recording_thread.start()

    input("Press Enter to stop recording...")

except KeyboardInterrupt:
    print("Recording stopped by user.")
finally:
    stop_recording()
    recording_thread.join()
    p.terminate()
    sys.exit(0)