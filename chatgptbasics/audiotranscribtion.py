from openai import OpenAI
import os

apikey = os.getenv("ChatGPTKEY")
os.environ['OPENAI_API_KEY'] = apikey
OpenAI.api_key = apikey

client = OpenAI()

audio_file = open("../../Resources/test.mp3", "rb")

print("Transcribing audio...")
response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

print(response)