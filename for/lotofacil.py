comeca = int(input('digite o concurso inicial '))
seque = int(input('digite a sequencia, 1 -> normal '))
final = int(input('digite o qtd de nº exibidos '))

for c in range(0, final):
    print(comeca, end=' ')
    soma = comeca + seque
    comeca = soma