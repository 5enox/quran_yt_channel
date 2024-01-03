'''
I came across a video in facebook shorts and decided to make this script to make an automated youtube channel for quran
should be both hard and fun and helpful, alhamdulilah
#############################
for now I'm planning on looking for an api or just scrape the quran off of a website i just found 
and use speec recognition to get which verse is been read at when and use moviepy to edit a nice UI ofr the video incha allah
then It's either youtube api or selenium to upload the final video, hope this will go as planned.
'''
import requests
import base64

with open("audio.wav", "rb") as f:
    base64_encoded_data = base64.b64encode(f.read()).decode("utf-8")


response = requests.post(
    "https://ics-dev1-speech-to-text-quran.hf.space/run/predict",
    json={
        "data": [
            {"name": "audio.wav", "data": base64_encoded_data}
        ]
    }
)

data = response.json()["data"]
