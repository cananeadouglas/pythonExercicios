km = float(input('digite a distancia '))

if km <= 200:
    km = km * 0.50
    print('vc irá pagar o valor de {}'
          ''.format(km))
else:
    km = km * 0.45
    print('vc ira pagar o valor de {}'
          ''.format(km))
