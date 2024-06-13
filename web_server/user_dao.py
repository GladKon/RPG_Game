import sqlite3
import bcrypt


class UserDAO:
    def __init__(self, name):
        self._name = name

    def _connect(self):
        return sqlite3.connect(self._name)

    def create_table_users(self):
        with self._connect() as connect:
            cursor = connect.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIME
            )
            ''')

            connect.commit()

    def create_table_character_types(self):
        with self._connect() as connect:
            cursor = connect.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS character_types (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                main_type TEXT UNIQUE NOT NULL,
                type_name TEXT UNIQUE NOT NULL
                
            )
            ''')

            connect.commit()

    def create_table_characters(self):
        with self._connect() as connect:
            cursor = connect.cursor()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                character_type_id INTEGER,
                character_name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIME,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(character_type_id) REFERENCES character_types(id)
                
            )
            ''')

            connect.commit()

    def add_user(self, username, password):
        password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=5))

        with self._connect() as connect:
            cursor = connect.cursor()


            cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, hashed_password))
            connect.commit()
    def delite_user(self, username):
        with self._connect() as connect:
            cursor = connect.cursor()
            connect.execute("DELETE FROM users WHERE username= ?", (username,))

            connect.commit()
            cursor.close()

    def drop_table_users(self):
        with self._connect() as connect:
            cursor = connect.cursor()
            cursor.execute('''
                DROP TABLE IF EXISTS users;
            ''')

            connect.commit()

    def drop_table_character_types(self):
        with self._connect() as connect:
            cursor = connect.cursor()
            cursor.execute('''
                DROP TABLE IF EXISTS character_types;
            ''')

            connect.commit()

    def drop_table_character(self):
        with self._connect() as connect:
            cursor = connect.cursor()
            cursor.execute('''
                   DROP TABLE IF EXISTS character;
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
    userdao.drop_table_users()
    userdao.create_table_characters()
    userdao.create_table_character_types()
    userdao.create_table_users()
    userdao.add_user('1','1')
    userdao.add_user('2','2')