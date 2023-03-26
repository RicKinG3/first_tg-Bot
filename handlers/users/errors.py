from  aiogram import  types , exceptions
from  loader import  dp

@dp.message_handler()
async  def command_error(message:  types.Message):
    try:
        with open('static/AnimatedSticker_01.tgs', 'rb') as sticker_file:
            sticker = types.InputFile(sticker_file)
            # Send the sticker to the user
            await message.answer_sticker(sticker)
    except exceptions.TelegramAPIError as e:
        print(f"Ошибка отправки стикера: {e}")
    await message.answer(f'Команда {message.text} не найдена :(' )
