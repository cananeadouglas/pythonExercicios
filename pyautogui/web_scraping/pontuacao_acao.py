#Web Scraping com python
# pip3 install bs4

import requests
import time
from bs4 import BeautifulSoup

while True:
    
    ticker = input('digite ticket da empresa: ')  
    
    response = requests.post('http://br.financas.yahoo.com/quote/'+ticker+'.SA?p='+ticker+'.SA')
    print ('Aguarde, coletando informações')

    #print ('Status code: ', response.status_code)

    if (response.status_code == 200):
        #print('OK')
        content = response.content
        try:
            site = BeautifulSoup(content, 'html.parser')
            post = site.find('span', attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
            print(post.text)
            
        except (AttributeError):
            print('atributo não identificado, ou qq outro erro interno')
            time.sleep(3)

    else:
        print('não vai adiantar')
    
    time.sleep(1)

