import speech_recognition as sr
from time import ctime, sleep
import webbrowser

r = sr.Recognizer()

def record_audio(ask = False): 
    with sr.Microphone() as source:
        if ask:
            print(ask)
        # r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_sphinx(audio, language="ko")
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
        except sr.RequestError:
            print('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print('My Name is Yeongsil')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = f"https://www.google.com/search?q={search}"
        webbrowser.get().open(url)
        print("Here's what i found for" + search)
    if 'search youtube' in voice_data:
        search = record_audio('What do you want to watch')
        url = f"https://www.youtube.com/results?search_query={search}"
        webbrowser.get().open(url)
    if 'exit' in voice_data:
        exit()

sleep(1)
print('How can i help you?')

while(1):
    voice_data = record_audio()
    respond(voice_data)
