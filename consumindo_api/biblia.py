# https://github.com/konexis/Bitcoin_python

import requests
import json
#from twilio.rest import Client
import os
from apscheduler.schedulers.blocking import BlockingScheduler

#sched = BlockingScheduler()


#url = 'https://bible-api.com/Jo%C3%A3o+3:12?translation=almeida'

base = "https://bible-api.com/"

book = input("digite o livro: ")
chapter = input("Digite o Capitulo: ")
verse = input("digite o versículo: ")


portugues = "translation=almeida"

information = ("{}{}+{}:{}?{}".format(base,book,chapter,verse,portugues))

print (information)

#@sched.scheduled_job('interval', seconds=10)
def get_last_bitcoin_price():
    res = requests.get(information)
    verso = res.json().get('text')
    reference = res.json().get('reference')
    print (reference)
    print (verso)
    return verso

#sched.start()

get_last_bitcoin_price()