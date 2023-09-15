import requests, json, sqlite3

#CRIAR TABELA
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS loteriasp (concurso string, data string, dezenas string)')
        
while True:

    connection = sqlite3.connect('lotofacil.db')
    c = connection.cursor()
    create_table()
    
    opcao = int(input('Digita 1 para consultar ou \n'
                      'digite 2 pra ver o que esta gravado \n'
                      'digite 3 para buscar somente as dezenas \n'))
    
    if opcao == 1:

        #INSERT
        def dadosentrada(concurso):
            
            requisicao = requests.get('https://loteriascaixa-api.herokuapp.com/api/lotofacil/'+concurso)
            resultado = json.loads(requisicao.text)
            data = 'dia do concurso: '+resultado['data']
            dezenas = ' '.join(resultado['dezenasOrdemSorteio'])
            
            c.execute('INSERT INTO loteriasp (concurso, data, dezenas) VALUES (?,?,?)',(concurso, data, dezenas))
            connection.commit()

        #CONSULTAR
        def consultar(concurso):

            c.execute('SELECT concurso FROM loteriasp WHERE concurso = ?', (concurso,))
            if c.fetchone() is None:
                print('Salvando dados do Concurso: '+concurso)
                dadosentrada(concurso)
                connection.commit()
            else:
                print('Dados já cadastrados anteriormente')
                
        concurso = input('digite o número do concurso: ')

        consultar(concurso)
                   
    if opcao == 2:

        for row in c.execute('SELECT * FROM loteriasp;'):
            print('[Concurso: {}],\n'
                '[Data: {}],\n'
                '[Dezenas: {}],\n'.format(row[0], row[1], row[2]))
    
    if opcao == 3:

        for row in c.execute('SELECT dezenas FROM loteriasp;'):
            print('[Dezenas: {}]'.format(row[0]))
        
        print(' ')


