frase = str(input('digite seu nome completo')).strip()

print(frase[9::3])
print(len(frase))
print(frase.count(' '))
print(frase.find('android')) #encontrando palavras ou combinações
#print(frase.replace('Python','Android'))
print(frase.upper()) # deixando todas maiusculas
print(frase.lower()) #deixando tudo minusculo
print(frase.title()) #deixando em maiusculas as iniciais
print(frase.strip())
print(frase.find(' '))#verificando quantas letras tem o primeiro nome

separa = frase.split()
print(separa)

print('oljlj {} lkjdflkjf{}'.format(separa[0], len(separa[0])))

