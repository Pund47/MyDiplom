from aiogram import types, Dispatcher
from Create_Bot import dp
from  Bot.Keybords.catalog import  *



async def prod (call):
     with open ('Bot/Images/креветка.jpg',"rb") as img:
        await call.message.answer_photo (img,f"Красотища")
        await call.answer()
#async def start_registration(message):
#    await message.answer(f"Welcome, {message.from_user.username}",reply_markup= registration_kb)
#await call.message.answer(f"Welcome",reply_markup=start_kb)
#    await call.answer()


def register_handlers_catalog(dp:Dispatcher):
   dp.register_callback_query_handler(prod,text="Shrims")
   #dp.register_message_handler(del_position, text="Удалить позицию")
   #dp.register_message_handler(add_position, text="Добавить")
   #dp.register_message_handler(back_on_head,text="На главную")