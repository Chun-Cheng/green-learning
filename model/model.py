import sqlite3
from datetime import datetime

connection = sqlite3.connect("./model/green_learing.db")
cursor = connection.cursor()

def commit():
    connection.commit()

def execute(statement: str, data: tuple = ()):
    return cursor.execute(statement, data)

def executemany(statement: str, data: list):
    return cursor.executemany(statement, data)


def create_table():
    # books
    '''
    url: kind of book id. syntax: title(only lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create date (example: the-book-20231214)
    title: the name of the book. syntax: Captalized Text
    tags: split in comma(,)
    ...
    homepage: the first page of the book. syntax: page id
    pages: pages of the book. split in comma(,)
    '''
    try:
        execute('CREATE TABLE books(url PRIMARY KEY, title, author, last_update, tags, homepage, pages)')
    except sqlite3.OperationalError:
        print(f'table "books" has exist')

    # pages
    '''
    url: kind of page id. syntax: book title - title(only lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create date (example: the-book-20231214)
    ...
    tags: split in comma(,)
    content: markdown
    '''
    try:
        execute('CREATE TABLE pages(url PRIMARY KEY, title, author, last_update, tags, content)')
    except sqlite3.OperationalError:
        print(f'table "pages" has exist')

    # user
    '''
    username: user id. syntax: Uppercase and lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create date (example: the-book-20231214)
    ...
    tags: split in comma(,)
    content: markdown
    '''
    try:
        execute('CREATE TABLE pages(url PRIMARY KEY, title, author, last_update, tags, content)')
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
        execute('CREATE TABLE books(url, title, author, last_update, tags, homepage, pages)')
        books = [
            ('book-1', 'Book 1', 'anonymous', datetime.now(), 'First,Celebration', "book-1-2021214-page-1-20231214", "book-1-2021214-page-1-20231214")
        ]
        executemany('INSERT INTO books VALUES(?, ?, ?, ?, ?, ?, ?)', books)  # write something into the database
        res = execute('SELECT * FROM books').fetchall()
        print(f'table books:\n{res}')
    except sqlite3.OperationalError:
        res = execute('SELECT * FROM books').fetchall()
        print(f'table "books" has exist, data:\n{res}')

    # pages
    try:
        execute('CREATE TABLE pages(url, title, author, last_update, tags, content)')
        pages = [
            ('book-1-2021214-page-1-20231214', 'Page 1', 'anonymous', datetime.now(), 'First,Celebration', "This is the 1 page of Book 1.")
        ]
        executemany('INSERT INTO pages VALUES(?, ?, ?, ?, ?, ?)', pages)  # write something into the database
        res = execute('SELECT * FROM pages').fetchall()
        print(f'table pages:\n{res}')
    except sqlite3.OperationalError:
        res = execute('SELECT * FROM pages').fetchall()
        print(f'table "pages" has exist, data:\n{res}')

    # other tables

    # commit
    commit()

sample_data()
create_table()


# do something before close
import atexit

@atexit.register
def close():
    global connection
    connection.close()