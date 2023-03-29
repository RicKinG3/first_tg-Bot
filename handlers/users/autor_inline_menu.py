from loader import dp
from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline import ikb_menu
from keyboards.inline import ikb_menu_autor

from keyboards.default import kb_book_eval


@dp.message_handler(text="Информация о авторе")
async def show_inline_menu(message: types.Message):
    await message.answer('Обратная связь', reply_markup=ikb_menu)


@dp.callback_query_handler(text='Перейти к рейтингу книг')
async def send_message(call: CallbackQuery):
    await call.message.answer("Кнопки Заменены", reply_markup=kb_book_eval)
    await call.answer("Кнопки Заменены", show_alert=True)
    await call.answer("Кнопки Заменены")  # alert = false


@dp.callback_query_handler(text='Кнопки 2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu_autor)  # alert = false
