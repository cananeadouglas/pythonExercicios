import PySimpleGUI as sg

#sudo apt-get install python3.8-tk

#Layout
def janela_login():

    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)

def janela_pedido():

    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer pedido')],
        [sg.Checkbox('Pizza Peperone', key='pizza1'),
        sg.Checkbox('Pizza Frango c/ Catupiry', key='pizza2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]

    ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)


#Janela

janela1, janela2 = janela_login(), None

#Ler os eventos

while True:
    window, event, values = sg.read_all_windows()
    #Quando janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    #ir para proxima janela
    if window == janela1 and event == 'Continuar':
        janela2 = janela_pedido()
        janela1.hide()
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == 'Fazer Pedido':
        if values['pizza1'] == True and values ['pizza2'] == True:
            sg.popup('Foram solicitados uma Pizza peperoni e Frango com Catupiry')
        elif values ['pizza1'] == True:
            sg.popup('Foi solicitado Peperoni')
        elif values ['pizza2'] == True:
            sg.popup('Foi solicitado Frango')
        
    #queremos voltar para janela anterior


#Lógica de eventos

            
            

