# create db table 

import sqlite3

with sqlite3.connect("blog.db") as con:
    c = con.cursor()

    # create table called posts
    c.execute("CREATE TABLE posts (title TEXT, post TEXT)")

    # insert data to the table
    c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
    c.execute('INSERT INTO posts VALUES("Excellent", "I\'m excellent.")')
    c.execute('INSERT INTO posts VALUES("Okay", "I\'m okay.")')