palavras = []
while True:
    
    palavra = input("Digite uma palavra ou digite END para finalizar: ")
    palavras.append("(")
    cont = int(input("quantas vezes "))
    for c in range(cont):
        c+=1
        if palavra == "END":
            break
        elif palavra != "END":
            palavras.append("AND")
        
        palavras.append("'"+palavra+"'")
    
    palavras.append(")")
    
    palavras.append("OR")
    
print("Palavras digitadas em sequência:")
for palavra in palavras:
    print(palavra, end=" ")