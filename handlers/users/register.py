from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from states import Register  # class


@dp.message_handler(text='Регистрация')
async def register_call(message: types.Message):
    await register_(message)


@dp.message_handler(Command('register'))  # /register если бот получил эту команду то будет выполнятся message_handler
async def register_(message: types.Message):
    await message.answer(("Привет ты начал регистрацию\nВведи свое имя:"))
    await Register.m_name.set()  # состояние ввода имени спуск к нижней функции установили это состояние


@dp.message_handler(state=Register.m_name)  # ловим все что вводит пользователь
async def state_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(m_name=answer)
    await message.answer(f"{answer} cколько тебе лет ?\n")
    await Register.m_yaer.set()  # cont to input yare


@dp.message_handler(state=Register.m_yaer)  # ловим все что вводит пользователь
async def state_year(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(m_yaer=answer)

    data = await state.get_data()
    name = data.get('m_name')
    years = data.get('m_yaer')

    await message.answer(f'Регистрация успешно пройдена\n'
                         f'Твое имя {name}\n'
                         f'тебе {years} лет')
    await  state.finish()
