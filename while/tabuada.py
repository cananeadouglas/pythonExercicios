while True:
    n = int(input('digite um numero \n'))
    if n < 0:
        break
    else:
        print('tabuada de {}'.format(n))
        for c in range(1, 11):
            print(c, 'x', n, '=', '{}'.format(n*c))