from  aiogram import  types
# использоваться для установки команд для вашего бота.
async  def set_default_commands(dp):
    await  dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить Бота"),  # описание команд
        types.BotCommand("help", "Помощь")  # описание команд
    ])