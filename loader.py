# файл loaders используется для инициализации экземпляров классов Bot и Dispatcher и сохранения их в
# переменных bot и dp соответственно. Это позволяет в дальнейшем удобно использовать их в других модулях проекта.
#
# Также в файле loaders может выполняться загрузка других настроек проекта, например, подключение
# к базе данных, установка настроек логирования и т.д.

from aiogram import Bot, Dispatcher, types, exceptions
from  data import  config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# Получите объект dp - Dispatcher:
dp = Dispatcher(bot)
