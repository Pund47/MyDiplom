from aiogram import types, Dispatcher
from Create_Bot import dp
from  Bot.Keybords.welcome import  *
from  Bot.Keybords.registration import *
from  Bot.Keybords.catalog import *

#@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=start_kb)

#@dp.message_handler(text="О нас")
async def about_us(message):
    await message.answer("Какой-то текст о нас....")

async def start_regstration(call):
    await call.message.answer("1111", reply_markup=registration_kb)

async def run_to_catalog(message):
    await message.answer("Добро пожаловать в каталог",reply_markup= catalog_kb)




def register_handlers_welcome(dp:Dispatcher):
    dp.register_message_handler(start,commands=["start"])
    dp.register_callback_query_handler(start_regstration, text="Регистрация")
    dp.register_callback_query_handler(about_us,text="О нас")
    dp.register_callback_query_handler(run_to_catalog,text = "Каталог")