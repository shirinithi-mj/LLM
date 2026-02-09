import sqlite3
conn=sqlite3.connect('salesDB/sales.db')
cursor=conn.cursor()
cursor.execute("SELECT * FROM sales")
rows=cursor.fetchall()
for row in rows:
    print(row)
conn.close()