ano= 2012       #formato AAAA
mes=  9         #usar numeros
dia= 11

import datetime

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

elif datapadrao <= hoje:
    delta = hoje - datapadrao

print delta.days
