#!/usr/bin/env bash
--script that lists all MySQL databases
import mysql.connector

# Replace these values with your MySQL server information
host = 'your_mysql_host'
user = 'your_mysql_user'
password = 'your_mysql_password'

# Connect to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a query to get a list of all databases
    cursor.execute("SHOW DATABASES")

    # Fetch all the rows
    databases = cursor.fetchall()

    # Print the list of databases
    print("List of Databases:")
    for database in databases:
        print(database[0])

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

