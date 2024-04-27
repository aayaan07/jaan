import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
import keyboard
import pyaudio
import google.generativeai as genai
import time
from colorama import Fore
import json
import pyautogui

config_file = open("./data.json")
config_data = json.load(config_file)



print(Fore.LIGHTMAGENTA_EX + "              **    ***       ***    **     **              ")
print("              **   ** **     ** **   ***    **              ")
print("              **  **   **   **   **  ** *   **              ")
print("              **  *******   *******  **  *  **              ")
print("              ** **     ** **     ** **   * **              ")
print("         **   ** **     ** **     ** **    ***              ")
print("          *****  **     ** **     ** **     **              ")

PALM_KEY = config_data["API_KEY"]
genai.configure(api_key=PALM_KEY)

bard = genai.GenerativeModel('gemini-pro')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[-1].id)
engine.setProperty('rate' , 190)

user_name = config_data["username"]
nick = config_data["nick"]
config_file.close()


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    print(Fore.RED)
    speak("Activating Jaan")
    time.sleep(1)
    print(Fore.GREEN)
    speak("Jaan Activated")
    print("")
    print("")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    print("")
    speak("I am Jaan, How can i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.WHITE + "Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
        r.phrase_threshold = 1
        audio = r.listen(source)

 

    try:
        print(Fore.LIGHTCYAN_EX + "Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(Fore.YELLOW + f"User said: {query}\n")
        print(Fore.MAGENTA) 

    except Exception as e:  
        print("Say that again please...")   
        return "None" 
    return query




if __name__ == "__main__":
    
    chat = bard.start_chat(history=[])
    chat.send_message(f"You are Jaan, a girl AI Assistant. Act like you are user\'s close friend. You are here to help users and answer their queries. Make sure that your answer is simple, short and to the point. Don\'t include extra text and emojies. The user\'s name is {user_name}, btw don\'t include it everytime in the reply, do it when needed.")

    wishMe()
    while True:
        query = takeCommand().lower().replace("john", "jaan").replace("sev", "save").replace("seb", "save")
        if "jaan" in query:
            query = query.replace("jaan", "").strip()

            if query != "":

                if 'wikipedia' in query: 
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "").replace("search", "").strip()
                    results = wikipedia.summary(query, sentences=2) 
                    speak("According to Wikipedia")
                    speak(results)

                elif "close this" in query:
                    speak("Closing")
                    pyautogui.hotkey("ctrl","w")

                elif 'google search' in query:
                    speak(f"Ok {nick} , this is what I found")
                    query = query.replace("google search" , "")
                    pywhatkit.search(query)

                elif 'youtube search' in query:
                    speak(f"Ok {nick}, this is what i found")
                    query = query.replace("youtube search","")
                    web = 'https://www.youtube.com/results?search_query=' + query
                    webbrowser.open(web)

                elif 'play' and 'on youtube' in query:
                    query.replace('play', "").replace('on youtube', "").strip()
                    speak("Starting youtube")
                    pywhatkit.playonyt(query)

                elif 'today\'s date' in query:
                    date = datetime.datetime.now()
                    speak(f"Today\'s date is {date.day} - {date.month} - {date.year}")

                elif 'music' in query or "song" in query:
                    speak(f"Which song do you want to listen {nick}")
                    songs = takeCommand().lower()
                    pywhatkit.playonyt(songs)
                    speak(f"Your song has been started {nick}, Enjoy!")

                elif query == "press enter":
                    keyboard.press('enter')

                elif 'new window' in query:
                    keyboard.press_and_release('ctrl + n')

                elif 'new tab' in query:
                    keyboard.press_and_release('ctrl + t')

                elif 'speak' in query:
                    speak("Listening...")
                    sent = takeCommand().lower()
                    speak(sent)

                elif "send mail" in query:
                    webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")
                    time.sleep(2)
                    speak("To whom do you want to send the mail")
                    email = takeCommand().lower().replace(" ","").replace("attherate", "@").replace("dot",".")
                    keyboard.press_and_release(list(email))
                    keyboard.press_and_release("tab")
                    speak("What\'s the subject")
                    subject = takeCommand().lower()
                    keyboard.press_and_release(list(subject))
                    keyboard.press_and_release("tab")
                    speak(f"{nick} do you want me to write the mail or you will write it itself.")
                    who = takeCommand().lower()
                    if "you" in who or "yes" in who:
                        speak(f"Ok {nick}, let me write the mail according to the subject for you")
                        res = bard.generate_content(f"Write a mail for the subject: {subject}")
                        keyboard.press_and_release(list(res.text.replace("*", "")))
                        speak(f"Done {nick}, If you want to make some changes you can.")
                    else:
                        speak(f"Ok {nick}")
                    



                elif 'keyboard' in query:
                    speak("Keyboard activated, Listening")
                    words = takeCommand().lower()
                    a = list(words)
                    keyboard.press_and_release(a)

                elif query == "hacking theme":
                    speak("Starting")
                    time.sleep(1)
                    speak("Hacking the system")
                    print('')
                    print('')
                    for a in range(1000000,1005665,19):
                        print(a,a*2,a*3,a*5,a*7,a*9)
                    print('')
                    speak("System hacked")

                elif 'bye' in query:
                    speak(f"Ok {nick}, see you soon")
                    break

                elif query == "save file":
                    keyboard.press_and_release("ctrl + s")
                    speak(f"With what name would you like to save it {nick}")
                    nameOfFile = takeCommand().strip()
                    if nameOfFile == "break":
                        break
                    else:
                        finalName = list(nameOfFile)
                        keyboard.press_and_release(finalName)
                        keyboard.press_and_release("enter")
                        speak(f"Done {nick}")

                elif "open" in query:                 
                    app_name = query.replace("open", "").strip()
                    speak(f"Opening {app_name}")
                    pyautogui.press("super")
                    time.sleep(0.1)
                    pyautogui.write(app_name)
                    time.sleep(0.1)
                    pyautogui.press("enter")

                else:
                    try:
                        res = chat.send_message(query)
                        reply = res.text.replace("*","")
                        
                        if "read that" in query:
                            speak(reply)
                        else:
                            if len(reply) < 300:
                                speak(reply)
                            else:
                                speak(f"Here you go {nick}")
                                print(reply)
                    
                    except:
                        speak(f"Sorry {nick}, an error occurred")
     
