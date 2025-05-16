from gtts import gTTS
import os

def generate_audio(text, filename="output_audio.mp3"):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        print(f"✅ Audio saved as {filename}")
        return filename
    except Exception as e:
        print("Error generating audio:", e)
        return None
