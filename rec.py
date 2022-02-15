import speech_recognition as sr
import pyttsx3
from os import path

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "poop.wav")
r = sr.Recognizer()


try:

    with sr.AudioFile(AUDIO_FILE) as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

        text = r.recognize_google(audio)
        text = text.lower()

        print(text)

except:

    pass