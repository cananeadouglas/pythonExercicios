import httpx

while True: 
    base_currency = input('digite a moeda base: ').upper()
    corrente = input('digite a moeda desejada: ').upper()

    response = httpx.get(
        url=f'https://api.exchangerate.host/latest?base={base_currency}'
        
    ).json()

    currency_data = response['rates']
    print ('                           ')

    print (f'1 {base_currency} vale {currency_data.get(corrente)} {corrente}')
    print ('---------------------------')
    print ('                           ')