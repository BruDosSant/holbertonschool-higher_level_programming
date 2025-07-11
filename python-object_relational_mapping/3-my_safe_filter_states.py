#!/usr/bin/python3
"""Lists all states matching a name passed as argument"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = db.cursor()
    # this uses parameterization to avoid SQL injection
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
