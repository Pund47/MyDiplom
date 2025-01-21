from  Bot.Keybords.registration import *


async def start_registration(message):
    await message.answer(f"Welcome, {message.from_user.username}",reply_markup=registration_kb)


async def reistration(call):
    await call.message.answer()
    await call.answer()