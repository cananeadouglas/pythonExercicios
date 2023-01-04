preço = 0
total = 0
cont1 = 0
cont2 = 0
menor = 0
continuar = ' '
maisbarato = ' '

while True:
    nome = str(input('digite seu nome'))
    preço = float(input('Preço: [9999.99] '))
    total += preço
    cont2 += 1

    if cont2 == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            maisbarato = 'O produto {} é o mais barato custando {} reais'.format(nome, menor)

    if preço > 1000:
        cont1 += 1

    while continuar not in 'SN':
        continuar = str(input('deseja continuar: [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        print('vamos continuar...', end=' ')
    else:
        break
    continuar = ' '
    nome = ' '

print('o total da compra foi {}\n'
      'temos {} produtos custando mais de 1000 reais\n'.format(total, cont1))
print(maisbarato)