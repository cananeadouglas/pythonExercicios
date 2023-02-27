num = int(input("Digite um número inteiro: "))
cont = 1

while num != 1:
    cont+=1
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
    print(num, cont)

print("Resultado: ", num)