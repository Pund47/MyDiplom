from  Bot.Keybords.registration import *
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State

from Bot.Models.user import User


async def start_registration(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=registration_kb)

#Подключение к базе на проверку пользователя!
async def Autorisation(call):
    await call.message.answer()          #!!!!!!
    await call.answer()

#Подключение к базе на Добавление нового пользователя!
async def Registration_new_user(message):
    #серия вопросов - ответов
    await message.answer("Введите имя:")
    await User.username.set()

async def registration_new_user_password(message,state):
    await state.update_data(username = message.text)
    date = await state.get_data()
    await message.answer(f"Введите пароль:")
    await User.password.set()

async def registration_new_user_age(message,state):
    await state.update_data(password=message.text)
    date = await state.get_data()
    await message.answer(f"Введите ваш возраст:")
    await User.age.set()

async def create_new_user(message,date,state):
    await User.create(username= date.username,age= date.age,password= date.password) #user_id =user_id,
    await state.finish()


def register_handlers_registration(dp:Dispatcher):
    dp.register_message_handler(Autorisation, text="Authorisation")
    dp.register_message_handler(Registration_new_user, text="Registration")
    dp.register_message_handler(registration_new_user_password,state= User.username)
    dp.register_message_handler(registration_new_user_age, state= User.password)
    dp.register_message_handler(create_new_user, state= User.age)

