
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# row_width = count button in row
ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='ВК', url='https://vk.com/ma4ches'),
                                        InlineKeyboardButton(text='ТГ', url='https://t.me/ma4ches')

                                    ]
                                ])

