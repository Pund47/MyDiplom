from  Bot.Keybords.registration import *
from aiogram import types, Dispatcher

async def start_registration(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=registration_kb)

#Подключение к базе на проверку пользователя!
async def Autorisation(call):
    await call.message.answer()
    await call.answer()

#Подключение к базе на Добавление нового пользователя!
async def Registration_new_user(call):
    pass




def register_handlers_registration(dp:Dispatcher):
    dp.register_message_handler(Autorisation, text="Authorisation")
    dp.register_message_handler(Registration_new_user, text="Registration")
