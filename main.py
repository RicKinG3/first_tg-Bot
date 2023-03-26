from aiogram import Bot, Dispatcher, types, exceptions
from aiogram.utils import executor
import config as cf

bot = Bot(token=cf.TOKEN)

# Получите объект dp - Dispatcher:
dp = Dispatcher(bot)

# async в языке Python используется для определения корутины (асинхронной функции.
#  Если бы мы вызвали функцию bot.send_sticker() в синхронном режиме,
#  то наш бот бы заблокировался на время отправки сообщения, и не смог бы
#  одновременно обрабатывать другие запросы от пользователей.
async def sendSticker(chat_id: int, sticker):
    await  bot.send_animation(chat_id=chat_id, animation=sticker)

async def sendText(chat_id: int, text: str):
    await bot.send_message(chat_id=chat_id, text=text)

# Когда пользователь отправляет сообщение боту, библиотека aiogram
# передает это сообщение функции-обработчику. Декоратор @dp.message_handlers() говорит библиотеке
# , что эта функция должна быть вызвана при обработке всех типов сообщений, включая текстовые, аудио, фото и т.д.
@dp.message_handler()
async def getMessage(message: types.Message):  # this simple write  types.Message as message
    # chat_id_types = types.Message.chat.id #var with types.Message
    # FOR send message user  u need id
    chat_id = message.chat.id  # var another

    text_welcome = "Привет я Бот, который поможет тебе с выбором книги!"
    sti_welcome = 'static/AnimatedSticker.tgs'
    try:
        with open(sti_welcome, "rb") as sticker_file:
            await sendSticker(chat_id, sticker_file)
    except exceptions.TelegramAPIError as e:
        print(f"Ошибка отправки стикера: {e}")


    # await используется для ожидания результата выполнения асинхронной операции.
    # Когда программа доходит до строки с await, она приостанавливает выполнение текущей функции и
    # переключается на выполнение других задач до тех пор, пока результат не будет доступен. После того,
    # как результат будет доступен, выполнение функции продолжится дальше.
    await  sendText(chat_id, text_welcome)

    print(message.from_user.id) # print id user

executor.start_polling(dp)
