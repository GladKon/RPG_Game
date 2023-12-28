import sqlite3


def create_db():
    # Подключение к базе данных (или создание, если она не существует)
    conn = sqlite3.connect('../users.db')
    cursor = conn.cursor()

    # Создание таблицы, если она ещё не создана
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def add_user(username, password):
    conn = sqlite3.connect('../users.db')
    cursor = conn.cursor()

    # Добавление нового пользователя
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()


def is_exist(username):
    conn = sqlite3.connect('../users.db')
    cursor = conn.cursor()

    # Проверка существования пользователя
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user is not None


def validate_user(username, password):
    conn = sqlite3.connect('../users.db')
    cursor = conn.cursor()

    # Проверка соответствия логина и пароля
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None


