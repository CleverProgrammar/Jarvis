# KAUN AUR MERA ITNA KAAM KARE YAAR- KAMIKYa
'''
0-> Basic Utilities:
        i) Time related:
            1. Time and Date
            2. Important Dates
            3. Schedule events
            4. Schedule Study
        ii) Browser related:
            1. Open websites
            2. Manipulate youtube
            5. Manage edge account
            6. Manage Google account
            7. Download Images
        iii) Applications:
            1. Open apps
            2. Manage whatsapp
            3. Take a pic
            4. Identify who is in the pic
'''
import datetime
import json
import pyttsx3
import random
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty("voices") # get the voices, currently 2 in my device  


def speak(text: str):
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
    engine.setProperty('voice', voices[1].id)

    # Convert text to speech
    print(f"{text}")
    engine.say(text)
    engine.runAndWait()
    return text

def greet(time: int):
    timeOfDay = ""
    if time<12:
        timeOfDay = "mornings"
    elif time >= 12 and time <= 16:
        timeOfDay ="afternoons"
    else: timeOfDay = "evenings"
    greetings = json.load(open("./data.json"))["greetings"][timeOfDay]
    return random.choice(greetings)

def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            audio = r.listen(source=source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
    except Exception:
        speak("Could you say that again?")
    return query

hour = int(datetime.datetime.now().strftime("%H"))

speak(greet(hour))
cmd = listen()
print(cmd)