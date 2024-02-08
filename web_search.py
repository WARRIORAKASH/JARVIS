import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia as wiki
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")
    except:
        print("Say that again please...")
        return "None"
    return query


query = takeCommand().lower()


def searchgoogle(query):
    if "google" in query:
        # import wikipedia as googleScrap
        speak("Searching from Google.")
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        try:
            pywhatkit.search(query)
            result = wiki.summary(query,2)
            speak("This is what I found on Google.")
            speak(result)
        except:
            speak("No result found")


def searchYoutube(query):
    if "youtube" in query:
        speak("Searching from YouTube...")
        query = query.replace("jarvis", "")
        query = query.replace("youtube search", "")
        query = query.replace("youtube ", "")
        web = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        speak("This is what I found on YouTube.")
        # pywhatkit.playonyt(query)


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from Wikipedia...")
        query = query.replace("jarvis", "")
        query = query.replace("search wikipedia", "")
        query = query.replace("wikipedia", "")
        results = wiki.summary(query,sentences=2)
        speak("This is what I found on Wikipedia.")
        # print(results)
        speak(results)
