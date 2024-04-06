import requests
import os
from time import sleep

API_key = "8fa93c3add204b758e44c50f42ba1439"

headers = {
    'authorization': API_key,
    'content-type': 'application/json',
}

upload_endpoint = 'https://api.assemblyai.com/v2/upload'
transcription_endpoint = "https://api.assemblyai.com/v2/transcript"

def upload(file_path):
    def read_audio(file_path):
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(5_242_880)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers, data=read_audio(file_path))

    return upload_response.json().get('upload_url')

def transcribe(upload_url):
    json_data = {"audio_url": upload_url, "auto_chapters": True}
    response = requests.post(transcription_endpoint, json=json_data, headers=headers)
    transcription_id = response.json()['id']
    return transcription_id

def get_result(transcription_id):
    current_status = "queued"
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcription_id}"

    while current_status not in ("completed", "error"):
        response = requests.get(endpoint, headers=headers)
        current_status = response.json()['status']

        if current_status in ("completed", "error"):
            return response.json()
        else:
            sleep(10)

upload_url = upload("speech.wav")
transcription_id = transcribe(upload_url)
response = get_result(transcription_id)

print(response["text"][:])

with open("speech.txt", "w") as file:
    file.write(response["text"][:])

summary = response["chapters"][0]['summary']

print("\nSummary:")
print(summary)

with open("FinalSummary.txt", "w") as output:
    output.write(summary)
