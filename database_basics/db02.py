# Insert values to db

import sqlite3

conn = sqlite3.connect("new_db.db")

cursor = conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York', 'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San', 'CA', 8000000)")

conn.commit()

conn.close()