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
#query = f"INSERT INTO national_team VALUES (7,'Mexico')"
query = f"SELECT * FROM national_team"

cur.execute(query) 
  
rows = cur.fetchall() 
conn.close() 
  
for row in rows : 
    print(row)