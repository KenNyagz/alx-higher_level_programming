#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
   all cities of that state
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """ lists all cities of that state, using the database hbtn_0e_4_usa"""
    if (len(sys.argv) < 5):
        sys.exit(1)

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         )
    state = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM cities JOIN states on cities.state_id=states.id\
            WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state,))

    results = cursor.fetchall()
    cities = []
    for row in results:
        if row[4] == state:
            cities.append(row[2])
    print(', '.join(cities))
    cursor.close()
    db.close()
