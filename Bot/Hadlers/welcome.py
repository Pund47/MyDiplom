#from main import dp
from  Bot.Keybords.welcome import  *

#@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=start_kb)