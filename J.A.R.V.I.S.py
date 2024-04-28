import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import time
import os
import requests
from bs4 import BeautifulSoup
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer
import speedtest
import cv2
from PIL import Image
import pytesseract

for i in range(3):
    a = input("Enter Password to open JARVIS : ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if a == pw:
        print("Access Granted !👍")
        print("WELCOME SIR! PLZ SPEAK [ WAKE UP JARVIS ] TO LOAD ME UP")
        break
    elif a != pw:
        print("Try Again")
    elif i == 2 and a != pw:
        exit()

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


def alarm(query):
    timehere = open("alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def tell_joke():
    try:
        # You can customize the joke category
        joke = pyjokes.get_joke(category='all')
        print(joke)
        speak(joke)
    except pyjokes.pyjokes.PyJokesException:
        speak("Sorry, I couldn't fetch a joke at the moment.")


# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('ajjubhai94ina@gmail.com', 'ajjubhaiakash*')
#     server.sendmail('ajjubhai94ina@gmail.com', to, content)
#     server.close()


if __name__ == "__main__":
    while True:
        # if 1:
        query = takeCommand().lower()
        # Wake up JARVIS
        if "wake up jarvis" in query:
            from wake_up import wakeup
            wakeup()
            while True:
                query = takeCommand().lower()
                # Sleep JARVIS
                if "go to sleep jarvis" in query:
                    speak("Ok sir, You can call me any time.")
                    break

                # Quit JARVIS
                elif "quit jarvis" in query:
                    speak("Ok Sir.")
                    exit()

                # Change Password
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the New Password : ")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    print("Done sir")
                    speak("Done sir")

                # Conversations
                elif "hello" in query:
                    speak("Hello Sir, how are you?")
                elif "i am fine" in query:
                    speak("That's great sir.")
                elif "how are you" in query:
                    speak("Perfect sir.")
                elif "thank you" in query:
                    speak("You're welcome sir.")

                # Open & Close Apps or Websites
                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("jarvis", "")
                    query = query.replace("application", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                elif "open" in query:
                    from dict_app import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dict_app import closeappweb
                    closeappweb(query)

                # Web Query
                elif "google" in query:
                    from web_search import searchgoogle
                    searchgoogle(query)
                elif "youtube" in query:
                    from web_search import searchYoutube
                    searchYoutube(query)
                # elif "wikipedia" in query:
                #     from web_search import searchWikipedia
                #     searchWikipedia(query)

                # Weather & Temperature
                elif "temperature" in query or "weather" in query:
                    from weather import get_weather
                    openweathermap_api_key = 'e266ac1b2b549cfa01ba6305258ee391'
                    city_name = 'Kolkata'  # Replace this with the desired city name
                    weather_info = get_weather(
                        openweathermap_api_key, city_name)

                    if weather_info:
                        print(f"Weather in {city_name}:")
                        speak(f"Current Weather in {city_name}")
                        print(f"Description: {weather_info['description']}")
                        speak(f"Description: {weather_info['description']}")
                        print(f"Temperature: {weather_info['temperature']}°C")
                        speak(f"Temperature: {
                              weather_info['temperature']}°Celcius")
                        print(f"Humidity: {weather_info['humidity']}%")
                        speak(f"Humidity: {weather_info['humidity']}%")
                    else:
                        print("Unable to fetch weather information.")
                        speak("Unable to fetch weather information.")

                # Alarm
                elif "set an alarm" in query:
                    print("Input time Example:- 10 and 10 and 10")
                    speak("Please input the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done Sir")

                # YT control
                elif "play" in query or "pause" in query:
                    pyautogui.press("k")
                    if query == "play":
                        speak("Video played")
                    elif query == "pause":
                        speak("Video paused")
                elif "mute" in query or "unmute" in query:
                    pyautogui.press("m")
                    if query == "mute":
                        speak("Video muted")
                    elif query == "unmute":
                        speak("Video unmuted")
                elif "volume up" in query or "volume down" in query:
                    if query == "volume up":
                        from keyboard import volumeup
                        speak("Turning volume up, sir")
                        volumeup()
                    elif query == "volume down":
                        from keyboard import volumedown
                        speak("Turning volume down, sir")
                        volumedown()

                # To Do
                elif "remember that" in query:
                    ToDo = query.replace("remember that", "")
                    ToDo = query.replace("jarvis", "")
                    speak("You told me"+ToDo)
                    task = open("todo.txt", "w")
                    task.write(ToDo)
                    task.close()
                elif "what do you remember" in query:
                    task = open("todo.txt", "r")
                    speak("You told me"+task.read())

                # Play Song
                elif "tired" in query:
                    speak("Playing your favourite song")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://youtu.be/4mLAIoqLYuQ")
                    elif b == 2:
                        webbrowser.open("https://youtu.be/h1PMLoiiliA")
                    elif b == 3:
                        webbrowser.open("https://youtu.be/7I_sq3umvQc")

                # News
                elif "news" in query:
                    from news import latestnews
                    latestnews()

                # Calculator
                elif "calculate" in query:
                    from calc_num import WolfRamAlpha
                    from calc_num import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                # Time Query
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")

                # WhatsApp Automation
                # elif "whatsapp" in query:
                #     from whatsapp import sendMessage
                #     sendMessage()

                # Media Query
                elif "play lucifer" in query:
                    luci_dir = "D:\\Movies&WebSeries\\Lucifer\\S1"
                    series = os.listdir(luci_dir)
                    print(series)
                    os.startfile(os.path.join(luci_dir, series[0]))

                # Shutdown System
                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown the system")
                    shutdown = input(
                        "Are you wish to shutdown your computer (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                # My Schedule
                elif "schedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks (Please say Yes or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write("")
                        file.close()
                        speak("Enter the number of tasks you have")
                        no_tasks = int(
                            input("Enter the number of tasks you have: "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task : "))
                            file = open("tasks.txt", "w")
                            file.write(f"{tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        speak("Enter the number of tasks you have")
                        no_tasks = int(
                            input("Enter the number of tasks you have: "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task : "))
                            file = open("tasks.txt", "a")
                            file.write(f"{tasks[i]}\n")
                            file.close()
                elif "notify about my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.wav")
                    mixer.music.play()
                    notification.notify(
                        title="My Schedule : ",
                        message=content,
                        # timeout=15
                    )

                # Internet speed testchrome
                elif "internet speed" in query:
                    print("Please Wait ⏳")
                    speak("Please Wait")
                    wifi = speedtest.Speedtest()
                    download_net = wifi.download()
                    upload_net = wifi.upload()
                    print(f"Download Speed : {download_net/1048576:.2f} Mbps")
                    print(f"Upload Speed : {upload_net/1048576:.2f} Mbps")
                    speak(f"Download Speed : {download_net/1048576:.2f} Mb ps")
                    speak(f"Upload Speed : {upload_net/1048576:.2f} Mb ps")

                # IPL Score
                # elif "cricket score" in query:
                #     url="https://www.cricbuzz.com/"
                #     page=requests.get(url)
                #     soup=BeautifulSoup(page.text,"html.parser")
                #     team1=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                #     team2=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                #     team1_score=soup.find_all(class_="cb-ovr-flo")[8].get_text()
                #     team2_score=soup.find_all(class_="cb-ovr-flo")[10].get_text()
                #     a=print(f"{team1} : {team1_score}")
                #     b=print(f"{team2} : {team2_score}")
                #     notification.notify(
                #         title="Cricket Score",
                #         message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                #         # timeout=10
                #     )

                # Screenshot
                elif "screenshot" in query:
                    from screenshot import take_screenshot
                    take_screenshot()

                # Jokes
                elif "joke" in query:
                    tell_joke()
                    # Application Query
                    # elif "open application" in query:
                    #     speak("Which application should I open for you, sir?")
                    #     App_query = takeCommand().lower()
                    #     if "whatsapp" in App_query:
                    #         codePath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2252.7.0_x64__cv1g1gvanyjgm\\WhatsApp.exe"
                    #         os.startfile(codePath)

                    #     elif "file explorer" in App_query:
                    #         codePath = "C:\\Users\\AKASH\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\File Explorer.lnk"
                    #         os.startfile(codePath)

                # Email
                elif "send email" in query:
                    from sendmail import send_email
                    speak("Whom do you want to email")
                    to_email = input("Enter the Recipient email : ")
                    speak("Enter subject")
                    subject = input("Enter Subject : ")
                    speak("Enter email body")
                    body = input("Enter Email Body : ")
                    send_email(subject, body, to_email)

                # Image to Text
                elif "read" in query:
                    camera = cv2.VideoCapture(0)
                    while True:
                        _, image = camera.read()
                        cv2.imshow('Text detection', image)
                        if cv2.waitKey(1) & 0xFF == ord('s'):
                            cv2.imwrite('image.jpg', image)
                            break
                    camera.release()
                    cv2.destroyAllWindows()

                    def tesseract():
                        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                        Imagepath = "image.jpg"
                        pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
                        text = pytesseract.image_to_string(
                            Image.open(Imagepath))
                        print(text[:-1])
                        speak(text[:-1])
                    tesseract()

                # QR Code
                elif "qr" in query:
                    cap = cv2.VideoCapture(0)
                    detector = cv2.QRCodeDetector()
                    while True:
                        _, img = cap.read()
                        data, _, _ = detector.detectAndDecode(img)

                        if data:
                            a = data
                            break
                        cv2.imshow('QR Code Scanner', img)
                        if cv2.waitKey(1) == ord('q'):
                            break
                    if a:
                        webbrowser.open(str(a))
                    cap.release()
                    cv2.destroyAllWindows()

                # Multi Language Translator
                elif "translate" in query:
                    pass