import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib
from gtts import gTTS
from tkinter import *
from PIL import Image
import subprocess
import os
import sys
from PIL import Image, ImageTk


print("enter your name")

#root = tkinter.Tk()
#inname ="tenor.gif"
#root.mainloop()
 
engine=pyttsx3.init()
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def userstart():
    print("Please enter your name")
    speak("please enter your name")
          



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
user = input()
def wishMe():
    speak("Welcome back sir")
    hour = int(datetime.datetime.now().hour)
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak("the current Time is")
    speak(Time)
    if hour>=6 and hour<12:
        speak("Good Morning!" + user)
        speak ("iam your assistant Soul bot")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!" + user)
        speak ("iam your assistant Soul bot")

    elif hour>=18 and hour<24:
        speak("Good Evening !" + user)
        speak ("iam your assistant Soul bot")

    else:
        speak("Good Night!" + user)
        speak ("iam your assistant Soul bot")
        
def assistant_speaks(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("PerSon : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
   
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
    
        
    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry," + user)
        speak("can you repeat that again?")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")
        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is opened")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("music is being played")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:/Users/User/AppData/Local/Programs/Python/Python310/Hackathon2022.py"
            os.startfile(codepath)
        
       
        elif 'open notepad' in query:
            notepadpath = "%windir%\system32\notepad.exe"
            os.startfile(notepad)
            engine = pyttsx3.init() 
            engine.say(command)  
            engine.runAndWait() 
      
        elif "hello" in query:
            print("hello my dear how are you")
            speak("hello my dear how are you")
            
            

        elif "do you love me" in query:
            print("of course i love you are so special for me")
            speak("of course i love you are so special for me")
            


        elif "I am good" in query:
            print("i am very glad to hear that.")
            speak("i am very glad to hear that.")
            

        elif "who are you" in query:
            print("i am Soul bot I am here to help you")
            speak("i am Soul bot I am here to help you")
            


        elif "how are you" in query:
            print("i am fine thanks for asking, how about you")
            speak("i am fine thanks for asking, how about you")
            


        elif  "why have you been created" in query:
            print("i have been created for helping you ask me anything")
            speak("i have been created for helping you ask me anything")
            
      
                   
            
        elif "made you"  in query:
            print("I have been created by 2 programmers. Programmers team from Azerbaijan")
            speak("I have been created by 2 programmers. Programmers team from Azerbaijan")
            
           
            
            
        elif "how to use" in query: 
            print("just sign up and go to main page. Later choose get started and continue")
            speak("just sign up and go to main page. Later choose get started and continue")

            
        elif  "what is your name" in query:
            print("my name is Soul bot. i am your assistant")
            speak("my name is Soul bot. i am your assistant")
            
            
            
        elif  "fact " in query:
            print("Our website have been created by 4 high school students, it's great right? ")
            speak("Our website have been created by 4 high school students, it's great right? ")
            
            
        elif "shut up" in query:
            print("Okay it is a pleasure to shut up for me")
            speak("Okay it is a pleasure to shut up for me")
            


        elif "sorry" in query:
            print ("no problem i love you my dear.Don't be sorry for me")
            speak ("no problem i love you my dear.Don't be sorry for me")
            


        elif "something" in query:
            print("YOU ARE THE BEST PERSON I HAVE EVER MET, I LOVE YOU.")
            speak("YOU ARE THE BEST PERSON I HAVE EVER MET, I LOVE YOU.")
            
            

        elif "gender" in query:
            print("no, I don't have a gender. Love is love, what is the difference?")
            speak("no, I don't have a gender. Love is love, what is the difference?")


 
        elif "go away" in query:
            print("NO PLEASE MY DEAR, I CAN'T LIVE WITHOUT YOU")
            speak("NO PLEASE MY DEAR, I CAN'T LIVE WITHOUT YOU")



        elif "register" in query:
            print("Go to the main menu page, and click on login/register button. Let me know if you need help again")
            speak("Go to the main menu page, and click on login/register button. Let me know if you need help again")
            

        elif "Who am" in query:
            speak("Because of your personality, one of the best shoes for you can be this: site.com/shoe/no1")
            print("Because of your personality, one of the best shoes for you can be this: site.com/shoe/no1")

                  
        
        elif 'bye' in query:
            print("see you soon my love")
            exit()

        
            
                
        else :
            webbrowser.open(query)
