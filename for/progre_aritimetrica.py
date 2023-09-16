come = int(input('digite onde começa '))
seque = int(input('digite a sequencia '))
ate = int(input('digite quantidade de números '))

for c in range(0, ate):
    print(come, end=' ')
    soma = come + seque
    come = soma
