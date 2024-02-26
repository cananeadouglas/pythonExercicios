import datetime

digitado = input("digite entre / a data dia e ano: ")

dia, mes, ano = digitado.strip().split('/')

datapadrao = datetime.date(int(ano), int(mes), int(dia))
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

elif datapadrao <= hoje:
    delta = hoje - datapadrao

print(delta.days)