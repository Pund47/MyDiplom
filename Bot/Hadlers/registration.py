from main import dp
from  Bot.Keybords.catalog import  *



@dp.callback_query_handler(text="")
async def reistration(call):
    await call.message.answer()
    await call.answer()