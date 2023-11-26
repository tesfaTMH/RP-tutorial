# SQLite3 database 

import sqlite3

# create a database 

conn = sqlite3.connect("new_db.db")

cursor = conn.cursor()

cursor.execute(""" CREATE TABLE population 
               (city TEXT, state TEXT, population INT)""")
conn.close()