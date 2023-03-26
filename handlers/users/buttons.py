from aiogram import types
from  loader import dp
@dp.message_handler(text = 'Случайная книга') # start this func is commsnd is /start
async def buttons_choice(message:  types.Message):
    await message.answer(f'Таксссс...\nСейчас что-нибудь найду для тебя')
