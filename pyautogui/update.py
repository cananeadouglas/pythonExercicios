import pyautogui
from time import sleep

# pyautogui.size()
pyautogui.hotkey('ctrl', 'alt', 't')
# pyautogui.press('esc')

print('espere 3 segundos')
sleep(3)


# pyautogui.click(x=2122, y=740)
sleep(4)

pyautogui.write(f'sudo apt update', interval=0.5)
#sleep(2)

pyautogui.press('enter')
