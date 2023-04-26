import mysql.connector
from mysql.connector import Error
 
conn = mysql.connector.connect(
    host="localhost",
    user="douglas",
    passwd="123456",
    db="futebol",
    port="3306"
)

cur  = conn.cursor()
country = "Mexico"

query = f"INSERT INTO national_team (country) VALUES ('{country}')"

cur.execute(query)
print(f"{cur.rowcount} details inserted")
conn.commit()
conn.close()