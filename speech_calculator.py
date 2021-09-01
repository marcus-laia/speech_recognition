import speech_recognition as sr

recog = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        print('Descreva sua multiplicação: ')
        #esperado formato "x vezes y" ou "x multiplica y"
        audio = recog.listen(source)

        speech = recog.recognize_google(audio, language='pt')
        if speech == "fechar": break

        print('Sua multiplicação é: ' + speech)
        print('O resultado é: ' + str(int(speech[0])*int(speech[-1])))