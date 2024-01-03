import sqlite3
from datetime import datetime
import textwrap
import json
import os

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
    url: kind of book id. syntax: title(only lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create time (the last 5 digit in milliseconds)  # create date (example: the-book-20231214)
    title: the name of the book. syntax: Captalized Text
    author
    reference
    tags: split in comma(,), not case-sensitive
    update_datetime: last update datetime
    description: text
    # homepage: the first page of the book. syntax: page id
    # (homepage: the 1st page in the pages list?)
    pages: pages of the book. split in comma(,)
    view_count: unsigned integer
    '''
    try:
        execute('CREATE TABLE books(id PRIMARY KEY, title, author, reference, update_datetime, tags, description, pages, view_count)')
    except sqlite3.OperationalError:
        print(f'table "books" has exist')

    # pages
    '''
    url: kind of page id. syntax: book title - title(only lowercase alphabet, numeric, underscore(_), and hyphen(-) are supported. replace unsupported character with -) - create time (the last 5 digit in milliseconds)  # create date (example: the-book-20231214)
    title
    author
    reference
    tags: split in comma(,), not case-sensitive
    update_datetime
    content: markdown & html
        Don't contain the title.
        Headings starts at h2 (## Heading 2).
        question block syntax:
            <div name="question-block" id="{question-id}">
                ...(question content)...
            </div>
        for instance: <div name="question-block" id="question-1">
    question: html
    book_id: book id (if it belongs to book)
    view_count: unsigned integer
    '''
    try:
        execute('CREATE TABLE pages(id PRIMARY KEY, title, author, reference, update_datetime, tags, content, question, book_id, view_count)')
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

    with open('./model/sample_data.json', encoding='utf-8') as file:
        sample_list = json.loads(file.read())

    # books
    try:
        res = execute('SELECT * FROM books').fetchall()
        if len(res) == 0:            
            books = []
            for book in sample_list['books']:
                books.append((
                    book['url'],
                    book['title'],
                    book['author'],
                    book['reference'],
                    book['update_datetime'],
                    book['tags'],
                    book['description'],
                    book['pages'],
                    book['view_count']
                ))
            executemany('INSERT INTO books VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', books)  # write something into the database
        else:
            print('The books table is not empty. Sample data generation is canceled.')
    except sqlite3.OperationalError:
        print('Error occurred when inserting data into book table')

    # pages
    try:
        res = execute('SELECT * FROM pages').fetchall()
        if len(res) == 0:
            pages = []
            for page in sample_list['pages']:
                with open(page['content_path'], encoding='utf-8') as file:
                    content = file.read()
                pages.append((
                    page['url'],
                    page['title'],
                    page['author'],
                    page['reference'],
                    page['update_datetime'],
                    page['tags'],
                    content,
                    page['questions'],
                    page['book_id'],
                    page['view_count']
                ))
            executemany('INSERT INTO pages VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', pages)  # write something into the database
        else:
            print('The pages table is not empty. Sample data generation is canceled.')
    except sqlite3.OperationalError:
        print('Error occurred when inserting data into pages table')

    # users
    try:
        res = execute('SELECT * FROM users').fetchall()
        if len(res) == 0:
            users = [(
                'user',  # username
                '使用者',  # name
                'user@email.com',  # email
                '',  # passkey
                '',  # opt-key
                '',  # sessions
                '',  # interests
                '',  # weights
                '',  # reading_history
                '',  # question_history
            )]
            executemany('INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', users)  # write something into the database
        else:
            print('The users table is not empty. Sample data generation is canceled.')
    except sqlite3.OperationalError:
        print('Error occurred when inserting data into users table')
    
    # other tables

    commit()


# do something before close
import atexit

@atexit.register
def close():
    global connection
    connection.close()