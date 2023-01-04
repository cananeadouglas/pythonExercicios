#1 para tesoura
#2 para pedra
#3 para papel
num = int(input('digite seu numero\n'
                '1 para tesoura\n'
                '2 para pedra\n'
                '3 para papel\n'))
import random
from time import sleep

numcompu = int(random.uniform(1,3))
#print(numcompu)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

if numcompu == num:
    print('empate')
elif numcompu == 1 and num == 2:
    print('você ganhou pedra ganha de tesoura')
elif numcompu == 1 and num == 3:
    print('você perdeu papel ganha de pedra')
elif numcompu == 2 and num == 1:
    print('você perdeu pedra ganha de tesoura')
elif numcompu == 2 and num == 3:
    print('você ganhou papel ganha de pedra')
elif numcompu == 3 and num == 1:
    print('você ganhou tesoura ganha de papel')
elif numcompu == 3 and num == 2:
    print('você perdeu papel ganha de pedra')