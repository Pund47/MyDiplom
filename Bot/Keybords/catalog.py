from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot.Models.products import *
#Нужно утроить перебор данных из Database для формирования Кнопок
# Варианты отображения каталога?
list_prod = []

#Product.find_by(**data)


catalog_kb = InlineKeyboardMarkup(row_width=3)
for prod in list_prod:
   catalog_kb.insert(InlineKeyboardButton(text=text, callback_data=data))

common_catalog = InlineKeyboardMarkup(
    inline_keyboard=[

         [InlineKeyboardButton(text="Креветки",callback_data="Shrims")],
         [InlineKeyboardButton(text="Молюски",callback_data="shellfish")],
         [InlineKeyboardButton(text="Рыба",callback_data="fish")],
         [InlineKeyboardButton(text="Икра",callback_data="caviar")]

    ]
)

#await call.message.answer("Случайный порядок в три ряда?", reply_markup=markup)






#catalog_kb = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#         [InlineKeyboardButton(text="Креветки",callback_data="Shrims")]
#        ]
#    ]
#)