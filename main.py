import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener=sr.Recognizer()
engine=pyttsx3.init()
print("OK")
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            talk("Hi my dear boss chanakya i am chandragupta i am hapy to meet you once again in 2022")
            print('listening')
            audio=listener.listen(source)
            query=listener.recognize_google(audio)
    except:
        print('sorry')
    return query


def run_chandragupta():
    print('give me command')
    command=take_command()
    print("THIS IS WORKING NICE")
    if "play" in command:
        song = command.replace('play', "")
        talk('playing' + song)
        pywhatkit.playonyt(song)
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%H %p")
        talk("Current time is" + time)
    if "who is " in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
run_chandragupta()













