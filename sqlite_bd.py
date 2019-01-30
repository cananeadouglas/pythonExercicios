import sqlite3, datetime, time

nome = str(input('digite aqui seu nome '))
reale = float(input('digame um valor real '))
idade = int(input('sua idade '))
dia = int(input('dia de hoje '))
datnow = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d.%m.%Y %H:%M:%S'))
# para converter uma string personalizada da hora (.strftime('%Y.%m.%d %H:%M:%S'))

connection = sqlite3.connect('tutorial.db')
c = connection.cursor()

def create_table():
    c.execute("create table if not exists dados (id integer, unix real, keyword text, datestamp text, value real)")

create_table()

def dataentry():
    c.execute("insert into dados (id, unix, keyword, datestamp, value) values (?,?,?,?,?)", (dia, reale, nome, datnow, idade))
    connection.commit()

dataentry()



