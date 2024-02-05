####### MODULE #######
import os
import subprocess
import webbrowser
import random
import datetime
######################
#Greeting
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        os.system("termux-tts-speak Good Afternoon sir")
    elif hour >= 12 and hour < 18 :
        os.system("termux-tts-speak Good Evening sir")
    else :
        os.system("termux-tts-speak I am Jarvis sir please Tell me How may I help you")

wishMe()
os.system ("clear")


while True :
    colour=["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m"]
    colour = random.choice(colour)
    print()

    
    print(colour,">>>>>[say somthing...!]<<<<")


    print ()
    query = subprocess.getoutput(" termux-speech-to-text")
    print()

    print("\033[41m""\033[32m[>",query,"<]\033[om")


###start
    if "hello" in query or "Hi" in query :
        os.system("termux-tts-speak Hello sir I am Jarvis")
        print("\033[34m""Hello sir I am Jarvis!\033[om")


    elif"who are you " in query or "what is your name " in query :
        os.system("termux-tts-speak I am Jarvis sir")
        print ("\033[38;5;209m""I am Jarvis sir")


#caller
    elif"call to mother" in query or "call to my mom" in query:
        os.system ("termux-tts-speak I am calling sir  ")
        os.system("termux-telephony-call 7754850429")
    elif"call to mama ji" in query or "call to my mama" in query: 
        os.system ("termux-tts-speak I am calling sir ")
        os.system("termux-telephony-call 9621770203")

    elif"battery" in query or "status" in query :
        os.system ("termux-tts-speak Here the Current information of your battery")
        os.system("termux-battery-status")
    elif"open google" in query or "google" in query:
        os.system("termux-tts-speak Opening Sir")
        os.system("termux-open-url https:// google.com")
    elif "open YouTube" in query or "YouTube" in query :
        os.system("termux-tts-speak Opening Sir")
        os.system("termux-open-url https://YouTube.cam")
    elif"what\'s up" in query or "how are you" in query:
        Ms = ['Just doing my thing !','I am Fine','Nice','I am Nice and Full of energy']
        os.system ("termux-tts-speak" + rendom.choice(Ms))


    elif"play music" in query or "start music" in query or "music" in query :
        os.system("bash music.sh")

#Termux-api command
    elif "touch" in query or "light" in query :
        os.system ("termux-touch on")

    elif "vibrate" in query or "vibrate in device" in query :
        os.system("termux-tts-speak I am Vibrating Your device Sir")
        os.system("termux-vibrate")

    elif"contact list" in query :
        os.system("I am Listing Your contact List")
        os.system("termux-contact-list")

    elif"brightness" in query:
        os.system("termux-tts-speak What should be the Ratio of brightness ")
        bright = subprocess.getoutput("termux-speech-to-text")
        print(str(bright))
        os.system("termux-brightness" + str(bright))
    elif"exit" in query or "stop" in query or "quit" in query :
        os.system("termux-tts-speak Okey Sir")
        exit()
    elif"Wi-Fi" in query:
        os.systen ("termux-tts-speak I am activating Your WiFi")
        os.system("termux-wifi-enable true")
    elif"disable Wi-Fi" in query:
        os.system("termux-tts-speak I am disactivated Your WiFi signal")
        os.system("termux-wifi-enable true")
    elif"I love you" in query or "Love" in query:
        os.system("termux-tts-speak I love you too Sir")
    elif"search" in query or "find" in query :
        os.system("termux-tts-speak What do you wanna search far")
        print("\033[32m<<[ \033[32m""What do You Wanna\033[31m\033[4mSEARCH \033[33mFor ? \033[32m]>>")
        print()
        command = subprocess.getoutput("termux-speech-to-text")
        print("\033[42m""\033[38;5;209m[>",command, "<]\033[0m")
        os.system("termux-open-url https://www.youtube.com/results?search_query=" + command)
        os.system("termux-tts-speak Here the Search Results About " + command + "From YouTube")
    elif "thanks" in query or "well done" in query:
        os.system("termux-tts-speak No problem Sir Its my pleasure ")

    elif "application" in query or "letter" in query :
        os.system("clear")
        os.system("\033[34m")
        os.system("cat notes_20371010210856.txt")





    else :
        os.system("termux-tts-speak Sorry sir ! i did not get that please Speak Again")
        print()
        print("\033[38;5;209m""Sorry sir ! i did not that please Speak Again !\033[0m ")

        
