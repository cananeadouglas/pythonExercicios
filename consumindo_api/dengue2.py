from urllib.resquest import urlopen # pip install urllib3

response = urlopen("https://info.dengue.mat.br/api/alertcity?geocode=3106200&disease=dengue&format=json&ew_start=1&ew_end=7&ey_start=2024&ey_end=2024").read().decode('utf8')
dados = json.loads(response)[0]
    
print(dados)