# Insert values to db

import sqlite3

with sqlite3.connect("new_db.db") as conn:

    cursor = conn.cursor()

    cursor.execute("INSERT INTO population VALUES('New York', 'NY', 8400000)")
    cursor.execute("INSERT INTO population VALUES('San', 'CA', 8000000)")
