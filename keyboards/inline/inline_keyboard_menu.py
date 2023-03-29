from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# row_width = count button in row
ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='ВК', url='https://vk.com/ma4ches'),
                                        InlineKeyboardButton(text='ТГ', url='https://t.me/ma4ches')

                                    ],
                                    [
                                        InlineKeyboardButton(text='Перейти к рейтингу книг',
                                                             callback_data='Перейти к рейтингу книг')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Заменить кнопки меню',
                                                             callback_data='Кнопки 2')
                                    ]

                                ])
