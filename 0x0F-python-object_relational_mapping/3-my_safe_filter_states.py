#!/usr/bin/python3

""" takes in arguments and displays all values in the states table of \
hbtn_0e_0_usa where name matches the argument \
while preventing SQL Injection attack
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE name = %s ORDER BY id',
                   (argv[4], ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
