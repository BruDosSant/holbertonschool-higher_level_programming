#!/usr/bin/python3
""" a script to select all states starting with 'N' from the database """

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%'")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
