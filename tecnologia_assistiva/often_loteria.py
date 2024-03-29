from collections import Counter

# Lista de números fornecida
numeros = [
    2, 3, 4, 5, 7, 8, 9, 11, 14, 17, 19, 20, 22, 23, 25, 1, 2, 3, 4, 5, 10, 11, 14, 15, 17, 18, 19, 20, 22, 24,
    1, 2, 3, 4, 6, 11, 12, 16, 19, 20, 21, 22, 23, 24, 25, 1, 2, 3, 7, 8, 9, 10, 13, 14, 15, 16, 17, 20, 22, 23,
    5, 6, 7, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 22, 24, 2, 5, 6, 7, 9, 10, 12, 16, 17, 18, 19, 20, 21, 23, 24,
    1, 2, 6, 7, 8, 9, 10, 13, 15, 18, 19, 20, 21, 23, 24, 3, 4, 6, 8, 9, 10, 11, 16, 18, 19, 20, 22, 23, 24, 25,
    1, 2, 4, 6, 10, 11, 14, 15, 16, 17, 19, 20, 22, 23, 25, 3, 4, 6, 7, 8, 9, 10, 12, 15, 17, 19, 21, 22, 24, 25,
    3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 17, 18, 20, 21, 25, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 19, 21, 23, 25,
    1, 3, 5, 11, 12, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 3, 4, 6, 9, 10, 14, 15, 16, 17, 19, 20, 21, 23, 24, 25,
    2, 6, 7, 8, 10, 11, 12, 14, 15, 16, 18, 20, 23, 24, 25, 3, 4, 5, 6, 7, 9, 10, 13, 16, 17, 18, 20, 22, 24, 25,
    1, 2, 4, 5, 6, 7, 9, 10, 12, 13, 14, 17, 18, 21, 22,
]

# Contagem da frequência dos números
contagem = Counter(numeros)

# Obtendo os 15 maiores números mais frequentes
maiores_numeros = contagem.most_common(15)

# Exibindo os resultados
for numero, frequencia in maiores_numeros:
    print(f'Número: {numero}, Frequência: {frequencia}')
