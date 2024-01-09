
cpf = input('digite seu cpf sem pontos')

a0 = int(cpf[0])
a1 = int(cpf[1])
a2 = int(cpf[2])
a3 = int(cpf[3])
a4 = int(cpf[4])
a5 = int(cpf[5])
a6 = int(cpf[6])
a7 = int(cpf[7])
a8 = int(cpf[8])
a9 = int(cpf[9])
a10 = int(cpf[10])

valorZero = 0

# print('verificando o seu cpf  \n' '{}{}{}.{}{}{}.{}{}{}-{}{}'''.format(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10))

d01 = ( a0*10 + a1*9 + a2*8 + a3*7 + a4*6 + a5*5 + a6*4 + a7*3 + a8*2 ) % 11
valor1 = 11 - d01 #
print(valor1, "d1")
if valor1 >= 10:
    print (valorZero)
else:
    print(valor1)

d02 = ( a0*11 + a1*10 + a2*9 + a3*8 + a4*7 + a5*6 + a6*5 + a7*4 + a8*3 + a9*2 ) % 11
valor2 = 11 - d02 #
print(valor2, "d2")
if valor2 >= 10:
    print (valorZero)
else:
    print(valor2)

if valor1 == a9 and valor2 == a10:
    print("É Verdadeiro")
else:
    print("É Falso")


""" 
1 – DF, GO, MS, MT e TO
2 – AC, AM, AP, PA, RO e RR
3 – CE, MA e PI
4 – AL, PB, PE, RN
5 – BA e SE
6 – MG
7 – ES e RJ
8 – SP
9 – PR e SC
0 – RS 
"""