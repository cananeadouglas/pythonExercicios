#Web Scraping com python
# pip3 install bs4

import requests
from bs4 import BeautifulSoup

response = requests.post('https://www.ig.com.br/')

print ('Status code: ', response.status_code)

#print(response.headers)
#print(response.content)

content = response.content

site = BeautifulSoup(content, 'html.parser')

#noticia
post = site.find('h2', attrs={'data-tb-region-item': 'taboola-region'})

#site organizado
#print(site.prettify())

print(post.text)
