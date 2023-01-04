num = int(input('digite um numero até 4 digitos'))

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print('unidade é {}\n'
      'dezena é {}\n'
      'centena é {}\n'
      'milhar é {}\n'
      ''.format(uni, dez, cen, mil))