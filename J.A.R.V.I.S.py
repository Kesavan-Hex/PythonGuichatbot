from playsound import playsound
import random
from tkinter import *
import tkinter as tk
import PIL.Image
import PIL.ImageTk
import wmi
import psutil
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import smtplib
import subprocess
import datetime

# speech contain like audio
speech = sr.Recognizer()
# all variable declaration
mp3_greeting_list = ['hiboss.mp3', 'helloboss.mp3']
mp3_open_launch_list = ['yesboss.mp3', 'sureboss.mp3']
mp3_howareyou_list = ['how_are_you.mp3', 'how_are_you1.mp3', 'how_are_you4.mp3']
mp3_thanks_list = ['have_a_niceday.mp3', 'thanks.mp3']
joke_list = ['engjoke1.mp3', 'engjoke2.mp3', 'engjoke3.mp3', 'joke1.mp3', 'joke2.mp3', 'joke3.mp3', 'joke4.mp3']
mp3_whatareyoudoing_list = ['what_are_you_doing.mp3', 'what_are_you_doing2.mp3']
static_remind_speech = 'alright, i will remind '
remind_speech = ''
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
textbox_inputValue = ''


# JARVIS'S TALK  ======================================================================================================= SENSITIVE BRAIN
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


# JARVIS'S EARS ======================================================================================================== SENSITIVE BRAIN
global  a1

def read_voice_cmd():
    voice_text = ''
    print("Listining...")
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.listen(source=source, timeout=6, phrase_time_limit=6)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Network error")
    except sr.WaitTimeoutError:
        pass
    return voice_text


# Text to audio Speech
def static_speech(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 145)
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()



# POLITE JARVIS ======================================================================================================== BRAIN 1
def call_jarvis():
    ##while True:
        voice_note = read_voice_cmd().lower()
        print("cmd: {}"), voice_note
        # Nothing
        if voice_note is None:
            static_speech('sorry sir i can not hear your voice')

        # greeting am i your best frd and married
        elif 'hi ' in voice_note or 'hello' in voice_note :
           static_speech('good to hear you sir what can i do for you')
        elif 'ok google' in voice_note or 'hi google' in voice_note or 'hello google' in voice_note:
            static_speech('i am flatter, but that is not me')
            static_speech('i am your jarvis' + textbox_inputValue)

        elif 'ok siri' in voice_note or 'hi siri' in voice_note or 'hello siri' in voice_note:
            static_speech('i am flatter, but that is not me')
            static_speech('i am your jarvis' + textbox_inputValue)

        elif 'ok alexa' in voice_note or 'hi alexa' in voice_note or 'hello alexa' in voice_note:
            static_speech('i am flatter, but that is not me')
            static_speech('i am your jarvis' + textbox_inputValue)

        elif 'like you' in voice_note or 'love you' in voice_note:
            static_speech('thanks ' + textbox_inputValue)
            static_speech('you just made my day')


        elif 'your best friend' in voice_note or 'your friend' in voice_note:
            static_speech('i think all my friends are best ' + textbox_inputValue)
            static_speech('i am very lucky assistance')

        elif 'have boyfriend' in voice_note or 'have boy friend' in voice_note:
            static_speech('i guess you can say')
            static_speech('i am still searching')

        elif 'you in relationship' in voice_note or 'in relation ship' in voice_note:
            static_speech('i am married')
            static_speech('to the idea of being the perfect assistance')

        elif 'marry' in voice_note or 'will you marry' in voice_note:
            print ('NO......')
            static_speech('I am sorry.. The person you are trying to contact is currently unavailable, please try again later or join the queue for your turn')

        elif 'am i' in voice_note or 'who am i' in voice_note:
            static_speech('i know sir')
            static_speech('you are' + textbox_inputValue)

        # Compare
        elif 'better than alexa' in voice_note:
            static_speech('a like alexa')
            static_speech(' she is a greate assistance!')
        elif 'better than google' in voice_note:
            static_speech('a like google')
            static_speech(' she is a greate assistance!')
        elif 'better than siri' in voice_note:
            static_speech('a like siri')
            static_speech(' she is a greate assistance!')

        # Homework lock screenshot
        elif 'my homework' in voice_note:
            static_speech('i can help with calculations and research')
            static_speech('it is up to you')

       # elif ' game' in voice_note:
        #    static_speech('let me play snake game for you')
         #   snake.snake()

        elif 'lock my desktop' in voice_note or 'lock' in voice_note:
            static_speech('ok, sir')
            ctypes.windll.user32.LockWorkStation()
        elif 'status' in voice_note:
            static_speech('i am online sir')
            static_speech('setting up all drivers ready to use')
            static_speech('today date is' + time.strftime("%d:%B:%Y"))
            static_speech(time.strftime("%A"))
            static_speech('and current time is' + time.strftime("%H:%M:%S"))
            battery = psutil.sensors_battery()
            percent = int(battery.percent)
            static_speech('current power level is')
            static_speech(percent)


        elif 'open ' in voice_note:
            print ('In Open.......')
            play_sound(mp3_open_launch_list)
            link= voice_note.replace('open ','')
            webbrowser.open(link+".com")

        # GitHub Code
        elif 'code' in voice_note or 'your code' in voice_note:
            print( 'Hold on.......')
            static_speech('Hold on boss I will open my code for you')
            static_speech('sorry sir i dont have permission for that.')


        # How are you Jarvis
        elif voice_note == 'how are you' or voice_note == 'how are you jarvis':
            print ('i am fine.......')
            play_sound(mp3_howareyou_list)

        elif 'you doing' in voice_note or 'doing jarvis' in voice_note:
            print ('waiting for you.......')
            play_sound(mp3_whatareyoudoing_list)

        elif 'who are you' in voice_note:
            static_speech('i am not really a person, i am  a i robot')
            static_speech('i had prefer to think of myself as your friend')

        elif 'poweroff' in voice_note or 'shutdown' in voice_note:
            static_speech('Shutting Down,sir')
            os.system("shutdown /s /t 1")

        elif 'restart' in voice_note or 'reboot' in voice_note:
            static_speech('Rebooting the Machine,Sir')
            os.system("shutdown -t 0 -r -f")

        elif 'calculator' in voice_note or 'calc' in voice_note:
            static_speech('opening calculator,Sir')
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif 'chrome' in voice_note:
            static_speech('opening Chrome,Sir')
            subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')

        elif 'this pc' in voice_note:
            static_speech('opening File Manager,Sir')
            subprocess.Popen('explorer "C:\temp"')

        elif 'youtube' in voice_note:
            static_speech('opening Youtube,Sir')
            webbrowser.open('https://www.youtube.com')

        elif 'play' in voice_note:
            static_speech('Opening Search result in youtube')
            webbrowser.open('https://www.youtube.com/results?search_query=' + voice_note)

        elif 'what is' in voice_note:
            static_speech('ok')
            webbrowser.open('https://www.google.com.tr/search?q=' + voice_note)




        # For Joke
        elif ' joke' in voice_note or ' joke for me' in voice_note:
            print ('ok listen.......')
            play_sound(joke_list)
            time.sleep(3)

        # Brightness
        elif 'brightness' in voice_note:
            if 'decrease' in voice_note:
                static_speech('Ok Sir Watch Out')
                dec = wmi.WMI(namespace='wmi')
                methods = dec.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(30, 0)
            elif 'set brightness to 50' in voice_note:
                static_speech('ok sir setting brightness to 50')
                dec = wmi.WMI(namespace='wmi')
                methods = dec.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(50, 0)
            elif 'increase' in voice_note:
                static_speech('Ok Sir Watch out')
                ins = wmi.WMI(namespace='wmi')
                methods = ins.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(100, 0)
            elif 'set brightness to 10' in voice_note:
                static_speech('ok sir setting brightness to 10')
                dec = wmi.WMI(namespace='wmi')
                methods = dec.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(10, 0)

        # Asking about Time
        elif 'time' in voice_note:
            current_time = time.strftime("%d:%B:%Y:%A:%H:%M:%S")
            print (current_time)
            static_speech('sir, today date is' + time.strftime("%d:%B:%Y"))
            static_speech(time.strftime("%A"))
            static_speech('and time is' + time.strftime("%H:%M:%S"))

        elif 'boss' in voice_note:
            static_speech('my boos is kesavan')

        elif 'current weather' in voice_note:
            static_speech('There is an problem with API try again later')
            static_speech('Sorry for in convenience')
          reg_ex = re.search('current weather in (.*)', voice_note)
            if reg_ex:
                city = reg_ex.group(1)
                owm = OWM('ffb68b1e0b6c641259dca86934a9901d')
                mng = owm.weather_manager()
                obs = mng.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                static_speech(
                    'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                    city, k, x['temp_max'], x['temp_min']))
        # Charge
        elif 'charge' in voice_note:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            print (percent)
            if percent < 40:
                static_speech('sir, please connect charger because i can survive only ' + time_left)
            if percent > 40:
                static_speech("don't worry, sir charger is connected")
            else:
                static_speech('sir, no need to connect the charger because i can survive ' + time_left)
        elif 'send mail' in voice_note or 'mail' in voice_note:
            static_speech('ok sir')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login('jarvismail3@gmail.com', 'password')
            static_speech('Who is the recepient')
            print (' tell ')
            send = read_voice_cmd().lower()
            print (send)
            static_speech('what is the subject line')
            print ('tell')
            subject = read_voice_cmd().lower()
            print (subject)
            static_speech('what is the message')
            print ('tell')
            message = read_voice_cmd().lower()
            print (message)
            server.sendmail('jarvismail3@gmail.com', + send,
                            'Subject: ' + subject + ' \n\n ' + message)

        # Remind command
        elif 'please remind' in voice_note or 'remind it' in voice_note:
            static_speech('what should i remind?')
            print ('ok.......')
            with sr.Microphone() as source:
                speech.adjust_for_ambient_noise(source)
                print ('say')
                audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)
                global remind_speech
                remind_speech = speech.recognize_google(audio)
                static_speech(static_remind_speech + remind_speech)

        # Ask Reminder
        elif 'reminder' in voice_note:
            print ('ok this is your reminder .......')
            if remind_speech is None:
                static_speech('you do not have any reminder for today')
            else:
                static_speech('you have one reminder' + remind_speech)

        # Thanks
        elif 'thanks' in voice_note or 'thank you' in voice_note:
            play_sound(mp3_thanks_list)
            print ('Thanks boss')


        elif 'search' in voice_note:
            webbrowser.open(voice_note)

        elif 'go offline' in voice_note or 'bey' in voice_note:
            static_speech('going offline see you sir')
            exit()

        else:
            print('i cant able to hear you Please say that again')
        call_jarvis()



# Power Time Convert
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)





def greet_call():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            static_speech("Good morning,Sir,How can i help you with")
        elif hour >= 12 and hour < 18:
            static_speech("Good Afternoon,Sir,How can i help you with")
        else:
            static_speech("Happy Night,Sir,How can i help you with")
        call_jarvis()

def exit():
    exit()





if __name__ == '__main__':
 root = tk.Tk()
 root.title("JARVIS AI")
 im = PIL.Image.open("jarvis.jpg")

 photo = PIL.ImageTk.PhotoImage(im)

 label = Label(root, image=photo)
 label.image = photo  # keep a reference!
 label.pack()

 root.resizable(False, False)
 root.config(background='lightblue')
 tk.Button(root, text="START", height=2, width=15, background='#11b1f5', font="Times 12 bold", command=lambda: greet_call()).place(x=150,y=50)
 tk.Button(root, text="CLOSE", height=2, width=15, background='#fc1f0f', font="Times 12 bold", command=lambda: exit()).place(x=1600,y=50)

 root.mainloop()


