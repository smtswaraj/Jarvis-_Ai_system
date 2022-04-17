import random
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis Sir.Please tell me how may I help you ")
def takeCommand():
    '''It take microphone input from user and return string out put'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please....")
        return "None"
    return query
def sendEmail(to, contant):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("swarajnayakdipu777@gmail.com",'swaraj754132')
    server.sendmail('youremail@gmail.com', to, contant)
    server.close()
if __name__ == '__main__':
    speak("swaraj is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for command
        if 'wikipedia' in query:                   #<<<<<<<<<<<---------  this is for wikipedia
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:              #<<<<<<<<<<<---------  this is for webbrowser
            webbrowser.open("https://www.youtube.com/?gl=IN")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music'  in query:
            music_dir = 'D:\\song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,1)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ")
            print(strTime)
        elif 'open code'  in query:
            codePath = "C:\\Users\\Swaraj Nayak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to swaraj' in query:
            try:
                speak("what should I say")
                contant = takeCommand()
                to  = "swarajnayakdipu227@gmail.com"
                sendEmail(to, contant)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend swaraj bhai. I am not able to sent this email ")
        elif "exit" in query:
           print("Exit")
           exit()


