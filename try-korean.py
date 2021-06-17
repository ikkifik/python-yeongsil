# KOREAN VERSION

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
        r.adjust_for_ambient_noise(source, duration=0.7)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language="ko")
        except sr.UnknownValueError :
            speak("인식하지 못해서 죄송합니다")
        return voice_data

def respond(voice_data):
    if "영실아" in voice_data:
        speak("네 알겠습니다")
    if "당신의 이름" in voice_data:
        speak("저는 영실입니다")
    if "검색" in voice_data:
        search = record_audio("무엇을 검색 하시겠습니까?")
        url = f"https://www.google.com/search?q={search}"
        webbrowser.get().open(url)
        speak("내가 찾은 내용은 다음과 같습니다. " + search)
    if "나는 어딘가에 가고 싶다" in voice_data:
        search = record_audio("어디 가요?")
        url = f"https://www.google.co.id/maps/search/{search}"
        webbrowser.get().open(url)
        speak("내가 찾은 내용은 다음과 같습니다. " + search)
    if "감사합니다" in voice_data:
        speak("천만에요")
        exit()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='ko')
    r = random.randint(1, 10000)
    audio_file = f"audio-{r}.mp3"

    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)

while 1:
    get_voice = record_audio()
    respond(get_voice)
    
