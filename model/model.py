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
    print('creating tables...')
    # books
    '''
    url: kind of book id. syntax: title(only lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create date (example: the-book-20231214)
    title: the name of the book. syntax: Captalized Text
    author
    tags: split in comma(,)
    update_datetime: last update datetime
    description: text
    # homepage: the first page of the book. syntax: page id
    # (homepage: the 1st page in the pages list?)
    pages: pages of the book. split in comma(,)
    view_count: unsigned integer
    '''
    try:
        execute('CREATE TABLE books(url PRIMARY KEY, title, author, update_datetime, tags, description, pages, view_count)')
    except sqlite3.OperationalError:
        print(f'table "books" has exist')

    # pages
    '''
    url: kind of page id. syntax: book title - title(only lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create date (example: the-book-20231214)
    title
    author
    tags: split in comma(,)
    update_datetime
    content: markdown & html
    question: html
    book_id: book id (if it belongs to book)
    view_count: unsigned integer
    '''
    try:
        execute('CREATE TABLE pages(url PRIMARY KEY, title, author, update_datetime, tags, content, question, book_id, view_count)')
    except sqlite3.OperationalError:
        print(f'table "pages" has exist')

    # user
    '''
    username: user id. syntax: Uppercase and lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create date (example: the-book-20231214)
    name: display name of the user. No limitation.
    email
    passkey
    otp_key
    sessions: session id. array, split in comma(,)
    interests: tags   , split in comma(,), 2D array with weights
    weights:   weights, split in comma(,), 2D array with interests
    reading_history: reading history id. array, split in comma(,)
    question_history: question history id. array, split in comma(,)
    '''
    try:
        execute('CREATE TABLE users(username PRIMARY KEY, name, email, passkey, otp_key, sessions, interests, weights, reading_history, question_history)')
    except sqlite3.OperationalError:
        print(f'table "users" has exist')

    # session
    '''
    id: session id.
    username: user id.
    create_datetime
    expire_datetime
    device: text
    '''
    try:
        execute('CREATE TABLE sessions(id PRIMARY KEY, username, create_datetime, expire_datetime, device)')
    except sqlite3.OperationalError:
        print(f'table "sessions" has exist')

    # reading history
    '''
    id: reading history id.
    username: user id.
    page_id: page id.
    start_datetime
    update_datetime
    duration: in seconds.
    '''
    try:
        execute('CREATE TABLE reading_history(id PRIMARY KEY, username, page_id, start_datetime, update_datetime, duration)')
    except sqlite3.OperationalError:
        print(f'table "reading_history" has exist')

    # question history
    '''
    id: question history id.
    username: user id.
    page_id: page id.
    finish_datetime
    times_count: unsigned integer. This is the (x) time the user answer the question of the page.
    score: integer
    all_correct: 0 (some questions are wrong) / 1 (all correct) / -1 (not applicable, for instance: open questions)
    '''
    try:
        execute('CREATE TABLE question_history(id PRIMARY KEY, username, page_id, finish_datetime, time_count, score, all_correct)')
    except sqlite3.OperationalError:
        print(f'table "question_history" has exist')

    commit()


# sample data initialize
def sample_data():
    create_table()
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
        # execute('CREATE TABLE books(url, title, author, last_update, tags, homepage, pages)')
        res = execute('SELECT * FROM books').fetchall()
        if len(res) == 0:
            books = [
                # url       title     author      update_datetime  tags                description pages                     view_count
                ('book-1', 'Book 1', 'anonymous', datetime.now(), 'First,Celebration', '', 'book-1-2021214-page-1-20231214', 0)
            ]
            executemany('INSERT INTO books VALUES(?, ?, ?, ?, ?, ?, ?, ?)', books)  # write something into the database
            res = execute('SELECT * FROM books').fetchall()
            print(f'table books:\n{res}')
    except sqlite3.OperationalError:
        # res = execute('SELECT * FROM books').fetchall()
        # print(f'table "books" has exist, data:\n{res}')
        print('Error occurred when inserting data into book table')

    # pages
    try:
        # execute('CREATE TABLE pages(url, title, author, last_update, tags, content)')
        res = execute('SELECT * FROM pages').fetchall()
        if res == 0:
            pages = [
                # url                               title     author      update_datetime  tags                 content                         question book_id view_count
                ('book-1-2021214-page-1-20231214', 'Page 1', 'anonymous', datetime.now(), 'First,Celebration', 'This is the 1 page of Book 1.', '', 'book-1', 0)
            ]
            executemany('INSERT INTO pages VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', pages)  # write something into the database
            res = execute('SELECT * FROM pages').fetchall()
            print(f'table pages:\n{res}')
    except sqlite3.OperationalError:
        # res = execute('SELECT * FROM pages').fetchall()
        # print(f'table "pages" has exist, data:\n{res}')
        print('Error occurred when inserting data into pages table')

    # other tables

    # commit
    commit()

# sample_data()
# create_table()


# do something before close
import atexit

@atexit.register
def close():
    global connection
    connection.close()