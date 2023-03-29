# ТУт будут все функции пользователя
from aiogram import types, exceptions
from loader import dp


# Когда пользователь отправляет сообщение боту, библиотека aiogram
# передает это сообщение функции-обработчику. Декоратор @dp.message_handlers() говорит библиотеке
# , что эта функция должна быть вызвана при обработке всех типов сообщений, включая текстовые, аудио, фото и т.д.
@dp.message_handler(text='/start')  # start this func is commsnd is /start
async def command_start(message: types.Message):
    try:
        with open('static/AnimatedSticker.tgs', 'rb') as sticker_file:
            sticker = types.InputFile(sticker_file)
            # Send the sticker to the user
            await message.answer_sticker(sticker)
    except exceptions.TelegramAPIError as e:
        print(f"Ошибка отправки стикера: {e}")

    await message.answer(f'Привет {message.from_user.full_name}) Я могу помочь тебе с выбором книг! \n'
                         f'Твой Айди: {message.from_user.id}')
