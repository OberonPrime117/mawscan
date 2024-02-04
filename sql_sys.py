import sqlite3

conn = sqlite3.connect('filesystem.db')
cursor = conn.execute("SELECT fullpath FROM filesystem WHERE filetype==\"exe\"")
rows = cursor.fetchall()
print(rows)
for row in rows:
	print(row[0])