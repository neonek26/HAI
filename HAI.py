import speech_recognition as spre
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import numpy
import pandas

listener = spre.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with spre.Microphone() as source:
            print('LISTENING')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hai' in command:
                command = command.replace('hai', '')
                print(command)
    except:
        pass
    return command

// PŘÍKAZY

def run_hai():
    command = take_command()
    print(command)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

// NEFUNGUJÍCÍ   ⇊ ⇊ ⇊ ⇊

    elif 'date' in command:
        time = datetime.date.today().strftime()
        talk('Current date is ' + datetime.date.today) 

// NEFUNGUJÍCÍ   ⇈ ⇈ ⇈ ⇈

    elif 'creator' in command:
        talk('HAI was created by Stepan Hofmann in 2022.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Say the command again.')


while True:
    run_hai()