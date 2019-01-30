import sqlite3, datetime, time, json

lista = []

connection = sqlite3.connect('rifa_com_bancodedados.db')
c = connection.cursor()
resposta = ' '

while True:
    def create_table():
        c.execute("create table if not exists cadastro (id integer primary key, nome text, telefone integer, datacadastro text)")

    def dataentry(nome, telefone, datacadastro):
        c.execute("insert into cadastro (nome, telefone, datacadastro) values (?,?,?)",
                  (nome, telefone, datacadastro))
        connection.commit()

    tela = int(input('digite 1 para cadastrar participante\n'
                 'digite 2 para consultar dados do participante\n'
                 'digite 3 para sair\n'))

    if tela == 1:
        create_table()
        nome = str(input('digite aqui seu nome completo: '))
        telefone = int(input('digite seu telefone para contato: '))
        datacadastro = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d.%m.%Y %H:%M:%S'))
        # para converter uma string personalizada da hora (.strftime('%Y.%m.%d %H:%M:%S'))

        # verificar se já existe usuário no sistema
        dataentry(nome, telefone, datacadastro)
        print('CADASTRADO COM SUCESSO')
    elif tela == 2:
        tela2 = int(input('digite 1 para consultar por telefone: \n'
                          'digite 2 para consultar por nomes: \n'
                          'digite 3 para listar todos os nomes \n'))
        if tela2 == 1:
            tel = int(input('digite numero de telefone: '))
            sql1 = "select * from cadastro where telefone = ?" \

            def leituranum(tel,):
                for row in c.execute(sql1, (tel,)):
                    print('usuario cadastrado no dia {},\nnome completo {}\ne o telefone {}'.format(row[3], row[1].upper(), row[2]))

            leituranum(tel)
        elif tela2 == 2:
            nom = str(input('digite nome da pessoa: '))
            sql2 = "select * from cadastro where nome like ?"

            def leituranome(nom,):
                for row in c.execute(sql2, (nom,)):
                    print(row)

            leituranome(nom)
        elif tela2 == 3:
            sql3 = "select nome, telefone, datacadastro from cadastro "

            def leituratudo():
                for row in c.execute(sql3,):
                    print(row)

            leituratudo()
            connection.commit()
    elif tela == 3:
        break
        c.close()
    else:
        print('vc digitou um numero errado, digite de 1 a 3')
