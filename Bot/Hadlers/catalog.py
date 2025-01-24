from aiogram import types, Dispatcher
from Create_Bot import dp
from  Bot.Keybords.catalog import  *
from  Bot.Keybords.welcome import *

async def back_to_start(call):
    await call.message.answer(f"Welcome",reply_markup=start_kb)
    await call.answer()


async def prod (call):
     with open ('Bot/Images/креветка.jpg',"rb") as img:
        await call.message.answer_photo (img,f"Красотища")
        await call.answer()
#Добавить вывод списка по 5 наименований с картинками?






def register_handlers_catalog(dp:Dispatcher):
   dp.register_callback_query_handler(prod,text="Shrimps")
   dp.register_callback_query_handler(back_to_start, text="back")
   #dp.register_message_handler(del_position, text="Удалить позицию")
   #dp.register_message_handler(add_position, text="Добавить")
   #dp.register_message_handler(back_on_head,text="На главную")