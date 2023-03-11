# pip install SpeechRecognition
import kivy
from kivy.app import App
from kivy.lang import Builder
import speech_recognition as sr
import pyttsx3

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    
    def build(self):
        
        return GUI

    def on_start(self):
        self.root.ids["button"].text = "Fala que eu te escuto"
        maquina = pyttsx3.init()
        maquina.say("olá, como posso ajudar")
        maquina.runAndWait()
    
    def listen_for_speech(self):
        audio = sr.Recognizer()
        
        
        try:
            with sr.Microphone() as source:
                print('ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language="pt-BR")
                comando = comando.lower()
                self.root.ids["messagevoz"].text = comando
                    
        except sr.UnknownValueError:
            self.root.ids["messagevoz"].text = 'não foi possível reconhecer'
    
        
    
MeuAplicativo().run()