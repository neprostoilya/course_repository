from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

LANGUAGES = {
    'ru': "Русский",
    'kk': "Казахский",
    'uz': "Узбекский",
    'de': "Немецкий",
    'pl': "Польский",
    'en': "Английский"
}

def get_key(value):
    '''Брать ключ по значению'''
    for k, v in LANGUAGES.items():
        if v == value:
            return k

def generate_languages():
    """функция для кнопок выбора языка"""
    markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)

    button = []
    for lang in LANGUAGES.values():
        btn = KeyboardButton(text=lang)
        button.append(btn)

    markup.add(*button)
    return markup

