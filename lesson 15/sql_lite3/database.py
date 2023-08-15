import sqlite3

def connect_db():
    return  sqlite3.connect('lesson 15/sql_lite3/sql.db.db')

def create_table():
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS translate_history(
        history_id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id BIGINT,
        src VARCHAR(30),
        dst VARCHAR(30),
        original_text VARCHAR,
        translate_text VARCHAR   
    );
    ''')
    database.commit()
    database.close()


def create_bot_table():
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bot(
        bot_id  INTEGER PRIMARY KEY AUTOINCREMENT,
        bot_name VARCHAR(20),
        bot_token VARCHAR
    );
    ''')
    database.commit()
    database.close() 

def get_token():
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        SELECT bot_token FROM bot WHERE bot_name = (?);
    ''', ('translate', ))
    token = cursor.fetchone()
    database.close()
    return token[0]

def db_history_write(telegram_id, src, dst, original_text, translate_text):
    """Функция для записи истории переводов пользователя"""
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO translate_history(telegram_id, src, dst, original_text, translate_text)
    VALUES ((?),(?),(?),(?),(?))
    ''', (telegram_id, src, dst, original_text, translate_text))
    database.commit()
    database.close()


def db_history_read(telegram_id):
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
    SELECT src, dst, original_text, translate_text FROM translate_history
    WHERE telegram_id = (?);
    ''', (telegram_id,))
    history = cursor.fetchall()
    history = history[::-1]
    database.close()
    return history
