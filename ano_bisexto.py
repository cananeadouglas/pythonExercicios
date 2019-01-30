#from datetime import date
#ano = int(input('qual o ano que vc quer analisar'
#  '\nou digite 0 para analisar o ano atual?'))
#if ano == 0:

#    ano = date.today().year
ano = int(input("digite o ano que deseja saber: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('BISSEXTO')
else:
    print('NAOBISSEXTO')
