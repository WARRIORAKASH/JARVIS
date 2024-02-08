import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def latestnews():
    api_dict = {"business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=9cd4052a05634f24bb2d7ad739e376b8",
                "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=9cd4052a05634f24bb2d7ad739e376b8",
                "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=9cd4052a05634f24bb2d7ad739e376b8",
                "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=9cd4052a05634f24bb2d7ad739e376b8",
                "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=9cd4052a05634f24bb2d7ad739e376b8",
                "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=9cd4052a05634f24bb2d7ad739e376b8"
                }
    url = None
    speak(
        "Which field news do you want, [business], [entertainment], [health], [science], [sports], [technology]")
    field = input("Type the proper field you want : ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"For more info visit : {news_url}")

        speak("Press 1 to continue and press 2 to stop")
        a = input("[Press 1 to continue] and [Press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
    speak("Thats all")