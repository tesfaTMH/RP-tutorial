# mathematical operation on db
import sqlite3

with sqlite3.connect("new_db.db") as con:
    cursor = con.cursor()

    sql_dict = {
        'average': "SELECT avg(population) FROM population",
        'maximum': "SELECT max(population) FROM population",
        'minimum': "SELECT min(population) FROM population",
        'sum': "SELECT sum(population) FROM population",
        'count': "SELECT count(city) FROM population",
    }

    for keys, values in sql_dict.items():
        cursor.execute(values)

        result = cursor.fetchone()

        print(keys + ": ", result[0])