#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot.Models.products import *

#Нужно утроить перебор данных из Database для формирования Кнопок
# Варианты отображения каталога?


#Product.find_by(**data)




common_catalog = InlineKeyboardMarkup(
    inline_keyboard=[

         [InlineKeyboardButton(text="Креветки",callback_data="Shrims")],
         [InlineKeyboardButton(text="Молюски",callback_data="shellfish")],
         [InlineKeyboardButton(text="Рыба",callback_data="fish")],
         [InlineKeyboardButton(text="Икра",callback_data="caviar")]

    ]
)

#################################################################################################################
list_prod = []
list_prod = Product.find_by("shellfish")
shellfish_kb = InlineKeyboardMarkup(row_width=3)
for prod in list_prod:
   shellfish_kb.insert(InlineKeyboardButton(text=f"{prod.name} , цена: {prod.price} {prod.img}" , callback_data=prod.id))

#################################################################################################################

list_shrims = Product.find_by("Shrims")

shrims_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton() ]
    ]
)
#################################################################################################################







#catalog_kb = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#         [InlineKeyboardButton(text="Креветки",callback_data="Shrims")]
#        ]
#    ]
#)