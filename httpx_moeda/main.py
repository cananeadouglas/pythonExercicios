import httpx

while True: 
    #base_currency = input('digite a moeda base: ').upper()
    #corrente = input('digite a moeda desejada: ').upper()
    
    base = input('ditie a moeda seguida de : ').upper()
    
    ticker = base.split(':')

    response = httpx.get( f'https://api.exchangerate.host/latest?base={ticker[0]}' ).json()

    currency_data = response['rates']
    print ('                           ')
    print (f'1 {ticker[0]} vale {currency_data.get(ticker[1])} {ticker[1]}')
    print ('---------------------------')
    print ('                           ')