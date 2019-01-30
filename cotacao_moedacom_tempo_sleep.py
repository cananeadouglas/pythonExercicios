import requests
import json
import time
import datetime

while True:
    requisicao = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
    cotacao = json.loads(requisicao.text)
    print('cotação', datetime.datetime.now())
    print('Dólar: ', cotacao['valores']['USD']['valor'])
    print('Euro: ', cotacao['valores']['EUR']['valor'])
    print('Bitcoin: ', cotacao['valores']['BTC']['valor'])
    time.sleep(3)