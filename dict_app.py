import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp = {"cmd": "cmd", "paint": "mspaint", "word": "winword",
           "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt","calculator":"calc"}


def openappweb(query):
    speak("Launching, Sir")
    if ".com" in query or ".in" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def closeappweb(query):
    speak("Closing, Sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("One tab closed")
    elif "two tabs" in query or "2 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Two tabs closed")
    elif "three tabs" in query or "3 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Three tabs closed")
    elif "four tabs" in query or "4 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Four tabs closed")
    elif "five tabs" in query or "5 tabs" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("Five tabs closed")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                speak(f"{dictapp[app]} closed")
