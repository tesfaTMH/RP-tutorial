# creating db from csv file
import csv
import sqlite3

with sqlite3.connect("employees.db") as conn:
    cursor = conn.cursor()

    # read .csv file and assign it to a variable
    employees = csv.reader(open("employees.csv", "r"))

    conn.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
    conn.executemany("INSERT INTO employees(firstname, lastname) VALUES(?, ?)", employees)
