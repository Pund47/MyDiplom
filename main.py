import asyncio
import logging

from aiogram.utils import executor

from Bot.settings.config_bot import create_tables
from Create_Bot import dp,Bot

logging.basicConfig(level=logging.INFO)
logging.root.setLevel(logging.WARNING)

# Создание обработчика для основного лога
file_handler = logging.FileHandler("logs.log", encoding="utf-8")






#Импорты хэндлеров!
from Bot.Hadlers import welcome,basket,registration,catalog

#Запуск хендлеров!
welcome.register_handlers_welcome(dp)
basket.register_handlers_basket(dp)
registration.register_handlers_registration(dp)
#catalog.register_handlers_catalog(dp)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_tables())

    #asyncio.run(create_tables())
    executor.start_polling(dp, skip_updates=True,loop=loop)

