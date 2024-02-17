#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Checks if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Retrieves MySQL credentials from command line arguments
    username, password, database = sys.argv[1:]

    # Connects to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Creates a cursor object to execute queries
    cursor = db.cursor()

    # Executes query to fetch all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetches all the rows
    states = cursor.fetchall()

    # Displays the results
    for state in states:
        print(state)

    # Closes the cursor and database connection
    cursor.close()
    db.close()
