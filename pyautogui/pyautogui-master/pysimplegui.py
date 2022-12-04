from PySimpleGUI import PySimpleGUI as sg

#sudo apt-get install python3.8-tk

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
]

bemvindo = [
    [sg.Text('Seja bem vindo')],
    [sg.Button('click aqui para confirmar')]
]
#Janela

janela = sg.Window('Tela de login', layout)
bem = sg.Window('Ok - vc acessou', bemvindo)

#Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'douglas' and valores['senha'] == '123456':
            print('Seja bem vindo')
            
            

