from pypdf import *
import dotenv
import os
import requests

dotenv.load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
voice_id = os.getenv("VOICE_ID")

pdf_reader = PdfReader('./Gs_Resume.pdf')

text_chunks=[]
# print(f"total number of pages:{len(pdf_reader.pages)}")

full_text = ""

for page in pdf_reader.pages:
    full_text += page.extract_text()
# print(full_text)

for i in range(0, len(full_text), 500):
    block = full_text[i:i+500]

    text_chunks.append(block)


url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

headers = {
    "xi-api-key": f"{api_key}",
    "Content-Type": "application/json"
}

for index, chunk in enumerate(text_chunks):
    data = {
        "text": f"{chunk}",
        "model_id": "eleven_multilingual_v2"
    }

    response = requests.post(
        url,
        headers=headers,
        json=data,

    )

    print("Characters extracted:", len(chunk))
    print("Status code:", response.status_code)

    if response.status_code == 200:
        filename = f"audio_{index}.mp3"
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(response.text)
        break
