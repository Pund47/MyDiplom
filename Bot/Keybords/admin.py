from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Покупатели", callback_data="Users")],
        [InlineKeyboardButton(text="Продукция", callback_data="Products")],
        [InlineKeyboardButton(text="Покупатели", callback_data="Stat")]
    ]
)
