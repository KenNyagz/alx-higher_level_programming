#!/usr/bin/python3
"""script that lists all states with a name starting with
   N (upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """ lists all states with a name starting with upper N from a db"""
    if (len(sys.argv) < 4):
        sys.exit(1)

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306
                         )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # cursor.close()
    db.close()
