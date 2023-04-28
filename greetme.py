import  pyttsx3
import datetime
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id) 
engine.setProperty("rate",170)

def  speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, sir")

    elif hour>12 and hour<=18:
        speak("Good Afternoon,sir")

    else :
        speak("Good Evening , sir")
    
    speak("I am your AI  voice assistant")
    speak("please tell me How can I help you?")