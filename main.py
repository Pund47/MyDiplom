import logging

from aiogram.utils import executor
from Create_Bot import dp,Bot

logging.basicConfig(level=logging.INFO)
#Импорты хэндлеров!
from Bot.Hadlers import welcome

#Запуск хендлеров!
welcome.register_handlers_welcome(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
