import pyttsx3
import speech_recognition as sr
import  datetime
import wikipedia
import webbrowser
import os
import sys

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")

    speak("I am Jarvis  sir. please tell me how may i help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=4000
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query




if __name__ == '__main__':
    wishme()
    while(True):
        query = takeCommand().lower()


        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("Accordin to Wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")


        elif "open google" in query:
            webbrowser.open("google.com")


        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\\photos'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            strtime=datetime.datetime.now().strftime("%H%M%S")
            speak(f"sir the time is {strtime}")

        elif "sublime"  in query:
            path="C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(path)

        elif "pycharm" in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.3\\bin\\pycharm64.exe"
            os.startfile(path)

        elif "exit" in query:
            sys.exit()
