import mysql.connector

conn = mysql.connector.connect(host='localhost',username='root',password='nil@2001',database='python')
my_cursor=conn.cursor()

conn.commit()
conn.close()
print("DONE !!")