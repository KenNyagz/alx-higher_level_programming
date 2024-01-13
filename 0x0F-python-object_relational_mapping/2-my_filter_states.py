#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states
   table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """displays all values in the states table of hbtn_0e_0_usa"""
    if (len(sys.argv) < 5):
        sys.exit(1)

    db = MySQLdb.connect(port=3306,
                         host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         )
    state_name = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY state.id ASC".\
            format(state_name)
    cursor.execute(query)

    result = cursor.fetchall()
    for row in result:
        print(row)

    cursor.close()
    db.close()
