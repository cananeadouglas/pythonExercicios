a = int(input('valor a: '))
b = int(input('valor b: '))
c = int(input('valor c: '))

if a == b == c:
    print('todos os lados são igual é escaleno\ne')
elif a == b or b == c or c == a:
    print('dois lados são iguais é Isósceles\ne')
elif a != b != c:
    print('todos os lados são direfentes é Escaleno\ne')


if a < b + c and b < a + c and c < b + a:
    print('podem formar um triangulo')
else:
    print('não forma triangulo')
