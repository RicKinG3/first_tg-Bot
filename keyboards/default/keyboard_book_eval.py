# сменая на другое меню при выборе рейтинг книг
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_book_eval = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='1 - за все время'),
        KeyboardButton(text='2 - за месяц'),
        KeyboardButton(text='3 - за день'),
        KeyboardButton(text='/menu  '),
    ],

], resize_keyboard= True) # ЧТОБ КНОПКИ НЕ БЫЛИ НА ПОЛ ЭКРАНА
