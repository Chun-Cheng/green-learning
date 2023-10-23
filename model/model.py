import sqlite3
from datetime import datetime

connection = sqlite3.connect("./model/green_learing.db")
cursor = connection.cursor()

def commit():
    connection.commit()

def execute(statement: str):
    return cursor.execute(statement)

def executemany(statement: str, data: list):
    return cursor.executemany(statement, data)


# do something before close
import atexit

@atexit.register
def close():
    global connection
    connection.close()