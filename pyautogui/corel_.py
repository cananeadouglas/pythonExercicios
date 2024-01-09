import pyautogui
from time import sleep

sleep(3)
print('Copiar o S ENTER iniciando em 3 segundos')

# vem = pyautogui.locateOnScreen(r'passa.png')
# pyautogui.click('./passa.png')
# print(vem)

# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)
# pyautogui.click(100, 200)
# seta -1255 602
# exportar -997 64
# digitar pyautogui.write('Hello world!', interval=0.25)
# exportar janela -489 624
# ok -489 624

i = 2
j = 51

for c in range(i, j, 1):
    # clicando na seta ao lado
    pyautogui.click(-1255, 602)
    sleep(1)

    # exportar
    pyautogui.click(-997, 64)
    sleep(2)

    # escrever
    pyautogui.write(f'{c}', interval=0.25)
    sleep(2)

    # exportar janela
    pyautogui.click(-485, 619)
    sleep(2)

    # OK janela
    pyautogui.click(-594, 567)
    sleep(2)

print('\033[0;36;40m Trabalho Concluido com sucesso \033[m')