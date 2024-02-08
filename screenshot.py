import pyttsx3
import pyautogui
import time

def speak(text):
    # Use text-to-speech to let Jarvis speak
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_screenshot(output_file="screenshot.png"):
    # Add a delay to give time to switch to the desired window or screen
    speak("I will take a screenshot in 5 seconds. Please switch to the desired window.")
    time.sleep(5)

    # Take a screenshot and save it to the specified file
    screenshot = pyautogui.screenshot()
    screenshot.save(output_file)
    speak(f"Screenshot saved as {output_file}")