import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as sourse:
        print("Clearing backgroud noises..Please wait..")
        recognizer.adjust_forambient_noices(source,duration=0.5)
        print("Ask Me Anything...")
        recordedaudio=recognizer.listen(source)

    try:
        command=recognizer.recoginze_google(recordedaudio)    