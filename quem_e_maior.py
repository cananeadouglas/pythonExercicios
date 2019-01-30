pri = int(input('primeiro valor '))
seg = int(input('segundo valor '))

if pri > seg:
    print('o primeiro é maior')
elif seg > pri:
    print('o segundo é maior')
elif pri == seg:
    print('os valores são iguais')