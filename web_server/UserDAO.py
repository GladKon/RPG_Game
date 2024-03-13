import sqlite3
import bcrypt


class UserDAO:
    def __init__(self, name):
        self._name = name

    def _connect(self):
        return sqlite3.connect(self._name)

    def create_db(self):
        with self._connect() as connect:
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

        with self._connect() as connect:
            cursor = connect.cursor()


            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            connect.commit()
    def delite_user(self, username):
        with self._connect() as connect:
            cursor = connect.cursor()
            connect.execute("DELETE FROM users WHERE username= ?", (username,))

            connect.commit()
            cursor.close()

    def clear_table(self):
        with self._connect() as connect:
            cursor = connect.cursor()
            cursor.execute('''
                DROP TABLE IF EXISTS users;
            ''')

            connect.commit()



    def is_exist(self, username):
        with self._connect() as connect:
            cursor = connect.cursor()

            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            return user is not None

    def validate_user(self, username, password):
        with self._connect() as connect:
            cursor = connect.cursor()

            cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
            user = cursor.fetchone()
            if user:
                stored_password = user[0]
                return bcrypt.checkpw(password.encode('utf-8'), stored_password)
            return False


if __name__ == '__main__':
    userdao = UserDAO('users.db')
    userdao.add_user('1','1')
    userdao.add_user('2','2')