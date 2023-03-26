# тип админки
import logging

from aiogram import Dispatcher
from data.config import admins


async def on_startup_notify(dp: Dispatcher):
    for admin in admins:
        try:
            text = "Hi Admins, i'm started and ready for work"
            await dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
