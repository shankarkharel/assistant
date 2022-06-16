import pyttsx3
import datetime
# import speech_recognition as sr
import wikipedia
import webbrowser
# import os
# import smtplib
# import pythoncom
import requests

res = requests.get('https://ipinfo.io/')
data = res.json()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# print(voices[1].id)

# print(voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hrs = int(datetime.datetime.now().hour)

    if hrs >= 12 and hrs < 0:
        speak("good morning!")
    elif hrs >= 0 and hrs < 5:
        speak("good afternoon!")
    elif hrs > 5 and time < 8:
        speak('good evening!')
    else:
        speak("hello there!")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threashold = 3
        audio = r.listen(source)

    query = None
    try:
        print("recogniting...")
        query = r.recognize_google(audio, language='en-uk')

        print(f"user said : {query}\n")
    except Exception as e:
        speak("please say that again..")
        query = None

    return query


# program starts.
speak("i am assistant to this device.")
speak('how can i help you?')
wishme()

query = takecommand()

# logic for executing task.
if 'exit' in query.lower():
    say('thank you!')

elif 'Wikipedia' in query:
    speak("searching wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=3)
    speak(results)

elif 'open youtube' in query.lower():
    speak('opening youtube')
    webbrowser.open("youtube.com")
elif 'open facebook' in query.lower():
    speak('facebook is opening')
    webbrowser.open("https://www.facebook.com/")
elif 'Google' in query:
    speak('browsing to google.com')
    webbrowser.open("google.com")
elif 'location' in query.lower():
    speak('opening google maps')
    webbrowser.open('www.google.com/maps')
