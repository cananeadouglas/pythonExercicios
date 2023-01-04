din = int(input('quanto quer sacar? '))

total = din
cont100 = cont50 = cont20 = cont10 = cont5 = cont2 = 0

while total >= 100:
    total -= 100
    cont100 += 1
if cont100 >= 1:
    print('{} notas de 100'.format(cont100))
while total >= 50:
    total -= 50
    cont50 += 1
if cont50 >= 1:
    print('{} notas de 50'.format(cont50))
while total >= 20:
    total -= 20
    cont20 += 1
if cont20 >= 1:
    print('{} notas de 20'.format(cont20))
while total >= 10:
    total -= 10
    cont10 += 1
if cont10 >= 1:
    print('{} notas de 10'.format(cont10))
if total % 6 == 0:
    while total >= 2:
        total -= 2
        cont2 += 1
    if cont2 >= 1:
        print('{} notas de 2'.format(cont2))
elif total % 5 == 0:
    while total >= 5:
        total -= 5
        cont5 += 1
    if cont5 >= 1:
        print('{} notas de 5'.format(cont5))
elif total % 7 == 0 or total % 9 == 0:
    while total >= 5:
        total -= 5
        cont5 += 1
    if cont5 >= 1:
        print('{} notas de 5'.format(cont5))
    while total >= 2:
        total -= 2
        cont2 += 1
    if cont2 >= 1:
        print('{} notas de 2'.format(cont2))
else:
    while total >= 2:
        total -= 2
        cont2 += 1
    if cont2 >= 1:
        print('{} notas de 2'.format(cont2))