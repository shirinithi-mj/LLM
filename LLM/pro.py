import sqlite3
conn=sqlite3.connect('salesDB/sales.db')
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT NOT NULL
)''')
cursor.execute('''INSERT INTO sales (customer_name, product_name, quantity, price, sale_date) VALUES ('alice', 'Laptop', 1, 1200.00, '2023-10-01'), 
               ('bob', 'mouse', 2, 800.00, '2023-10-02'), 
               ('charlie', 'keyboard', 1, 150.00, '2023-10-03'),
                ('dave', 'monitor', 1, 300.00, '2023-10-04'),
               ('eve', 'tablet', 1, 400.00, '2023-10-05'),
               ('frank', 'smartphone', 1, 600.00, '2023-10-06'),
               ('grace', 'smartwatch', 1, 200.00, '2023-10-07'),
               ('hank', 'laptop', 1, 1200.00, '2023-10-08'),
               ('ian', 'desktop', 1, 1500.00, '2023-10-09'),
               ('jack', 'printer', 1, 300.00, '2023-10-10')
''')
conn.commit()
conn.close()