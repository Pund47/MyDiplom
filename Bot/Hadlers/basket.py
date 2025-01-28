from aiogram import Dispatcher
from  Bot.Keybords.basket import  *
from  Bot.Keybords.welcome import *

async def oformit_zakaz(message):
    await message.answer(f"Дорогой покупатель, {message.from_user.username}, заказ успешно оформлен  ")

async def del_position(message):
#Обращение к базе (корзина) удаление выбранной позиции
    await message.answer(f"Дорогой покупатель, {message.from_user.username}, позиция успешно удалена  ")

async def add_position(message):
    # Обращение к базе (корзина) добавление позиции  или открытие каталога!
    await message.answer(f"Дорогой покупатель, {message.from_user.username}, позиция успешно добавлена  ")

async def back_on_head(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=start_kb)



def register_handlers_basket(dp:Dispatcher):
    dp.register_message_handler(oformit_zakaz,commands=["Оформить заказ"])
    dp.register_message_handler(del_position, text="Удалить позицию")
    dp.register_message_handler(add_position, text="Добавить")
    dp.register_message_handler(back_on_head,text="На главную")