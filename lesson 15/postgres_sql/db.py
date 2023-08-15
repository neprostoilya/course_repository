import psycopg2


def db_connect():
    database = psycopg2.connect(
        dbname ='postgres',
        host = '127.0.0.1',
        user = 'postgres',
        password = '18960707')
    return database



def create_table():
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS translate_history(
        history_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
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
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bot(
        bot_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        bot_name VARCHAR(20),
        bot_token VARCHAR
    );
    ''')

    database.commit()
    database.close() 

def get_token():
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
        SELECT bot_token FROM bot WHERE bot_name = %s;
    ''', ('translate', ))
    token = cursor.fetchone()
    database.close()
    return token[0]
    


def db_history_write(telegram_id, src, dst, original_text, translate_text):
    """Функция для записи истории переводов пользователя"""
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO translate_history(telegram_id, src, dst, original_text, translate_text)
    VALUES (%s, %s, %s, %s, %s)
    ''', (telegram_id, src, dst, original_text, translate_text))
    database.commit()
    database.close()


def db_history_read(telegram_id):
    """Функция для чтения истории переводов пользователя"""
    database = db_connect()
    cursor = database.cursor()
    cursor.execute('''
    SELECT src, dst, original_text, translate_text FROM translate_history
    WHERE telegram_id = %s;
    ''', (telegram_id,))
    history = cursor.fetchall()
    history = history[::-1]
    database.close()
    return history