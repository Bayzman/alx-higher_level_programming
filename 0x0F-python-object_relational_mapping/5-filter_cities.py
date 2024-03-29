#!/usr/bin/python3

""" takes in the name of a state as an argument and lists all cities of \
that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("""SELECT c.name FROM cities as c INNER JOIN states\
as s ON s.id=c.state_id WHERE s.name=%s""", (argv[4], ))

    rows = cursor.fetchall()
    city_list = []
    for row in rows:
        city_list.append(row[0])

    print(*city_list, sep=", ")
    cursor.close()
    db.close()
