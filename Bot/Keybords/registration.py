from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

registration_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
         [InlineKeyboardButton(text="Авторизация",callback_data="Autorisation")],
         [InlineKeyboardButton(text="Регистрация нового покупателя",callback_data="Registration")]
        ]
    ]
)

