frase = str(input('digite a frase ')).strip().upper()


palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('vc digitou a frase {} - {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um Palídromo')
else:
    print('a frase digitada não é palidromo')


