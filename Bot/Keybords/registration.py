from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

registration_kb = InlineKeyboardMarkup(
    inline_keyboard=[

#         [InlineKeyboardButton(text="Авторизация",callback_data="Authorisation")],
         [InlineKeyboardButton(text="Регистрация нового покупателя",callback_data="Registration")],
         [InlineKeyboardButton(text="На главную",callback_data="back_to_start")]
        
    ]
)

