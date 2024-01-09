dia = int(input('digite o dia '))
mes = int(input('digite o mes '))
ano = int(input('digite o ano '))

import datetime

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

print('###{}###'.format(hoje))

if datapadrao > hoje:
    delta = datapadrao - hoje
    print('a quantidade restante de dias é {} para seu aniversário'.format(delta.days))

elif datapadrao <= hoje:
    delta = hoje - datapadrao
    print('A quantidade de dias passados é {}'.format(delta.days))
