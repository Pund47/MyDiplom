from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#Нужно утроить перебор данных из Database для формирования Кнопок


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
         [InlineKeyboardButton(text="Креветки",callback_data="Shrims")]
        ]
    ]
)