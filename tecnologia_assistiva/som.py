import pyttsx3

s = pyttsx3.init()
data = "Eu sou o Douglas e Você não é o Douglas"
s.say(data)
s.runAndWait()