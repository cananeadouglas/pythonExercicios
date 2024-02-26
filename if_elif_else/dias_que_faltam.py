dia = int(input('digite o dia '))
mes = int(input('digite o mes '))
ano = int(input('digite o ano '))

import datetime

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

print('###{}###'.format(hoje))

if datapadrao > hoje:
    delta = datapadrao - hoje
    print(f'a quantidade restante de dias é {delta.days} para seu aniversário')

elif datapadrao <= hoje:
    delta = hoje - datapadrao
    print(f'A quantidade de dias passados é {delta.days}')
