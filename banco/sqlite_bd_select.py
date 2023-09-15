import sqlite3

connection = sqlite3.connect('tutorial.db')
c = connection.cursor()

def read_data(wordUser, aqui):
    sql = "select * from dados where keyword = ? and value = ?"
    for row in c.execute(sql, (wordUser, aqui)):
        print(row)

idade = int(input('Digite a idade: '))
nome = input('Digite o nome: ')

read_data(nome, idade)