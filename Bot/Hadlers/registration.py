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
async def Registration_new_user(call):
    #серия вопросов - ответов!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!не пошло....
    await call.message.answer("Введите имя:")
    await call.answer()
    await User.username

async def registration_new_user_password(message,state):
    await state.update_data(username = message.text)
    data = await state.get_data()
    await message.answer(f"Введите пароль:")
    await User.password

async def registration_new_user_age(message,state):
    await state.update_data(password=message.text)
    data = await state.get_data()
    await message.answer(f"Введите ваш возраст:")
    await User.age

async def create_new_user(message,data,state):
    await User.create(username= data.username,age= data.age,password= data.password) #user_id =user_id,
    await state.finish()


def register_handlers_registration(dp:Dispatcher):
    dp.register_callback_query_handler(Autorisation, text='Authorisation')
    dp.register_callback_query_handler(Registration_new_user, text='Registration')
    dp.register_callback_query_handler(registration_new_user_password,state= User.username)
    dp.register_callback_query_handler(registration_new_user_age, state= User.password)
    dp.register_callback_query_handler(create_new_user, state= User.age)

