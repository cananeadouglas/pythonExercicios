'''Application Settings
Keep the "Consumer Secret" a secret. This key should never be human-readable in your application.
Consumer Key (API Key)	hxHlNhyDBf9D4Uar9TouIhxdc
Consumer Secret (API Secret)	niYMTIgyAEYK7KzTLmqZafFFqUWfX7a12GDqDkzAHrKfjfssUv

Your Access Token
This access token can be used to make API requests on your own account's behalf. Do not share your access token secret with anyone.
Access Token	84585483-q0askQUpIGqQIQ8vDAhqEz8hiRExydf3no20MaNYR
Access Token Secret	da52LuqM5mG9XSFQXlCYLbxxy6UybbZfVPmXf4jnHetRF
(pip3 install oauth2) no terminal do pycharm
'''


import requests
import json
import oauth2
import pprint
import urllib

consumer_key = 'hxHlNhyDBf9D4Uar9TouIhxdc'
consumer_secret = 'niYMTIgyAEYK7KzTLmqZafFFqUWfX7a12GDqDkzAHrKfjfssUv'

token_key = '84585483-q0askQUpIGqQIQ8vDAhqEz8hiRExydf3no20MaNYR'
token_secret = 'da52LuqM5mG9XSFQXlCYLbxxy6UybbZfVPmXf4jnHetRF'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

query = input('Novo Twitter? ')
query_code = urllib.parse.quote(query, safe='')
requisicao = client.request('https://api.twitter.com/1.1/statuses/update.json?status='+query_code, method='POST')

decodificar = requisicao[1].decode()

#objeto dict
objeto = json.loads(decodificar)

pprint.pprint('ok. publicado' if objeto['user']['name'] == 'Douglas Cananéa' else 'há alguma coisa errada')
