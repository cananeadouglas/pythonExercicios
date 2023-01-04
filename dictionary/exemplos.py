diciona = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# mostrando o valores
print(diciona.values())
print ("---")

# mostrando os itens
print(diciona.items())
print ("---")

# mostrando o valores / chaves
print(diciona.keys())
print ("---")
print(len(diciona))

for k, v in diciona.items():
    print(f' {k} é {v} ')

# Adicionando mais uma chave com valor
diciona['chave'] = "valor"

for k, v in diciona.items():
    print(f' {k} é {v} ')