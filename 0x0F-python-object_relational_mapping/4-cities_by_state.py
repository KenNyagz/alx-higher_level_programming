#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    """lists all cities from db"""
    if (len(sys.argv) < 4):
        sys.exit(1)

    connection = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=sys.argv[1],
                                 passwd=sys.argv[2],
                                 db=sys.argv[3]
                                 )
    cursor = connection.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN\
             states on cities.state_id = states.id ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
