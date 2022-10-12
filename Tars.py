#from tkinter.tix import MAIN
#from pip import main
#import pyaudio
from datetime import datetime
from time import strftime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#import smtplib
import requests
from bs4 import BeautifulSoup
import pyautogui
import pywhatkit
from os import startfile
import pyjokes
# from pyautogui import click
# from keyboard import press
# from keyboard import write
# from time import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(f": {audio}")

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")

    speak("I am Tars! Your personal AI assistant! How may I help you?")


def closeApp():
    speak("okay!")

    if 'youtube' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'chrome' in query:
        os.system("TASKKILL /F /im chrome.exe")

    elif 'telegram' in query:
        os.system("TASKKILL /F /im telegram.exe")

    elif 'vs code' in query:
        os.system("TASKKILL /F /im code.exe")

    speak("successfully closed")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)

    except Exception as e:
        print(e)
        print("Say that again please!!")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()  # type: ignore
        if 'wikipedia' in query:
            speak('Searching wikipedia... Please wait')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'I am working on ' in query:
            speak("It is good to see you working .. I am very much glad to work with you.")

        elif 'how are you working today' in query:
            speak("I am okay! Thank you! I am currently working hard on my new features.")

        elif 'you need a break' in query:
            speak("sure maam!as you wish!")

        elif 'have a coffee' in query :
            speak("okay maam! do not forget your coffee too. It's good for human's health")

        elif 'open youtube' in query:
            speak("here we go")
            webbrowser.open("youtube.com")

        # elif 'open google' in query:
        #     speak("searching")
        #     webbrowser.open("google.com")

        elif 'launch website' in query:
            speak("which website")
            webname = takeCommand()
            web = 'https://www.' + webname + '.com'  # type: ignore
            webbrowser.open(web)
            speak("launched!!")

        elif 'open telegram' in query:
            speak("as your wish")
            telepath = (":\\Users\\soujanya\\AppData\\Roaming\\Telegram Desktop")
            os.startfile(telepath)

        # elif 'open discord' in query:
        #     speak("here we go")
        #     dispath = ("")
        #     os.startfile(telepath)


        elif 'play music' in query:
            speak("from where")
            location = takeCommand()
            music_dir = 'D:\\' + location   # type: ignore
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play a song' in query:
            speak("which song")
            songname = takeCommand()
            speak("here enjoy your song")
            pywhatkit.playonyt(songname)

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime} AM")

        elif 'open code' in query:
            speak("code again!!!")
            codepath = "E:\\Users\\soujanya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'temperature' in query:
            search = "temperature in kolkata"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current temperature is {temp}")

        elif 'screenshot' in query:
            speak("where should I save this?")
            path = takeCommand()
            pathname = path + ".png"
            path1 = "C:\\Users\\Windows 10\\OneDrive\\Pictures\\Screenshots\\" + pathname
            ss = pyautogui.screenshot()
            ss.save(path1)
            os.startfile("C:\\Users\\Windows 10\\OneDrive\\Pictures\\Screenshots")
            speak("saved!")

        elif 'tell me a joke' in query:
            jokes = pyjokes.get_joke('en', category= "neutral")
            #print(jokes)
            speak(jokes)

        elif 'chrome' in query:
            closeApp()
        
        elif 'youtube' in query:
            closeApp()

        elif 'vs code' in query:
            closeApp()

        elif 'telegram' in query:
            closeApp()

        elif 'bye' in query:
            speak("Bye maam! Call me anytime you need.")
        break
