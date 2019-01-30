num = int(input('digite um numero'))

num2 = int(input('digite uma forma de conversão'
                 '\n1 para binário\n'
                 '2 para octal\n'
                 '3 para hexadecimal'
                 ''))

if num2 == 1:
    print('{} convertido em BINARIO é {}'.format(num, bin(num)[2:]))
elif num2 == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif num2 == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('vc digitou a opção que não tem')
