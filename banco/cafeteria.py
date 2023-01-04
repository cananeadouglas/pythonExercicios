import sqlite3, datetime, time
from pycpfcnpj import gen, cpfcnpj
#pip install pycpfcnpj ou interpretador: procurar por: pycpfcnpj

while True:

    connection = sqlite3.connect('cafeteria.db')
    c = connection.cursor()


    opcao = int(input('digite 1 para cadastro de cliente\n'
                      'digite 2 para cadastro de produto\n'
                      'digite 3 para fazer o pedido\n'
                      'digite 4 para relatório de vendas por dia\n'
                      'digite 5 para consulta de cadastro\n'
                      'digite 6 para alteração de cadastro\n'))

    if opcao == 1:

        cpfuser = input('digite seu cpf válido: ')

        dado = cpfcnpj.validate(cpfuser)

        if dado == True:
            print('trueee')
            cpf = cpfuser
            nomecompleto = str(input('digite nome completo: '))
            datacadastro = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))

            dia = int(input('digite o dia de aniversário '))
            mes = int(input('digite o mes de aniversário '))
            ano = int(input('digite o ano de aniversário '))
            datanascimento = datetime.date(ano, mes, dia)

            num_ddd = int(input('digite seu DDD, 2 dígitos xx: '))
            num_contato = int(input('digite numero de telefone, 9 dígitos: '))


            def create_table():
                c.execute(
                    "create table if not exists cliente (id integer primary key, nomecompleto text, cpf integer, datacadastro text, datanascimento text, dia integer, mes integer, ano integer, ddd integer, contato integer)")


            create_table()


            def dadosentrada():
                c.execute(
                    "insert into cliente (nomecompleto, cpf, datacadastro, datanascimento, dia, mes, ano, ddd, contato) values (?,?,?,?,?,?,?,?,?)",
                    (nomecompleto, cpf, datacadastro, datanascimento, dia, mes, ano, num_ddd, num_contato))
                connection.commit()


            dadosentrada()
        else:
            print('false')



    elif opcao == 2:

        nomeproduto = str(input('digite o nome do produto: '))
        pscliente = str(input('digite alguma observação do cliente: '))
        valorproduto = float(input('digite o valor do produto: '))

        def create_table2():
            c.execute("create table if not exists produto (id integer primary key AUTOINCREMENT, nomeproduto text, pscliente text, valorproduto real)")

        create_table2()

        def dadosproduto():
            c.execute("insert into produto (nomeproduto, pscliente, valorproduto) values (?,?,?)", (nomeproduto, pscliente, valorproduto))
            connection.commit()

        dadosproduto()


    elif opcao == 3:

        acao = str(input('digite número do CPF do usuário: '))
        sql3 = "select * from cliente where cpf = ? "

        for row in c.execute(sql3, (acao,)):
            id = row[0]
            print('usuario: {},\n'
                  'data do cadastro: {},\n'
                  'data do nascimento: {},\n'
                  'fone {} {}.\n'
                  ''.format(row[1], row[3], row[4], row[8], row[9]))

        num = id
        print(num)

        '''if num > 0:
            print('zero ou maior') #estamos aqui
        else:
            print('nada')'''

    elif opcao == 4:
        print('4')
    elif opcao == 5:
        print('5')
    elif opcao == 6:
        print('6')
    else:
        print('opcao errada')

