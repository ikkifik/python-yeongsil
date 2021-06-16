import webbrowser
import speech_recognition as sr
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()
mic = sr.Microphone()

def record_audio(ask=False):
    with mic as source:
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="en")
        except sr.UnknownValueError :
            speak("Sorry i didn't recognize that")
        return voice_data

def respond(voice_data):
    if "your name" in voice_data:
        speak("My name is yeongsil")
    if "search" in voice_data:
        search = record_audio("What do you want to search?")
        url = f"https://www.google.com/search?q={search}"
        webbrowser.get().open(url)
        speak("Here's what i found for " + search)
    if "go to somewhere" in voice_data:
        search = record_audio("Where do you want to go?")
        url = f"https://www.google.co.id/maps/search/{search}"
        webbrowser.get().open(url)
        speak("Here's what i found for " + search)
    if "thank you" in voice_data:
        speak("Your welcome")
        exit()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000)
    audio_file = f"audio-{r}.mp3"

    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)
speak("How can I help you?")

while 1:
    get_voice = record_audio()
    respond(get_voice)
    
