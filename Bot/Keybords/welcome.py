from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
         [InlineKeyboardButton(text="О нас",callback_data="info")],
         [InlineKeyboardButton(text="Регистрация",callback_data="info")],
         [InlineKeyboardButton(text="Авторизация",callback_data="info")],
         [InlineKeyboardButton(text="Каталог",callback_data="info")]
        ]
    ]
)









