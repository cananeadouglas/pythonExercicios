# várias formas de importar um arquivo
# usando módulos no python
# 1- import calcule_preco (se o arquivo estiver na raiz)
# 2- import nome_da_pasta.calcule_preco (se o arquivo estiver dentro de uma pasta específica)
# 3- from vendas.calcule_preco import aumento, desconto 
# dessa forma vc chama os atributos no final



import formato_preco
import calcule_preco

preco = 50

preco_com_aumento = calcule_preco.aumento(preco, 15, formato=True)
print(preco_com_aumento)

print("-----------------")
preco_com_desconto = calcule_preco.desconto(preco, 15, formato=True)
print(preco_com_desconto)

print(formato_preco.real(500))

