valorcasa = float(input('valor da casa?'))

salario = float(input('seu salario?'))
print('mensalidade poderá ser até R$ {}'.format(salario*0.7))

quantidadeanos = int(input('quantidade de anos'))
print('a quant de meses é {}'.format(quantidadeanos*12))

print('parabéns vc poderar comparar a casa'
      if (valorcasa/(quantidadeanos*12)) < (salario*0.7)
      else 'vc não poderar comprar a casa')