import sqlite3
conn = sqlite3.connect('delay.db')
c = conn.cursor()
row=[row for row in c.execute('SELECT DISTINCT * FROM delay WHERE Source="ndls" and Destination="ald" ORDER BY delay') ]
print row