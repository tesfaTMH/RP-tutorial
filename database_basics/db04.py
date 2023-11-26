# insert multiple values to db

import sqlite3

with sqlite3.connect("new_db.db") as conn:
    cursor = conn.cursor()

    cities = [
        ('Boston', 'MA', 600000),
        ('Chicago', 'IL', 270000),
        ('Houston', 'TX', 210000),
        ('Phonex', 'AZ', 150000)
    ]

    conn.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)