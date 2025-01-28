from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from  Bot.Keybords.welcome import *
from Bot.Models.products import *
from Bot.Models.basket import *
async def back_to_start(call):
    await call.message.answer(f"Welcome",reply_markup=start_kb)
    await call.answer()


async def prod (call,state):

     list_prod = []
     categor = call.data.split("prod_")[1]
     list_prod = await Product.find_by(categor)
    #

     data = await state.get_data()
     current_limit = 0
     limit = data.get("limit", 2)
     current_limit = data.get("current_limit",0)
     message_ids = data.get("message_ids",[])

     for prod in list_prod[current_limit: limit]:
        fk_prod = InlineKeyboardMarkup()
        fk_prod.add(InlineKeyboardButton(text="Добавить в корзину", callback_data=f"add_{prod.id}"), )
        fk_prod.add(InlineKeyboardButton(text="Далее", callback_data=f"next_page_{categor}"), )
            

        with open('Bot/Images/креветка.jpg', "rb") as img:
           await call.message.answer_photo(img, f"{prod.name} , цена: {prod.price} {prod.img}",reply_markup=fk_prod)

           message_ids.append(call.message.message_id)

     await state.update_data({"message_ids":message_ids, "current_limit":current_limit+2, "limit":limit+2, "categor":categor})
async def next_page (call,state):
    data = await state.get_data()
    print(data.get("message_ids"))
    print(data.get("chat_ids"))
    print(call.message.chat.id)
#   for ids in data.get("message_ids"):
#        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=ids)

    message_ids = []
    list_prod = []
    categor = call.data.split("_")[-1]
    list_prod = await Product.find_by(categor)
    limit = data.get("limit", 2)
    current_limit = data.get("current_limit", 0)
    print(current_limit,limit)
    for prod in list_prod[current_limit: limit]:
        fk_prod = InlineKeyboardMarkup()
        fk_prod.add(InlineKeyboardButton(text="Добавить в корзину", callback_data=f"add_{prod.id}"), )
        fk_prod.add(InlineKeyboardButton(text="Далее", callback_data=f"next_page_{categor}"), )
        with open('Bot/Images/креветка.jpg', "rb") as img:
            await call.message.answer_photo(img, f"{prod.name} , цена: {prod.price} {prod.img}", reply_markup=fk_prod)
            message_ids.append(call.message.message_id)
    await state.update_data({"message_ids": message_ids, "current_limit": current_limit + 2, "limit": limit})

async def add_to_basket(call,state):
    product_id = call.data.split("_")[1]
    await state.update_data(product_id=product_id)
    await call.message.answer(f"Введите количество:")
    await state.set_state("add_to_basket")

async def find_and_add(message, state):
    await state.update_data(quantity = message.text)
    await state.update_data(user_id = message.from_user.id)
    data = await state.get_data()
    result_mod_prod = await Baskets.create(user_id=data.get('user_id'), product_id=data.get('product_id'), quantity=data.get('quantity'))
    await message.answer(f"Товары добавлены в корзину успешно: {result_mod_prod}")
    categor =data.get('categor')
    kb_zak = InlineKeyboardMarkup()
    kb_zak.add(InlineKeyboardButton(text="Оформить заказ", callback_data="oformlenie" ), )
    kb_zak.add(InlineKeyboardButton(text="Далее", callback_data=f"next_page_{categor}"), )
    await message.answer("Продолжаем?", reply_markup=kb_zak)

async def oformit_zakaz(call,state):
    call.message.answer(f"Поздравляем, заказ успешно оформлен.")
    pass




def register_handlers_catalog(dp:Dispatcher):

   dp.register_callback_query_handler(prod,Text(startswith="prod_") )# Фильтр по префиксу
   dp.register_callback_query_handler(back_to_start, text="back")
   dp.register_callback_query_handler(next_page, Text(startswith="next_page"))
   dp.register_callback_query_handler(back_to_start, text="back")
   dp.register_callback_query_handler(add_to_basket, Text(startswith="add_"))
   dp.register_message_handler(find_and_add, state="add_to_basket")
   dp.register_callback_query_handler(oformit_zakaz, text="oformlenie")




