import random
numcompu = int(random.uniform(0,6))
pessoa = int(input('digite um numero de 0 a 6 '))
print('vc acertou' if numcompu == pessoa else 'vc errou o numero pensado foi {}'.format(numcompu))
