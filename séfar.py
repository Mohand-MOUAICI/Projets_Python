import speech_recognition   as sr
import pyttsx3 as ttx
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = ttx.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', 'frensh')

def parle(text):
    engine.say(text)
    engine.runAndWait()

def ecoute():
    try:
        with sr.Microphone()  as source:
            print("Parle")
            voix = listener.listen(source)
            command = listener.recognize_google(voix, language='fr-FR')

    except:
        pass
    return command

def assistant():
    command = ecoute()
    print(command)
    if 'bonjour' in command:
        parle('bonjour')

    elif 'bonsoir' in command:
        parle('bonsoir')
    
    elif 'oui ça va et toi?' in command:
        parle('oui ça va bien, merci, comment je peux vous servire?')

    elif 'mets la chonsson de ' in command:
        chanteur = command.replace( 'mettez la chanson de ', '')
        print(chanteur)
        pywhatkit.playonyt(chanteur)

    elif 'heure' in command:
        heure = datetime.datetime.now().strftime("%H:%M")
        parle(f"Il est {heure}")

    elif 'ton nom' in command:
        parle("Je  m'appelle séfar")

    elif 'qui es-tu?' in command:
        parle("Je suis un assistant vocal qui peut te répondre à tes questions ou effectuer certaines tâches.")
    
    elif 'merci' in command:
        parle('De rien, comment peut-je vous aider encore?')
    
    elif 'Je t\'aime' in command:
        parle("Ce n’est pas grave, c’est mon travail! Comment puis-je vous aider aujourd’hui?")

    elif 'joue' in command and 'par' in command:
        song = command.split('par')[1].strip()
        pywhatkit.playonyt(song)

    elif 'au revoir' in command:
        parle("À bientôt")
        return False  # Stop the loop

while True:
    assistant()