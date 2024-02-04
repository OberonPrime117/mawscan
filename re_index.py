import sqlite3
conn = sqlite3.connect('filesystem.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM filesystem')
if cursor.fetchone() is not None:
    print('The SQL file is populated')
else:
    print('The SQL file is empty')
