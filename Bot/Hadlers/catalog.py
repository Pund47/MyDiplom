from aiogram import types, Dispatcher
from Create_Bot import dp
from  Bot.Keybords.catalog import  *


#@dp.message_handler(text="")
async def prod (message):
     with open ('Images/креветка.jpg',"rb") as img:
        await message.answer_photo (img,"Текст Описания", reply_markup= catalog_kb)





def register_handlers_catalog(dp:Dispatcher):
    dp.register_message_handler(oformit_zakaz,commands=["Оформить заказ"])
    dp.register_message_handler(del_position, text="Удалить позицию")
    dp.register_message_handler(add_position, text="Добавить")
    dp.register_message_handler(back_on_head,text="На главную")