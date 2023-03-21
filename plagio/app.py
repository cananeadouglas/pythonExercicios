import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def calcula_similaridade(texto1, texto2):
    # Tokeniza e remove stopwords dos textos
    tokens1 = [token.lower() for token in word_tokenize(texto1) if token.lower() not in stopwords.words('portuguese')]
    tokens2 = [token.lower() for token in word_tokenize(texto2) if token.lower() not in stopwords.words('portuguese')]
    
    # Cria um conjunto de palavras únicas nos dois textos
    palavras = set(tokens1 + tokens2)
    
    # Cria um vetor de frequências de palavras para cada texto
    freq1 = nltk.FreqDist(tokens1)
    freq2 = nltk.FreqDist(tokens2)
    
    # Calcula a similaridade entre os vetores de frequência usando a métrica de similaridade de Jaccard
    similaridade = nltk.jaccard_distance(set(freq1), set(freq2))
    
    # Retorna a similaridade
    return 1 - similaridade

texto1 = "O céu é azul e as nuvens são brancas."
texto2 = "As nuvens são brancas e o céu é azul."

similaridade = calcula_similaridade(texto1, texto2)
print("A similaridade entre os textos é:", similaridade)
