#Web Scraping com python
# pip3 install bs4

import requests
import time
from bs4 import BeautifulSoup

while True:
    
    ticker = input('digite ticket da empresa: ')  
    
    response = requests.post('https://www.fundsexplorer.com.br/funds/'+ticker)
    print ('Aguarde, coletando informações')

    print ('Status code: ', response.status_code)

    if (response.status_code == 200):
        #print('OK')
        content = response.content
        try:
            site = BeautifulSoup(content, 'html.parser')
            post = site.find('div', attrs={'class': 'headerTicker__content__price'})
            preco = post.find('p')

            print('Preço: ', preco.text)
            
        except (AttributeError):
            print('atributo não identificado, ou qq outro erro interno')
            time.sleep(3)

    else:
        print('não vai adiantar')
    
    time.sleep(1)