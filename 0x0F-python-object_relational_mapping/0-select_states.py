#!/usr/bin/python3

""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
