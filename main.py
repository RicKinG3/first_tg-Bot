# async в языке Python используется для определения корутины (асинхронной функции.
#  Если бы мы вызвали функцию bot.send_sticker() в синхронном режиме,
#  то наш бот бы заблокировался на время отправки сообщения, и не смог бы
#  одновременно обрабатывать другие запросы от пользователей.

async  def on_startup(dp):
    print("MAIN Bot is started")

    from utils.notify_admins import on_startup_notify
    await  on_startup_notify(dp) # Всем админам придет сообщение о запуске бота

    from  utils.set_bot_commands import  set_default_commands
    await  set_default_commands(dp)


if __name__ == '__main__':
    from aiogram  import executor
    from  handlers import  dp

    executor.start_polling(dp, on_startup=on_startup)


# @dp.message_handler()
# async def getMessage(message: types.Message):  # this simple write  types.Message as message
#     # chat_id_types = types.Message.chat.id #var with types.Message
#     # FOR send message user  u need id
#     chat_id = message.chat.id  # var another
#
#     text_welcome = "Привет я Бот, который поможет тебе с выбором книги!"
#     sti_welcome = 'static/AnimatedSticker.tgs'
#     try:
#         with open(sti_welcome, "rb") as sticker_file:
#             await sendSticker(chat_id, sticker_file)
#     except exceptions.TelegramAPIError as e:
#         print(f"Ошибка отправки стикера: {e}")
#
#
#     # await используется для ожидания результата выполнения асинхронной операции.
#     # Когда программа доходит до строки с await, она приостанавливает выполнение текущей функции и
#     # переключается на выполнение других задач до тех пор, пока результат не будет доступен. После того,
#     # как результат будет доступен, выполнение функции продолжится дальше.
#     await  sendText(chat_id, text_welcome)
#
#     print(message.from_user.id) # print id user
#
# executor.start_polling(dp)
