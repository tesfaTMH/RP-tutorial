# update and delete db
import sqlite3

with sqlite3.connect("new_db.db") as conn:
    cursor = conn.cursor()

    #Update data
    cursor.execute("UPDATE population SET population=1000000 WHERE city='New York'")

    # delete data
    cursor.execute("DELETE FROM population WHERE city='Boston'")

    print("\nUpdated Data\n")

    cursor.execute("SELECT * FROM population")

    rows = cursor.fetchall()

    for row in rows:
        print(row)