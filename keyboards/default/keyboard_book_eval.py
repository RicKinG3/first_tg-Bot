# смена на другое меню при выборе рейтинг книг
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_book_eval = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='1) За все время'),
        KeyboardButton(text='2) За месяц'),
        KeyboardButton(text='3) За день'),
    ],
    [
        KeyboardButton(text='/menu')
    ]

], resize_keyboard=True)  # ЧТОБ КНОПКИ НЕ БЫЛИ НА ПОЛ ЭКРАНА
