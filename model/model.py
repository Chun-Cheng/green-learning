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


def create_table():
    # books
    try:
        execute('CREATE TABLE books(title, author, datetime, tags, homepage, pages)')
    except sqlite3.OperationalError:
        print(f'table "books" has exist')

    # pages
    try:
        execute('CREATE TABLE pages(title, author, datetime, tags, content)')
    except sqlite3.OperationalError:
        print(f'table "pages" has exist')

    commit()


# sample data initialize
def sample_data():
    print('load sample data...')

    # # articles
    # try:
    #     execute('CREATE TABLE articles(title, author, datetime, tags, content)')
    #     articles = [
    #         ('Article 1', 'anonymous', datetime.now(), 'First, Celebration', "# This Is The First Article  Let's celebrate!")
    #     ]
    #     executemany('INSERT INTO articles VALUES(?, ?, ?, ?, ?)', articles)  # write something into the database
    #     res = execute('SELECT * FROM articles').fetchall()
    #     print(f'table articles:\n{res}')
    # except sqlite3.OperationalError:
    #     res = execute('SELECT * FROM articles').fetchall()
    #     print(f'table "articles" has exist, data:\n{res}')

    # # topics
    # try:
    #     execute('CREATE TABLE topics(title, description, courses)')
    #     topics = [
    #         ('Topic 1', 'How to go green', '101, 102, 103')
    #     ]
    #     executemany('INSERT INTO topics VALUES(?, ?, ?)', topics)  # write something into the database
    #     res = execute('SELECT * FROM topics').fetchall()
    #     print(f'table topics:\n{res}')
    # except sqlite3.OperationalError:
    #     res = execute('SELECT * FROM topics').fetchall()
    #     print(f'table "topics" has exist, data:\n{res}')

    # books
    try:
        execute('CREATE TABLE books(title, author, datetime, tags, homepage, pages)')
        articles = [
            ('Article 1', 'anonymous', datetime.now(), 'First, Celebration', "# This Is The First Article  Let's celebrate!", " ")
        ]
        executemany('INSERT INTO books VALUES(?, ?, ?, ?, ?, ?)', articles)  # write something into the database
        res = execute('SELECT * FROM books').fetchall()
        print(f'table books:\n{res}')
    except sqlite3.OperationalError:
        res = execute('SELECT * FROM books').fetchall()
        print(f'table "books" has exist, data:\n{res}')

    # pages
    try:
        execute('CREATE TABLE pages(title, author, datetime, tags, content)')
        articles = [
            ('Article 1', 'anonymous', datetime.now(), 'First, Celebration', "# This Is The First Article  Let's celebrate!")
        ]
        executemany('INSERT INTO pages VALUES(?, ?, ?, ?, ?)', articles)  # write something into the database
        res = execute('SELECT * FROM pages').fetchall()
        print(f'table articles:\n{res}')
    except sqlite3.OperationalError:
        res = execute('SELECT * FROM pages').fetchall()
        print(f'table "pages" has exist, data:\n{res}')

    # other tables

    # commit
    commit()

# sample_data()
create_table()


# do something before close
import atexit

@atexit.register
def close():
    global connection
    connection.close()