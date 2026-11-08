from pypdf import *
import dotenv
import os
import requests

dotenv.load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("VOICE_ID")

pdf_reader = PdfReader('./Gs_Resume.pdf')

# print(f"total number of pages:{len(pdf_reader.pages)}")

full_text = ""

for page in pdf_reader.pages:
    full_text += page.extract_text() + "\n"
# print(full_text)

url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

headers = {
    "xi-api-key": f"{api_key}",
    "Content-Type": "application/json"
}

data = {
    "text": f"{full_text}",
    "model_id": "eleven_multilingual_v2"
}


response = requests.post(
    url,
    headers=headers,
    json=data,

)

print("Characters extracted:", len(full_text))
print("Status code:", response.status_code)

with open("test_audio.mp3", "wb") as f:
    f.write(response.content)

