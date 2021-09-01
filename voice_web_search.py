import pyttsx3
import speech_recognition as sr
import webbrowser

en = pyttsx3.init()
en.say("Opa, vai pesquisar o que?")
en.setProperty('voice', b'brazil')
en.setProperty('rate', 150)
en.setProperty('volume', 1)
en.runAndWait()
print("Assistant: Opa, vai pesquisar o que?")

recog = sr.Recognizer()

with sr.Microphone() as source:
    audio = recog.listen(source)
    answer = recog.recognize_google(audio, language='pt')
    command = answer.upper()

print("User: " + answer.lower())

if command == "DESEJO ABRIR O YOUTUBE":
    en.say("Redirecionando")
    en.setProperty('voice', b'brazil')
    en.setProperty('rate', 150)
    en.setProperty('volume', 1)
    en.runAndWait()

    print("Assistant: Redirecionando. . . .")

    webbrowser.open('www.youtube.com')