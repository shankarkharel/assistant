This code is able to wish good morning,good afternoon,good evening by using datetime module of python.
def wishme():
    hrs = int(datetime.datetime.now().hour)

    if hrs>=12 and hrs<0:
            speak("good morning!")
    elif hrs>=0 and hrs<5:
         speak("good afternoon!")
    elif hrs>5 and time<8:
        speak('good evening!')
    else:
            speak("hello there!")
it can listen to your instructions and convert them to text and print on scrren by writting user said...
def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threashold = 3 \\stops for 3 second until user say something.
        audio = r.listen(source)

    query = None
    try:
        print("recogniting...")
        query = r.recognize_google(audio,language='en-uk')

        print(f"user said : {query}\n")
    except Exception as e:
        query = None
        speak("please say that again..")
        

    return query \\query is what the user said.

this can open youtube,google,map.
#logic for executing task.
if 'exit'in query.lower():
        say('thank you!')

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


This is also able to search any thing on wikipedia and read out 3 sentences.
elif 'Wikipedia' in query:
    speak("searching wikipedia....")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=3)
    speak(results)
insall and import the following modules as shown for running this in your python environment.
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pythoncom.
