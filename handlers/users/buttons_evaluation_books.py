from aiogram import types
from loader import dp
from keyboards.default import kb_book_eval


@dp.message_handler(text='Рейтинг книг')  # start this func is commsnd is /start
async def buttons_choice(message: types.Message):
    await message.answer(f'За какой промежуток времени показать рейтинг ?\n'
                         f'1) За все время\n'
                         f'2) За месяц\n'
                         f'3) За день', reply_markup=kb_book_eval)


@dp.message_handler(text='1) За все время')
async def buttons_choice(message: types.Message):
    await message.answer(f'Список 1')


@dp.message_handler(text='2) За месяц')
async def buttons_choice(message: types.Message):
    await message.answer(f'Список 2')


@dp.message_handler(text='3) За день')
async def buttons_choice(message: types.Message):
    await message.answer(f'Список 3')
