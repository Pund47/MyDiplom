import logging

from aiogram.utils import executor
from Create_Bot import dp,Bot

logging.basicConfig(level=logging.INFO)
#Импорты хэндлеров!
from Bot.Hadlers import welcome,basket,registration,catalog

#Запуск хендлеров!
welcome.register_handlers_welcome(dp)
basket.register_handlers_basket(dp)
registration.register_handlers_reistration(dp)
catalog.register_handlers_catalog(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
