from datetime import date

atual = date.today().year
nasc = int(input('ano de nascimento'))

idade = atual - nasc

if idade == 18:
    print('vc tem que se alistar imediatamente, vc tem {} anos'.format(idade))
elif idade < 18:
    saldo = 18 - idade
    print('vc ainda não tem idade para se alistar\n'
          'ainda falta {} ano para se alitar\n'
          ''.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('vc já passou da idade de se alistar\n'
          'vc demorou {} anos '.format(saldo))
