import logging
import asyncio

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from Bot.settings.config_bot import *
#from Bot.Hadlers.registration import *
#from Bot.Keybords.registration import *
#from Bot.Keybords.welcome import *
from Bot.Hadlers.welcome import *
from Bot.Hadlers.registration import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())
#dp.include_router()
dp.register_message_handler(start,)
dp.register_inline_handler(start_registration,)


def create_base():
    asyncio.run(create_tables())




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
