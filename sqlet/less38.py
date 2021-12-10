import sqlite3
import os
from sqlite3 import Error

def create_connection(db_file):

    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(str(e))
def create_table(connection,sql_string):
    pass



if __name__ == '__main__':
    datebase = os.path.join(os.getcwd(),'mydatebase.db')
    try:
        connection = create_connection(datebase)
    except Error as e:
        print(str(e))
    finally:
        connection.close()

