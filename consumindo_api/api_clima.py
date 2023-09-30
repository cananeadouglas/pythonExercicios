#534118531af1c8a02d928874f70c262e
#key do registro login: cananeadouglas@hotmail.com, senha: 12345678
import requests
import json
import pprint


cidade = input('escreva a cidade para consulta: ')

requisicao = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='+cidade+'&limit=5&appid=534118531af1c8a02d928874f70c262e')

#tipo python
tempo = json.loads(requisicao.text)

print(tempo)

pprint.pprint(tempo)

# temperatura convertida em celsius
celsius = float((tempo['main']['temp']) - 273.15)
nome_cidade = str(tempo['name'])

print('nome da cidade: ', nome_cidade)
print('Temperatura: ', celsius)