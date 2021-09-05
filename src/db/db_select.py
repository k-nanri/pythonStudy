import sqlite3

# DBに接続
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('select * from articles')
for row in c:
    print(row)

c.execute('select * from articles')
for row in c.fetchall():
    print(row)

c.execute('select * from articles')
print(c.fetchone())
print(c.fetchone())

conn.close()
