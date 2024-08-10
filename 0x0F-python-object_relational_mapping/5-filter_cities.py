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
        db=sys.argv[3]
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute the query to fetch all states
    state_name = sys.argv[4]
    cur.execute("SELECT cities.name FROM cities \
            INNER JOIN states ON states.id=cities.state_id \
            WHERE states.name = %s", (state_name,))

    # Fetch and print the results
    for row in cur.fetchall():
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
