sexo = ' '
cont1 = 0
contH = 0
contM = 0
continuar = ' '

while True:
    idade = int(input('digite idade '))

    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        cont1 += 1
    if sexo == 'F' and idade < 20:
        contM += 1
    if sexo == 'M':
        contH += 1
    sexo = ' '

    while continuar not in 'SN':
        continuar = str(input('deseja continuar: [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        print('vamos continuar', end=' ')
    else:
        break
    continuar = ' '

print('{} tem mais de 18 anos, \n'
      '{} homens foram cadastrados\n'
      '{} mulheres tem menos de 20 anos foram cadastrados '
      .format(cont1, contH, contM))