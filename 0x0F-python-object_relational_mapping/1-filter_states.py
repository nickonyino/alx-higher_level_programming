#!/usr/bin/python3

import mySQLdb
import sys

def lis_state(username, password, database):
    try:
        connection = MySQLdb.connect(
                host =  "localhost",
                port = 3306,
                user = username,
                passwd = password,
                db = database
                )
        cursor =  connection.cursor()
        querry = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)
        states - cursor.fetchall()

        for states in states:
        print(state)
    except MySQLdb.Error as e:
        print("MySQL Eroor:", e)

    finally:
        if 'çonnection' in locals() and connection.open:
            cursor.close()
            connection.close()
            print("Database connection closed.")

            if __name__ == "__main__":
                if len(sys.argv) != 4:
                    print("Usage: python script.py <username> <password> <database>")
            else:
                username = sys.argv[1]
                password = sys.argv[2]
                database = sys.argv[3]
                list_states(username, password, database)



