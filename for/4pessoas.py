#pessoas
#douglas
maior = 0
soma = 0
frasedomaior = ''
frasemulher = ''
cont = 0
for c in range(0, 4):
    nome = str(input('nome '))
    idade = int(input('idade '))
    sexo = str(input('sexo ')).upper()
    soma += idade

    if maior < idade:
        maior = idade
        frasedomaior = '{} é o homem mais velho ele tem {} de idade'.format(nome, maior)
    if sexo == 'M' and idade < 20:
        cont+=1
        frasemulher = '{} mulheres tem menos de 20 anos'.format(cont)

print('a média de idade é {} anos\n{} \n{}'.format(soma/4, frasedomaior, frasemulher))
