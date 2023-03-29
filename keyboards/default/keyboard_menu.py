from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# СОЗДАЛИ КНОПКИ КАЖДЫЙ МАССИВ ОТДЕЛЬНЫЕ строки  И ПОДКЛЮЧИЛИ КЛАВИАТУРУ
kb_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Случайная книга'),
    ],
    [
        KeyboardButton(text='Рейтинг книг'),
    ],
    [
        KeyboardButton(text='Информация о авторе'),
        KeyboardButton(text='another1'),
        KeyboardButton(text='another2'),

    ]
], resize_keyboard= True) # ЧТОБ КНОПКИ НЕ БЫЛИ НА ПОЛ ЭКРАНА
