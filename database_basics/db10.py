# joining data from multiple tables 
import sqlite3

with sqlite3.connect("new_db.db") as conn:
    cursor = conn.cursor()

    cursor.execute("""SELECT population.city, population.population,
                   regions.region FROM population, regions
                   WHERE population.city = regions.city""")
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)