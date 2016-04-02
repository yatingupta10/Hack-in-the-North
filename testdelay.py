import sqlite3
conn = sqlite3.connect('delay.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM delay ORDER BY delay'):
        print row
