#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with Khushi!"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# ElevenLabs is optional. This project currently runs with gTTS to avoid
# ElevenLabs import/runtime issues in some Windows environments.
# import elevenlabs
# from elevenlabs.client import ElevenLabs

# ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")


def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    raise NotImplementedError("ElevenLabs disabled in this environment; use text_to_speech_with_gtts().")

    audio=client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",  
        model_id="eleven_multilingual_v2",
        text=input_text
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

# #Step2: Use Model for Text output to Voice
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):

    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text="Hi this is Ai with Khushi, autoplay testing!"
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    raise NotImplementedError("ElevenLabs disabled in this environment; use text_to_speech_with_gtts().")

    audio=client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",  
        model_id="eleven_multilingual_v2",
        text=input_text
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing_autoplay.mp3") 
