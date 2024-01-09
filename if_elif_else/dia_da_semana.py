dia = int(input('digite o dia ex: 00 '))
mes = int(input('digite o mes ex: 00 '))
ano = int(input('digite o ano ex: 0000 '))

a = (14 - mes) // 12
b = ano - a
c = mes + 12 * a - 2
d = dia + (31 * c//12) + b + (b // 4) - (b // 100) + (b // 400)
r = d % 7 + 1

if r == 1:
    print('Domingo - {}.{}.{}'.format(dia, mes, ano))
elif r == 2:
    print('Segunda - {}.{}.{}'.format(dia, mes, ano))
elif r == 3:
    print('Terça - {}.{}.{}'.format(dia, mes, ano))
elif r == 4:
    print('Quarta - {}.{}.{}'.format(dia, mes, ano))
elif r == 5:
    print('Quinta - {}.{}.{}'.format(dia, mes, ano))
elif r == 6:
    print('Sexta - {}.{}.{}'.format(dia, mes, ano))
elif r == 7:
    print('Sábado - {}.{}.{}'.format(dia, mes, ano))
else:
    print('aconteceu algun erro, tente novamente')