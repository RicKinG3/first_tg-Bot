from  aiogram import  types
from  loader import  dp


# Когда пользователь отправляет сообщение боту, библиотека aiogram
# передает это сообщение функции-обработчику. Декоратор @dp.message_handlers() говорит библиотеке
# , что эта функция должна быть вызвана при обработке всех типов сообщений, включая текстовые, аудио, фото и т.д.
@dp.message_handler(text = '/help') # start this func is commsnd is /start
async  def command_start(message:  types.Message):
    await message.answer(f'Привет {message.from_user.full_name} \n'
                         f'Чем я могу вам помочь?')
