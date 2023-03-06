# pip install SpeechRecognition
# pip install pyaudio
# sudo apt-get install python-pyaudio python3-pyaudio

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo!")
    audio = r.listen(source)

try:
    print("Você disse: " + r.recognize_google(audio, language="pt-BR"))
except sr.UnknownValueError:
    print("Day nao pode entender o audio")
except sr.RequestError as e:
    print("Error ao chamar Google Spreech Recognition service; {0}".format(e))