from datetime import date
anoatual = date.today().year
cont1 = 0
cont2 = 0
for c in range(0, 7):
    nascimento = int(input('digite ano de nascimento '))
    aqui = anoatual - nascimento
    if aqui < 18:
        cont1 += 1
    else:
        cont2 += 1

print('menor idade são {}\n'
      'e maior idade são {}'.format(cont1, cont2))