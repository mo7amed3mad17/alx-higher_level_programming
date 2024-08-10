#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Create a cursor object
    c = db.cursor()

    # Execute the query to fetch all states
    c.execute("SELECT * FROM states WHERE name LIKE '{}'".format(sys.argv[4]))

    # Fetch and print the results
    for row in c.fetchall():
        print(row)

    # Close the cursor and the database connection
    c.close()
    db.close()
