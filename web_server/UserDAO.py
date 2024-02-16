import sqlite3
import bcrypt


class UserDAO:
    def __init__(self, name):
        self._name = name

    def create_db(self):
        with sqlite3.connect(self._name) as connect:
            cursor = connect.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            ''')

            connect.commit()

    def add_user(self, username, password):
        password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=5))

        with sqlite3.connect('users.db') as connect:
            cursor = connect.cursor()


            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            connect.commit()

    def is_exist(self, username):
        with sqlite3.connect('users.db') as connect:
            cursor = connect.cursor()

            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            return user is not None

    def validate_user(self, username, password):
        with sqlite3.connect('users.db') as connect:
            cursor = connect.cursor()

            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            if user:
                stored_password = user[0]
                return bcrypt.checkpw(password.encode('utf-8'), stored_password)
            return False
