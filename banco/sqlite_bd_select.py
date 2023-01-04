import sqlite3, datetime, time

connection = sqlite3.connect('tutorial.db')
c = connection.cursor()

idade = int(input('digita idade '))
nome = input('digita nome ')

sql2 ="select * from dados where keyword = ? and value = ?"

def read_data(wordUser, aqui):
    for row in c.execute(sql2, (wordUser, aqui,)):
        print(row)

read_data(nome, idade)