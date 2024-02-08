import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wakeup():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour == 12:
        speak("Good Noon!")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Welcome back sir. Jarvis is at your service. How may I help you.")
