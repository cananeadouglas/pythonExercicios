import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
import speech_recognition as sr

kivy.require('1.11.1')

Builder.load_string('''
<MainWindow>:
    orientation: 'vertical'

    TextInput:
        id: text_input
        text: 'Pressione o botão e fale'
        font_size: 24
        size_hint_y: 0.8

    Button:
        id: button
        text: 'Pressione para falar'
        font_size: 24
        size_hint_y: 0.2
        on_press: root.listen_for_speech()

''')

class MainWindow(BoxLayout):
    def listen_for_speech(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

        try:
            recognized_speech = recognizer.recognize_google(audio, language="pt-BR")
            self.ids.text_input.text = recognized_speech
        except sr.UnknownValueError:
            self.ids.text_input.text = 'Não foi possível reconhecer o que foi dito'

class MainApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return MainWindow()

if __name__ == '__main__':
    MainApp().run()
