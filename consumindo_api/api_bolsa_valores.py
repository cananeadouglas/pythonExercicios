import requests, json

token = "dVPJMZo1k3ca2jzWcf6HiV"

opcao = int(input('Digite 1 para consultar POR TICKET\n'
                    'Digite 2 para ver o que está gravado\n'))

if opcao == 1:
    def requisicaoweb():
        url = 'https://brapi.dev/api/quote/' + ticket + '?token=' + token
        print(url)
        requisicao = requests.get(url)
        if requisicao.status_code == 200:
            resultado = json.loads(requisicao.text)
            preco = resultado['results'][0]['marketCap']
            print(f'O preço do ativo é: {preco}')
        else:
            print('Erro na requisição:', requisicao.status_code)

    ticket = input('Digite o ticket da bolsa: ')
    requisicaoweb()

elif opcao == 2:
    # Lógica para ver o que está gravado (não implementado)
    print('ainda não configurado')
else:
    print('Opção inválida')

# https://brapi.dev/api/quote/PETR4?token=gk1553jg9YjogtFAoKebYy


