import requests


def get_passagem():
    res = requests.get(information)
    verso = res.json().get('text')
    reference = res.json().get('reference')
    print (reference)
    print (verso)


#url = 'https://bible-api.com/Jo%C3%A3o+3:12?translation=almeida'

base = "https://bible-api.com/"


book = input("Digite o livro: ")
chapter = int(input("Digite o Capitulo: "))
verse = int(input("Digite o versículo: "))


portugues = "translation=almeida"


information = (f'{base}{book}+{chapter}:{verse}?{portugues}')

print (information)
get_passagem()

