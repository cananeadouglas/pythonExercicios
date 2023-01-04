valor = float(input('digite valor '))

print('''\nirá pagar a vista com dinheiro?
tem 10% de desconto = {}
no 1 x no cartão terá 5% de desconto = {}
ou 2 vezes no cartão com parcela de {}
ou 3 vezes com 20% de juros = {}
'''.format(valor*0.9, valor*0.95, valor/2, valor*1.20))
