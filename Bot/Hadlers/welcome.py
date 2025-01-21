from  Bot.Keybords.welcome import  *


async def start(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=start_kb)