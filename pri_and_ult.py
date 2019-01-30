nome = str(input('nome completo')).strip()

separa = nome.split()

print('\n\n'
      'o nome digitado foi {}\n'
      'o primeiro é {}\n'
      'o ultimo é {}'
      ''.format(nome, separa[0], separa[-1]))

print(separa)