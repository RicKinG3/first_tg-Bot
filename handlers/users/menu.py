from  aiogram import  types
from  loader import  dp
from  aiogram.dispatcher.filters import  Command

from  keyboards.default import kb_menu
@dp.message_handler(Command("/menu")) # filter for input commands
async def menu(message: types.Message):
    await message.answer("Выбери число из меню ниже", reply_markup=kb_menu)
