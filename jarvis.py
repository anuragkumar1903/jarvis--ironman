import  pyttsx3
import speech_recognition
import query
import datetime
import pyautogui
from sqlalchemy import true
import requests
import bs4
import speedtest
import os
for i in range(3):
    a=input("Enter password to open assistant\n")
    pw_file=open("password.txt","r")
    pw=pw_file.read()
    pw_file.close()
    if(a==pw):
        print("Anurag Kumar Identity verfied , welcome sir! start me with your initial commands")
        break
    elif (i==2 and a!=pw):
        exit()
    elif (a!=pw):
        print("Try Again")
from intro import play_gif
play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id) 
engine.setProperty("rate",200)

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 3500
        audio = r.listen(source,0,4)
    try:
        print("understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said:{query}\n")
    
    except Exception as e:
        print("I am unable to recognise your voice check your wifi and router and try again or say that again")
        #speak("say that again")
        return"None"
    return query

if __name__== "__main__":
    while True:
        query = takecommand().lower()
        if"wake up" in query:
            from greetme import greetMe
            greetMe()

            while True:
                query = takecommand().lower()
                if"go to sleep" in query:
                    speak("ok Sir,You can call me anytime")
                    break

                elif"who are you" in query:
                    speak ("I am an Ai voice assistant Desinged by Anurag-Kumar stduent of Computer science  at Government Polytechnic purnea")

                elif "hello" in query:
                    speak("Hello sir, how are you?")

                elif "how are you" in query:
                    speak("I'm doing good waiting for your command")

                elif"i am fine" in query:
                    speak("that's great sir")

                elif"i am good" in query:
                    speak("that's amazaing..")
                elif"thank you" in query:
                    speak("you are welcome , sir")
                
                elif"i love you" in query:
                    speak("I love You too Baby")
                
                elif"good night" in query:
                    speak("Good Night sir !")
                    speak("the Ai system is shutting down !")
                    exit()
                
                elif"play" in query:
                    pyautogui.press("k")
                    speak("video played")
                
                elif"pause"  in query:
                    pyautogui.press("k")
                    speak("video paused")
                
                elif"mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                
                elif"full screen" in query:
                    pyautogui.press("f")
                    speak("video is on full screen")
                
                elif"exit" in query:
                    pyautogui.press("ESC")
                    speak("exited fullscreen mode")
                elif "open" in query:
                     from Dictapp import openappweb
                     openappweb(query)
                     
                elif"close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
               
                elif"google" in query:
                    from search import searchGoogle
                    searchGoogle(query)

                elif"youtube "in query:
                    from search import searchYoutube
                    searchYoutube(query)
                    

                elif"wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir, the time is{strTime}")
                
                elif"shutdown" in query:
                    speak("Are you sure want to shutdown system")
                    shutdown= input("(yes/no)")
                    if shutdown=="yes":
                        os.system("shutdown /s /t 1")
                    
                    elif shutdown=="no":
                        break
                
                elif"temperature" in query:
                    query=query.replace("what is the temperature in","")
                    search = "temperature in"+query
                    url =f"https://www.google.com/search?q="+search
                    r= requests.get(url)
                    data = bs4.BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div", class_="BNeawe").text
                    speak(f"current{search} is{temp}")
                    
                elif"internet speed" in query:
                    wifi=speedtest.Speedtest()
                    upload_net= wifi.upload()/1048576
                    download_net=wifi.download()/1048576
                    print("wifi download speed is",download_net)
                    print("wifiupload speed is",upload_net)
                    speak(f"wifi download speed is{download_net}")
                    speak(f"wifiupload speed is{upload_net}")
                
                elif"terminate" in query:
                    speak("Executing assistant Termination File ,sir")
                    exit()