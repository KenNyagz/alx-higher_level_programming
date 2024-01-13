#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

# if __name__ == "__main__":
def main (argv):
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract cmd-line args
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object to execute sql queries
    cursor = db.cursor()

    # Execute MySQL qurery to fetch all states and sort by states.id
    states = cursor.fetchall()

    # Display results
    for state in states:
        print(state);

    cursor.close()
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
