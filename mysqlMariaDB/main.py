import mysql.connector
from mysql.connector import Error
 
connection = mysql.connector.connect(
    host="localhost",
    user="douglas",
    passwd="123456",
    db="futebol",
    port="3306"
)
 
try:
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        db = cursor.fetchone()
        print("Você está conectado ao banco de dados: ", db)        
except Error as e:
    print("Erro ao conectar ao MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("A conexão MySQL está fechada")
