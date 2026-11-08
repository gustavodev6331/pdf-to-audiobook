# PDF to Audiobook

A Python application that extracts text from PDF documents and converts it into speech using the ElevenLabs Text-to-Speech API. The application splits extracted text into smaller chunks and generates individual MP3 audio files.

## Screenshot

<img width="1469" height="821" alt="Screenshot 2026-11-08 at 3 49 48 PM" src="https://github.com/user-attachments/assets/aa653a68-8c8f-41d1-a46c-9315922afa26" />


## Features

- Extracts text from PDF documents using PyPDF.
- Converts text into speech using the ElevenLabs API.
- Splits large texts into smaller chunks to handle API request limits.
- Generates separate MP3 files for each text chunk.
- Uses environment variables to securely store API credentials.
- Handles unsuccessful API requests and stops processing when an error occurs.

## Technologies Used

- Python
- PyPDF
- Requests
- Python-dotenv
- ElevenLabs Text-to-Speech API

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/gustavodev6331/pdf-to-audiobook.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pdf-to-audiobook
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Install the dependencies:

   ```bash
   pip install pypdf requests python-dotenv
   ```

## Configuration

Create a `.env` file in the project root directory and add your ElevenLabs credentials:

```env
ELEVENLABS_API_KEY=your_api_key
VOICE_ID=your_voice_id
```

You can obtain your API key and voice ID from your ElevenLabs account.

## Usage

1. Place your PDF file in the project directory.
2. Update the PDF path in `main.py` if necessary.
3. Run the application:

   ```bash
   python main.py
   ```

4. The application extracts the PDF text, divides it into chunks of 500 characters, and sends each chunk to the ElevenLabs API.
5. Successfully generated audio files are saved in the project directory:

   ```text
   audio_0.mp3
   audio_1.mp3
   audio_2.mp3
   ```

Each MP3 file contains the audio generated from its corresponding text chunk.

## Notes

- An active ElevenLabs account and available API credits are required.
- Audio generation depends on the API's usage limits and available quota.
- The application generates separate MP3 files rather than combining them into a single audio file.
- The PDF must contain extractable text. Scanned documents may require OCR processing.
