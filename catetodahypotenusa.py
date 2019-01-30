from math import hypot

oposto = float(input('digite cateto oposto'))
adjacente = float(input('digite cateto adjacente'))

#hi = ( oposto**2 + adjacente**2 ) ** (1/2)
#print('a hipotenusa vai medir {:.2f}'.format(hi))

hi = hypot(oposto, adjacente)

print('o valor da hipotenusa é {:.2f}'.format(hi))