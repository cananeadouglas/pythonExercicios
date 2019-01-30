a = int(input('digite o primeiro num'))
b = int(input('digite o segundo num'))
c = int(input('digite o terceiro num'))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('o maior é {} e o menor é {}'.format(maior, menor))

