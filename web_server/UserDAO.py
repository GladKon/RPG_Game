import sqlite3


import bcrypt


class UserDAO:
    def __init__(self, db_name):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
            ''')
            conn.commit()

    def add_user(self, username, password):
        # password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()

    def is_exist(self, username):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            return cursor.fetchone() is not None

    def validate_user(self, username, password):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password,))
            user = cursor.fetchone()
            if user:
                return True
            return False

    def validate_user2(self, username, password):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            if user:
                stored_password_hash = user[0]
                return bcrypt.checkpw(password.encode('utf-8'), stored_password_hash)
            return False
