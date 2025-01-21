from main import dp

from  Bot.Keybords.catalog import  *

from Bot.settings.config_bot import Base

#from Base


#@dp.message_handler(text="")
async def prod (message):
     with open ('Images/креветка.jpg',"rb") as img:
        await message.answer_photo (img,"Текст Описания", reply_markup= catalog_kb)