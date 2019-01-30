num = int(input('digite um valor '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        cont+=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n')
if cont == 2:
    print('numero primo ')
else:
    print('não é primo ')