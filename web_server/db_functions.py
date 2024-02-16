import sqlite3


def create_db():
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    connect.commit()
    connect.close()


def add_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()


    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))


    conn.commit()
    conn.close()


def is_exist(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()


    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))


    user = cursor.fetchone()
    conn.close()
    return user is not None


def validate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None
