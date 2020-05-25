import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pythoncom
import requests
res = requests.get('https://ipinfo.io/')
data = res.json()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices[1].id)

#print(voices)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morning!")
        elif hour>12 and hour<18:
         speak("good afternoon!")
        else:
            speak("good evening")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threashold = 2
        audio = r.listen(source)

    query = None
    try:
        print("recogniting...")
        query = r.recognize_google(audio,language='en-in')

        print(f"user said : {query}\n")
    except Exception as e:
        print("please say that again..")
        query = None
    return query



if __name__ == '__main__':
    speak("i am assistant to this device coded by shankar.")
wishme()
query = takecommand()

if 'wikipedia' in query.lower():
    speak("searching wikipedia....")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=3)
    speak(results)

elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com")
elif 'open facebook' in query.lower():
    webbrowser.open("www.facebook.com")
elif 'open google' in query.lower():
    webbrowser.open("www.google.com")
elif 'my location' in query.lower():
    webbrowser.open('www.google.com/maps')

