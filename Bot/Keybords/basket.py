from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оформить заказ"),
            KeyboardButton(text="Удалить позицию"),
            KeyboardButton(text="Добавить"),
            KeyboardButton(text="На главную")
        ]
    ],resize_keyboard=True
)