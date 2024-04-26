import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener=sr.Recognizer()
engine = ttx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'french')

def parler(text):
        engine.say(text)
        engine.runAndWait()

def ecouter():
    try:
        with sr.Microphone() as source:
            print("Vous pouvez parler!")
            voix=listener.listen(source)
            command=listener.recognize_google(voix,language="fr-FR")
            command.lower()
            
    except:
        pass
    return command

def lacer_assistant():
    command = ecouter()
    print(command)
    if "bonjour" in command or "salut" in command:
       text = 'bonjour. comment ça va?'
       parler(text)
    
    elif "chanson" or "musique" in command:
        chanteur = command.replace("mets la chanson de",'')
        print(chanteur)
        pywhatkit.playonyt(chanteur)
        parler(chanteur)

    elif "heure" in command:
        heure = datetime.datetime.now().strftime("%H:%M")
        parler("il est" + heure)

    elif "date" in command:
        date = datetime.datetime.today().strftime("%d/%%Y")
        parler("aujourd'hui c'est le %s."%date)
    
    elif 'au revoir' in command:
        parler("À bientôt")
        return False
    
    else:
        parler("Je n'ai pas compris.")

while True:
    lacer_assistant()