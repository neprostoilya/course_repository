# Найти бота https://t.me/Trans_let_bot



 

from library.db import get_token, db_history_write, db_history_read
from library.keyboards import generate_languages, get_key, LANGUAGES

from googletrans import Translator

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


TOKEN = get_token()
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



class Questions(StatesGroup):
    src = State()
    dst = State()
    text = State()


@dp.message_handler(commands=['start', 'help', 'about', 'history'])
async def command_start(message: Message):
    if message.text == '/start':
        await message.answer('Здравствуй сударь, вас приветствует Бот переводчик ')
        await start_questions(message)
    elif message.text == '/help':
        await message.answer('Если у вас возникла ошибка пишите к этому челу @neprostoilyaa')
    elif message.text == '/about':
        await message.answer('Данный бот был создан этим челом @neprostoilyaa')
    elif message.text == '/history':
        await get_history(message)

async def get_history(message: Message):
    chat_id = message.chat.id
    stories = db_history_read(chat_id)

    for src, dst, original_text, translate_text in stories[:10]:
        await message.answer(f'''
Вы переводили:
С языка: {src} 
На язык: {dst}
Ваш текст: {original_text}
Бот перевел: {translate_text}''')


async def start_questions(message: Message):
    await Questions.src.set()
    await message.answer('С какого языка хотите перевести? ',
                         reply_markup=generate_languages()) 
        
@dp.message_handler(content_types=['text'], state=Questions.src)
async def confirm_src_ask_dst(message: Message, state: FSMContext):
    if message.text in LANGUAGES.values():
        async with state.proxy() as data:
            data['src'] = message.text
        await Questions.next()
        await message.answer(f'Вы выбрали {message.text}\nВыберите на какой язык перевести',
                                reply_markup=generate_languages())
    elif message.text in ['/start', '/help', '/about', '/history']:
            await state.finish()
    else: 
        await message.answer('Такого языка нет!')


    

@dp.message_handler(content_types=['text'], state=Questions.dst)  
async def confirm_dst_ask_text(message: Message, state: FSMContext):
    if message.text in LANGUAGES.values():
        async with state.proxy() as data: 
            data['dst'] = message.text
        await Questions.next()
        await message.answer(f"Начинаем перевод с {data['src']}, на {data['dst']}\nВведите текст, который хотите перевести",
                            reply_markup=ReplyKeyboardRemove())
    else: 
        await message.answer('Такого языка нет!')




@dp.message_handler(content_types=['text'], state=Questions.text)
async def confirm_text_translate(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text

    src = get_key(data['src'])
    dst = get_key(data['dst'])
    text = data['text']
    try:
        translator = Translator()
        trans_text = translator.translate(text=text, src=src, dest=dst).text
    except:
        await message.answer('Ошибка в написаниях слова повторите попытку!')
        await start_questions(message)
    else:
        chat_id = message.chat.id
        db_history_write(chat_id, src, dst, text, trans_text)

        await message.answer(trans_text)
        await state.finish()
        await start_questions(message)



executor.start_polling(dp)