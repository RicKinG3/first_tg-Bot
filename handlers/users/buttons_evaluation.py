

from aiogram import types
from loader import dp
from  keyboards.default import  kb_book_eval

@dp.message_handler(text='Рейтинг книг')  # start this func is commsnd is /start
async def buttons_choice(message: types.Message):
    await message.answer(f'За какой промежуток времени показать рейтинг ?\n1 - за все время \n2 - за месяц \n3 - за день', reply_markup=kb_book_eval)
