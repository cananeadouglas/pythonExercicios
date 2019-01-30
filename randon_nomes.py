import random

#from random import choice

nome1 = str(input('nome 1 aqui'))
nome2 = str(input('nome 2 aqui'))
nome3 = str(input('nome 3 aqui'))
nome4 = str(input('nome 4 aqui'))

list = [nome1, nome2, nome3, nome4]

result = random.choice(list)
random.shuffle(list)

print('o nome escolhido foi {}\n'
      'a ordem escolhida foi \n{}'
      ''.format(result, list))

