import sqlite3

conn = sqlite3.connect("./data/departement.db")
c = conn.cursor()

c.execute("""CREATE TABLE Friends (firstname TEXT, lastname TEXT)""")
c.execute("""INSERT INTO Friends VALUES ("Davy", "Lucas")""")
conn.commit()


c.execute("""SELECT * FROM Friends""")
for row in c:
    print(row)

c.close()
conn.close()
