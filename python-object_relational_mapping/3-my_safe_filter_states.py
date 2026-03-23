#!/usr/bin/python3
""" Lists all values in states table safe from MySQL injections """
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    query_rows = cursor.fetchall()

    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
