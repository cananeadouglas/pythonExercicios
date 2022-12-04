#Web Scraping com python
# pip3 install bs4

import requests
import time
from bs4 import BeautifulSoup

while True:
    
    response = requests.post('http://br.financas.yahoo.com/')

    print ('Status code: ', response.status_code)

    if (response.status_code == 200):
        print('OK')
        #print(response.headers)
        #print(response.content)

        content = response.content

        site = BeautifulSoup(content, 'html.parser')

        #noticia
        post = site.find('span', attrs={'class': 'Trsdu(0.3s) Fz(s) Mt(4px) Mb(0px) Fw(b) D(ib)'})

        #site organizado
        #print(site.prettify())

        print(post.text)
    else:
        print('não vai adiantar')
    
    time.sleep(3)

