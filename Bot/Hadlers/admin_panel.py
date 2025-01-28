from aiogram import  Dispatcher, types
from sqlalchemy.testing import startswith_
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from  Bot.Keybords.admin import  *
from Bot.Models.user import User
from Bot.Models.products import Product
from Bot.Models.basket import Baskets
from Bot.settings.config_bot import *


async def start_admin(message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(f"Welcome, {message.from_user.username}", reply_markup=admin_panel)
    else:
        await message.answer("У вас нет доступа к админ-панели.")

####################################################################################################################

async def start_admin_Users(call):
    await call.message.answer(f"Welcome", reply_markup=admin_panel_users)

async def registration_new_user(call,state):
    await call.message.answer("Введите имя:")
    await state.set_state("user_name")
    await call.answer()

async def registration_new_user_password(message,state):
    await state.update_data(username = message.text)
    await message.answer(f"Введите пароль:")
    await state.set_state("set_password")

async def registration_new_user_age(message,state):
    await state.update_data(password=message.text)
    await message.answer(f"Введите ваш возраст:")
    await state.set_state("set_age")

async def create_new_user(message,state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await User.create(user_id= message.from_user.id,**data)
    await state.finish()
    #await message.answer(f"Покупатель {User.username} успешно зарегистрирован):")
async def full_list(call):
    full_list_user = await  User.full_list()
    for user in full_list_user:
        await call.message.answer(f" Пользователь: {user.username},пароль: {user.password}, возраст: {user.age}")

async def dell_by_id(call,state):
    await call.message.answer("Введите id:")
    await state.set_state("set_id")
    await call.answer()

async def deel_from_base(message,state):
    await state.update_data(user_id=message.text)
    data = await state.get_data()
    result = await User.dell_by_id(**data)
    await message.answer(f"Успешно: {result}")

####################################################################################################################
async def start_admin_Products(call):
    await call.message.answer(f"Welcome", reply_markup=admin_panel_products)

async def full_list_prod(call):
    full_list_prod = await  Product.full_list_prod()
    for prod in full_list_prod:
        await call.message.answer(f" Продукция: {prod.name},категория: {prod.category}, цена: {prod.price}, id: {prod.id}")

async def dell_by_id_prod(call,state):
    await call.message.answer("Введите id:")
    await state.set_state("set_id_prod")
    await call.answer()

async def deel_from_base_prod(message,state):
    await state.update_data(id=message.text)
    data = await state.get_data()
    result = await Product.dell_by_id_prod(**data)
    await message.answer(f"Успешно: {result}")

async def change_by_id(call,state):
    await call.message.answer("Введите id:")
    await state.set_state("find_prod_for_change")
    await call.answer()

async def choice_to_change(message, state):
    await state.update_data(id=message.text) #Получаем по чему искать продукт на изменение.
    keyb_select_to_change = InlineKeyboardMarkup()
    for atr in list_of_atr_productions_to_make_change:
        keyb_select_to_change.add(InlineKeyboardButton(text=f"{atr}", callback_data=f"atr:{atr}"))
    await message.answer(f"Выберите что нужно изменить:", reply_markup=keyb_select_to_change)
    await state.set_state("set_atr_to_change")

async def set_new_value(call, state):
    atr_to_change = call.data.split(":")[1]
    await state.update_data(atr_tochange=atr_to_change)
    await call.message.answer(f"Введите новое значение:")
    await state.set_state("set_new_val")


async def oper_with_base (message, state):
    await state.update_data(new_val=message.text)
    data = await state.get_data()
    result_mod_prod = await Product.change_by_id_prod(**data)
    await message.answer(f"Изменения внесены успешно: {result_mod_prod}")




async def new_prod(call, state):
    await call.message.answer("Введите название:")
    await state.set_state("name_of_prod")
    await call.answer()

async def registration_new_prod_name(message, state):
    await state.update_data(name=message.text)
    await message.answer(f"Введите цену:")
    await state.set_state("set_price")

async def registration_new_prod_category(message, state):
    await state.update_data(price=message.text)
    fk_cat = InlineKeyboardMarkup()
    for cat in list_of_category:
        fk_cat.add(InlineKeyboardButton(text=f"{cat}", callback_data=f"category:{cat}"))
    await message.answer(f"Выберите категорию:", reply_markup=fk_cat)
    await state.set_state("set_category")

# Новый обработчик для нажатия кнопок категорий
async def handle_category_selection(call, state):
    category = call.data.split(":")[1]
    await state.update_data(category=category)
    await call.message.answer(f"Вы выбрали категорию: {category}. Введите количество:")
    await state.set_state("set_fin")

async def category_selected(call, state):
    category = call.data.split(":")[1]
    await state.update_data(category=category)
    await call.message.answer(f"Введите количество:")
    await state.set_state("set_fin")

async def registration_new_prod_count(message, state):
    await state.update_data(count=message.text)
    await message.answer(f"Введите фото:")
    await state.set_state("set_fin2")

async def registration_new_prod_img(message, state):
    await state.update_data(img=message.text)
    data = await state.get_data()
    result_prod = await Product.create(**data)
    await state.finish()
    await message.answer(f"Продукция: {result_prod.name} успешно добавлена")



####################################################################################################################
async def start_admin_Baskets(call):
    await call.message.answer(f"Welcome", reply_markup=admin_panel_basket)

async def full_list_baskets(call,state):
    full_list_basket = await  Baskets.full_list_basket()
    for basket in full_list_basket:
        await call.message.answer(f" Пользователь: {basket.user_id},id: {basket.basket_id}, продукция: {basket.product_id}, количество: {basket.quantity}")

async def dell_by_id_basket(call,state):
    await call.message.answer("Введите id:")
    await state.set_state("set_id_basket")
    await call.answer()

async def deel_from_base_basket(message,state):
    await state.update_data(basket_id=message.text)
    data = await state.get_data()
    result = await Baskets.dell_by_id_basket(**data)
    await message.answer(f"Успешно: {result}")
####################################################################################################################


def register_handlers_admin(dp:Dispatcher):
    dp.register_message_handler(start_admin, commands=["admin"])
    dp.register_callback_query_handler(start_admin_Users, text=["Users"])
    dp.register_callback_query_handler(start_admin_Products, text=["Products"])
    dp.register_callback_query_handler(start_admin_Baskets, text=["Baskets"])
######################################users######################################################
    dp.register_callback_query_handler(full_list, text="Users_list")
    dp.register_callback_query_handler(registration_new_user, text='add_new_user')
    dp.register_callback_query_handler(dell_by_id,text="dell_by_id")
    dp.register_message_handler(registration_new_user_password, state="user_name")
    dp.register_message_handler(registration_new_user_age, state="set_password")
    dp.register_message_handler(create_new_user, state="set_age")
    dp.register_message_handler(deel_from_base, state="set_id")
######################################users######################################################

######################################product######################################################
    dp.register_callback_query_handler(full_list_prod, text="product_list")
    dp.register_callback_query_handler(change_by_id,text="change_product")
    dp.register_callback_query_handler(dell_by_id_prod, text="dell_by_id_product")
    dp.register_message_handler(deel_from_base_prod, state="set_id_prod")
    dp.register_message_handler(choice_to_change,state="find_prod_for_change")
    dp.register_callback_query_handler(set_new_value,state="set_atr_to_change")
    dp.register_message_handler(oper_with_base,state="set_new_val")




    dp.register_callback_query_handler(new_prod, text="add_new_product")
    dp.register_message_handler(registration_new_prod_name, state="name_of_prod")
    dp.register_message_handler(registration_new_prod_category, state="set_price")
    dp.register_callback_query_handler(handle_category_selection,state="set_category")
    dp.register_message_handler(registration_new_prod_count,state="set_fin")
    dp.register_message_handler(registration_new_prod_img, state="set_fin2")

######################################product######################################################

######################################basket######################################################
    dp.register_callback_query_handler(full_list_baskets, text="basket_list")
    dp.register_callback_query_handler(dell_by_id_basket, text="dell_by_id_basket")
    dp.register_message_handler(deel_from_base_basket, state="set_id_basket")
######################################basket######################################################