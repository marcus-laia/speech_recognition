import pyttsx3
from datetime import datetime

now = datetime.now()

name = "amigo"
hour = now.hour
minute = now.minute

text = f"Olá {str(name)} seja bem-vinda. Agora são {str(hour)} horas e {str(minute)} minutos"

en = pyttsx3.init()

en.setProperty('voice', b'Brazil')
en.setProperty('rate', 180)
en.setProperty('volume', 1)

en.say(text)
en.runAndWait()