velox = int(input('diga sua velocidade\n'))

multa = 50
multaacima = 7

if velox <= 80:
    print('vc não foi multado')
else:
    b = velox - 80
    multaacima = multaacima * b + multa
    print('vc foi multado em R$ {} reais'.format(multaacima))
