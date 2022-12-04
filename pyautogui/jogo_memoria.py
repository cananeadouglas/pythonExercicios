import random
from time import sleep
import string
import time

nome_do_jogador = " "
pontuacao_jogador = 0
number = 0
print ('Bem vindo ao Jogo de Memória com letras e números: ')

num = int(input('digite sua opção de jogo\n'
                '1 para números\n'
                '2 para letras\n'
                '3 para  placa de carros \n'))

def criacao():

    num1 = int(random.uniform(0,9999))
    return num1

if num == 1:

    digitado = 0
    acertos = 0

    while digitado != 88: 
        #for c in range (0, passo):
        salvo = criacao()
        print(salvo)
        time.sleep(5.4)
        print("\x1b[2J")
        oi = int(input('digite o que viu: '))
        print('vc acertou' if salvo == oi else 'vc errou')
        if salvo == oi:
            acertos+=1
        else:
            print('quantidade de acertos:',acertos)
            print('programa finalizado')
            break


# mostrar o passo anterior junto com o atual
#print('vc acertou' if numcompu == pessoa else 'vc errou o numero pensado foi {}'.format(numcompu))


elif num == 2:
    letras = string.ascii_uppercase
    let1 = ''.join(random.choice(letras) for _ in range(3))
    print (let1)
elif num == 3: 

    while number < 501 :
        number +=1;
        num1 = int(random.uniform(0000,9999))
        letras = string.ascii_uppercase
        let1 = ''.join(random.choice(letras) for _ in range(4))
        let_and_num1 = ('{}-{}'.format(let1, num1))
        print (let_and_num1)

else:
    print('nada fazer')

