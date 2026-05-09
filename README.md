# AI Doctor VoiceBot (Vision + Voice)

This is a Gradio-based “AI Doctor” demo that:
- Takes **an image** of a skin condition
- Takes **patient audio** from your microphone
- Uses **Groq** for **speech-to-text (STT)** and for **multimodal image + text analysis**
- Converts the doctor response to **speech** using **gTTS** (ElevenLabs support was disabled in this environment)

> Note: This project is for learning/testing only. It is not a medical device.

---

## Demo URL (local)
After running, open the URL printed by Gradio, typically:
- http://127.0.0.1:7860

---

## Features
- Speech-to-text (Groq Whisper via Groq API)
- Image understanding + diagnosis-style response (Llama vision via Groq)
- Text-to-speech output (gTTS)
- Simple Gradio UI (microphone + image upload)

---

## Project Structure
- `gradio_app.py` — Gradio UI and main `process_inputs()` flow
- `voice_of_the_patient.py` — microphone recording + Groq transcription
- `brain_of_the_doctor.py` — encode image + analyze with a vision model
- `voice_of_the_doctor.py` — text-to-speech (gTTS). (ElevenLabs methods disabled)

---

## Requirements
### Python packages
This repo uses a `Pipfile` (pipenv):
- `speechrecognition`
- `pydub`
- `gtts`

Additional runtime deps come from imports in the code (e.g., `gradio`, `groq`).

### System dependencies
- **ffmpeg** (needed by pydub / ffplay)

### Microphone note (PyAudio)
The app may show:
- `Could not find PyAudio; check installation`

That warning affects microphone recording only. The rest of the pipeline can still work if audio input is provided.

---

## Setup
### 1) Install dependencies
From the project folder:

```bat
pip install pipenv
pipenv install
```

### 2) Add environment variables
Create a file named `.env` in the project root and set:

```env
GROQ_API_KEY=your_groq_api_key
```

> For ElevenLabs, the current environment disables it, so `ELEVEN_API_KEY` is not required.

---

## Run the project
Start Gradio:

```bat
pipenv run python gradio_app.py
```

Then open the printed local URL in your browser.

---

## How to use (UI)
1. Click/record audio using the microphone input
2. Upload an image (skin photo)
3. Submit
4. View:
   - Speech-to-text
   - Doctor response text
   - Generated audio output

---

## Troubleshooting
### 1) PyAudio missing
If you get `Could not find PyAudio`:
- Install PyAudio (Windows wheels are often easiest)
- Or run without live microphone recording

### 2) Port already in use
If you already have a Gradio server running, it may switch ports (e.g. 7861). Open the latest URL shown in terminal.

### 3) API key errors
If Groq calls fail, verify `GROQ_API_KEY` in `.env`.

---

## Security note
Do **not** commit your real API keys to GitHub.
Add `.env` to `.gitignore`.

---

## License
You can add your preferred license here (e.g., MIT).

Build with learning from AIwithhassan.
