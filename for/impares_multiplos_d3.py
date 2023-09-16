count = 0
soma = 0

for c in range(1, 6000, 2):
    if c % 3 == 0:
        count += 1
        soma += c

print('a soma dos {} numeros é {}'.format(count, soma))