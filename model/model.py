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


# sample data initialize
def sample_data():
    print('load sample data...')

    # articles
    try:
        execute('CREATE TABLE articles(title, author, datetime, tags, content)')
        articles = [
            ('Article 1', 'anonymous', datetime.now(), 'First, Celebration', "# This Is The First Article  Let's celebrate!")
        ]
        executemany('INSERT INTO articles VALUES(?, ?, ?, ?, ?)', articles)  # write something into the database
        res = execute('SELECT * FROM articles').fetchall()
        print(f'table articles:\n{res}')
    except sqlite3.OperationalError:
        res = execute('SELECT * FROM articles').fetchall()
        print(f'table "articles" has exist, data:\n{res}')

    # topics
    try:
        execute('CREATE TABLE topics(title, description, courses)')
        topics = [
            ('Topic 1', 'How to go green', '101, 102, 103')
        ]
        executemany('INSERT INTO topics VALUES(?, ?, ?)', topics)  # write something into the database
        res = execute('SELECT * FROM topics').fetchall()
        print(f'table topics:\n{res}')
    except sqlite3.OperationalError:
        res = execute('SELECT * FROM topics').fetchall()
        print(f'table "topics" has exist, data:\n{res}')

    # other tables

    # commit
    commit()

sample_data()


# do something before close
import atexit

@atexit.register
def close():
    global connection
    connection.close()