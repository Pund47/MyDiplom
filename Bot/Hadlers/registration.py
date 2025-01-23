from  Bot.Keybords.registration import *
from  Bot.Keybords.welcome import *

from aiogram import Dispatcher


from Bot.Models.user import User


async def start_registration(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=registration_kb)

#Подключение к базе на проверку пользователя!
async def autorisation_1(call):
    await call.message.answer()          #!!!!!!
    await call.answer()

#Подключение к базе на Добавление нового пользователя!
async def registration_new_user(call,state):
    await call.message.answer("Введите имя:")
    await state.set_state("user_name")
    await call.answer()

async def registration_new_user_password(message,state):
    await state.update_data(username = message.text)
#    data = await state.get_data()
    await message.answer(f"Введите пароль:")
    await state.set_state("set_password")

async def registration_new_user_age(message,state):
    await state.update_data(password=message.text)
#    data = await state.get_data()
    await message.answer(f"Введите ваш возраст:")
    await state.set_state("set_age")

async def create_new_user(message,state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await User.create(user_id= message.from_user.id,**data)
    await state.finish()

async def back_to_start(call):
    await call.message.answer(f"Welcome",reply_markup=start_kb)
    await call.answer()



def register_handlers_registration(dp:Dispatcher):
    dp.register_callback_query_handler(autorisation_1, text='Authorisation')
    dp.register_callback_query_handler(registration_new_user, text='Registration')
    dp.register_callback_query_handler(back_to_start, text="back_to_start")
    dp.register_message_handler(registration_new_user_password,state= "user_name")
    dp.register_message_handler(registration_new_user_age, state= "set_password")
    dp.register_message_handler(create_new_user, state= "set_age")



