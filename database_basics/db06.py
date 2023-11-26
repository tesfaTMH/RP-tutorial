# iterate through database 
import sqlite3

#with sqlite3.connect("employees.db") as conn:
#    cursor = conn.cursor()
#
#    for row in cursor.execute("SELECT firstname, lastname from employees"):
#        print(row)

with sqlite3.connect("employees.db") as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT firstname, lastname from employees")

    rows = cursor.fetchall()

    for row in rows:
        print(row)