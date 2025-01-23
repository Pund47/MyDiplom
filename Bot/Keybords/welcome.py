from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[

         [InlineKeyboardButton(text="О нас",callback_data="О нас")],
         [InlineKeyboardButton(text="Регистрация",callback_data="Регистрация")],
         [InlineKeyboardButton(text="Авторизация",callback_data="Авторизация")],
         [InlineKeyboardButton(text="Каталог",callback_data="Каталог")]


    ]
)

#start_kb = ReplyKeyboardMarkup(
#    keyboard=[
#        [
#            KeyboardButton(text="О нас"),
#            KeyboardButton(text="Регистрация"),
#            KeyboardButton(text="Авторизация"),
#            KeyboardButton(text="Каталог")
#        ]
#    ],resize_keyboard=True
#)








