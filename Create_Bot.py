import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Bot.settings.config_bot import *

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

def create_base():
    asyncio.run(create_tables())