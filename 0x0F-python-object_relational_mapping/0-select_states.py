#!/usr/bin/python3
"""
script should take 3 arguments: mysql username, mysql password and database name
"""
import MySQLdb
from sys import argv


def myFunction(username, password, name):
    """
    the function to return all methods
    Args:
        username: the db username
        password: db password
        name: name
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=str(username),
                         passwd=str(password), db=str(name), charset="utf8")
    cur = db.cursor()
    tablSelect = cur.execute("SELECT * FROM states ORDER BY id;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()


if __name__ == '__main__':
    myFunction(argv[1], argv[2], argv[3])
