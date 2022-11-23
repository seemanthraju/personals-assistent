import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

greetings = ['hey there jarvis', 'hello jarvis', 'hi jarvis', 'Hai jarvis', 'hey! jarvis', 'hey jarvis',]

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at "+usage)
    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def sq(query): 
    if query == 'start':
        wishMe()
        while True:
    # if 1:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")


            elif 'play music' in query:
                try:
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)
                    os.startfile(os.path.join(music_dir, songs[0]))
                except Exception as e:
                    print(e)
                    speak("no audio files found Sir")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in query:
                codePath = "C:\\Users\\seemanth\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'email to harry' in query:
                try:
                    speak("What should I say Sir?")
                    content = takeCommand()
                    to = "harryyourEmail@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent sir!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")
            
            elif query in greetings:
                speak(query+"sir")
            
            elif 'shutdown' in query:
                speak("as you say sir!!")
                break
            elif 'cpu' or 'battery' in query:
                cpu()

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if query=="start":
            sq(query)
            break
    
    