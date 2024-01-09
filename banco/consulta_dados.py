import sqlite3

def conecta_db():
    conn = sqlite3.connect("/home/jdfc1/cananeadouglas_git/pythonExercicios/banco/rifa_com_bancodedados.db")
    cursor = conn.cursor()
    print("Conectando\n")
    return conn, cursor

def desconectar_db(conn):
    conn.close(); print("\nDesconectando")

def consultar_tudo(cursor):
    
    # consultar dados da tabela
    #| cid | name        | type      | notnull | dflt_value | pk |
    #-------------------------------------------------------------
    #| 1   | id          | INTEGER   | 1       | NULL       | 1  |
    # cursor.execute("""PRAGMA table_info('cliente');""")

    cursor.execute("""SELECT * FROM cadastro;""")

    tudo = cursor.fetchall()

    for linha in tudo:
        print(linha)

conn, cursor = conecta_db()
consultar_tudo(cursor)
desconectar_db(conn)