import random
compu = random.randint(1,9)
contEu = 0
contComp = 0
while True:
    pi = str(input('Par ou Impar [ P / I ] \n')).upper()
    num = int(input('diga um valor de 1 a 5 \n'))
    soma = num + compu
    print('voce escolheu {} e o computador escolheu {} a soma é {} '.format(num, compu, soma))
    if soma % 2 == 0:
        if pi == 'P':
            print('vc ganhou ')
            contEu += 1
        else:
            print('vc perdeu e o COMPUTADOR GANHOU')
            break
    else:
        if pi == 'I':
            print('vc ganhou')
            contComp += 1
        else:
            print('vc perdeu e o COMPUTADOR GANHOU')
            break

print('GAME OVER, vc ganhou {} vezes'.format(contEu))