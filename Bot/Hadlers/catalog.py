from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove

from Bot.Keybords.welcome import start_kb
from Bot.Models.products import Product
from Bot.Models.basket import Baskets
from Bot import *


async def back_to_start(call: types.CallbackQuery):
    """Handler to return to the start menu."""
    await call.message.answer("Welcome", reply_markup=start_kb)
    await call.answer()


async def display_products(call: types.CallbackQuery, state: FSMContext):
    try:
        # Пытаемся удалить предыдущие сообщения
        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
    except Exception as e:
        # Если кнопка уже удалены, то продолжаем выполнение кода
        pass
    """Display products based on the selected category."""
    try:
        # Extract category from callback data
        category = call.data.split("prod_")[1]
        products = await Product.find_by(category)

        # Get pagination data from state
        data = await state.get_data()
        current_limit = data.get("current_limit", 0)
        limit = data.get("limit", 2)
        message_ids = data.get("message_ids", [])

        # Display products within the current limit
        for product in products[current_limit:current_limit + limit]:
            product_kb = InlineKeyboardMarkup(row_width=2)
            product_kb.add(
                InlineKeyboardButton(text="Добавить в корзину", callback_data=f"add_{product.id}"),
                InlineKeyboardButton(text="Далее", callback_data=f"next_page_{category}")
            )

            # Send product photo and details
            with open('Bot/Images/креветка.jpg',  "rb") as img:
                message = await call.message.answer_photo(
                    img,
                    caption=f"{product.name}, цена: {product.price}",
                    reply_markup=product_kb
                )
                message_ids.append(message.message_id)

        # Update state with new pagination data
        await state.update_data({
            "message_ids": message_ids,
            "current_limit": current_limit + limit,
            "category": category
        })

    except Exception as e:
        await call.message.answer(f"Произошла ошибка: {e}")


async def next_page(call: types.CallbackQuery, state: FSMContext):
    #await call.message.reply("text",reply_markup=ReplyKeyboardRemove())  ###################################################################
    """Handler for pagination (next page)."""
    try:
        # Extract category from callback data
        category = call.data.split("_")[-1]
        products = await Product.find_by(category)

        try:
            # Пытаемся удалить предыдущие сообщения
            await call.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id - 1)
        except Exception as e:
            # Если кнопка уже удалены, то продолжаем выполнение кода
            pass





        # Get pagination data from state
        data = await state.get_data()
        current_limit = data.get("current_limit", 0)
        limit = data.get("limit", 2)
        #message_ids = data.get("message_ids", [])

        # Display next set of products
        for product in products[current_limit:current_limit + limit]:
            product_kb = InlineKeyboardMarkup(row_width=2,resize_keyboard=True, one_time_keyboard=True)
            product_kb.add(
                InlineKeyboardButton(text="Добавить в корзину", callback_data=f"add_{product.id}"),
                InlineKeyboardButton(text="Далее", callback_data=f"next_page_{category}")
            )

            with open('Bot/Images/креветка.jpg', "rb") as img:
                message = await call.message.answer_photo(
                    img,
                    caption=f"{product.name}, цена: {product.price}",
                    reply_markup=product_kb
                )
                #message_ids.append(message.message_id)

        # Update state with new pagination data
        await state.update_data({
            #"message_ids": message_ids,
            "current_limit": current_limit + limit
        })

    except Exception as e:
        await call.message.answer(f"Произошла ошибка: {e}")


async def add_to_basket(call: types.CallbackQuery, state: FSMContext):
    try:
        # Пытаемся удалить предыдущие сообщения
        await call.bot.delete_message(chat_id=call.message.chat.id, message_id=[call.message.message_id - 1,call.message.message_id - 2])
    except Exception as e:
        # Если кнопка уже удалены, то продолжаем выполнение кода
        pass


    """Handler to add a product to the basket."""
    try:
        product_id = call.data.split("_")[1]
        await state.update_data(product_id=product_id)
        await call.message.answer("Введите количество:")
        await state.set_state("add_to_basket")
    except Exception as e:
        await call.message.answer(f"Произошла ошибка: {e}")


async def find_and_add(message: types.Message, state: FSMContext):
    """Handler to process the quantity and add the product to the basket."""
    try:
        # Update state with user input and user ID
        await state.update_data(quantity=message.text, user_id=message.from_user.id)
        data = await state.get_data()

        # Create a new basket entry
        result_mod_prod = await Baskets.create(
            user_id=data['user_id'],
            product_id=data['product_id'],
            quantity=data['quantity']
        )

        # Notify the user about successful addition
        await message.answer(f"Товары добавлены в корзину успешно: {result_mod_prod}")

        # Prepare inline keyboard for further actions
        category = data.get('category')
        kb_zak = InlineKeyboardMarkup(row_width=2,resize_keyboard=True, one_time_keyboard=True)
        kb_zak.add(
            InlineKeyboardButton(text="Оформить заказ", callback_data="оформить"),
                  InlineKeyboardButton(text="Далее", callback_data=f"next_page_{category}")
        )

        # Ask the user if they want to continue
        await message.answer("Продолжаем?", reply_markup=kb_zak)
        await state.reset_state()

    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


async def oformit_zakaz(message: types.Message, state: FSMContext):
   # await message.reply("Второе - прячем клавиатуру после одного нажатия", reply_markup=kb_zak.greet_kb2)
    """Handler to place an order."""
    try:
        # Fetch all products in the user's basket
        zakaz = await Baskets.find_by_user_id_basket(user_id=message.from_user.id)
        print(message.from_user.id)
        # Display each product in the basket
        for prod in zakaz:
            print(prod)
            await message.answer(f"{prod.user_id}, цена: {prod.basket_id}, количество: {prod.product_id}")

        # Notify the user about successful order placement
        await message.answer("Поздравляем, заказ успешно оформлен.")

    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")


async def handle_oformlenie(callback_query: types.CallbackQuery, state: FSMContext):
    """Callback handler for 'Оформить заказ'."""
    try:
        # Acknowledge the callback query
        await callback_query.answer()

        # Debug message to confirm the handler is triggered
        #print("Оформить заказ button clicked!")

        # Call the order placement function
        await oformit_zakaz(callback_query.message, state)
    except Exception as e:
        await callback_query.message.answer(f"Произошла ошибка: {e}")

async def log_all_callbacks(callback_query: types.CallbackQuery):
    print(f"Received callback data: {callback_query.data}")
    await callback_query.answer()  # Acknowledge the callback




def register_handlers_catalog(dp: Dispatcher):


    dp.register_callback_query_handler(display_products, Text(startswith="prod_"))
    dp.register_callback_query_handler(back_to_start, text="back")
    dp.register_callback_query_handler(next_page, Text(startswith="next_page"))
    dp.register_callback_query_handler(add_to_basket, Text(startswith="add_"))
    dp.register_message_handler(find_and_add, state="add_to_basket")
    dp.register_callback_query_handler(handle_oformlenie, text="оформить")  # Specific handler
    # dp.register_callback_query_handler(log_all_callbacks)