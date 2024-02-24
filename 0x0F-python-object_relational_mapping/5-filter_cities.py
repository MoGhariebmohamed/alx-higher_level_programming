#!/usr/bin/python3
"""
script that put all states with a name starting N from database hbtn_0e_0_usa
"""
import sys
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
    tablSelect = cur.execute("SELECT * FROM `cities` INNER JOIN `states` ON\
                             `cities`.`state_id` = `states`.`id`\
                             ORDER BY `cities`.`id`")
    rows = cur.fetchall()
    for row in rows:
        # for prevent code injection .format(argv[4]) LIKE BINARY'{}'
        if row[4] == sys.argv[4]:
            print("".join(row[2]), ", ",end="")
    # Close all cursors
    cur.close()
    # Close all databases
    db.close()


if __name__ == '__main__':
    myFunction(argv[1], argv[2], argv[3])
    
