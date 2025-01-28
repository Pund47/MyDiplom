#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Нужно утроить перебор данных из Database для формирования Кнопок
# Варианты отображения каталога?


#Product.find_by(**data)




common_catalog = InlineKeyboardMarkup(
    inline_keyboard=[

         [InlineKeyboardButton(text="Креветки",callback_data="prod_shrimps")],
         [InlineKeyboardButton(text="Молюски",callback_data="prod_shellfish")],
         [InlineKeyboardButton(text="Рыба",callback_data="prod_fish")],
         [InlineKeyboardButton(text="Икра",callback_data="prod_caviar")],
         [InlineKeyboardButton(text="Назад",callback_data="back")]
        # [InlineKeyboardButton(text="Доавить Новую", callback_data="new_prod")]

    ]
)

#################################################################################################################
#list_prod = []
#list_prod = Product.find_by("shellfish")
#shellfish_kb = InlineKeyboardMarkup(row_width=5)
#for prod in list_prod:
#   shellfish_kb.insert(InlineKeyboardButton(text=f"{prod.name} , цена: {prod.price} {prod.img}" , callback_data=prod.id))

#################################################################################################################

#list_Shrimps = Product.find_by("Shrimps")
#shrimps_kb = InlineKeyboardMarkup(row_width=5)
#for shrimps in list_Shrimps:
#    shrimps_kb.insert(InlineKeyboardButton(text=f"{shrimps.name} , цена: {shrimps.price} {shrimps.img}", callback_data=shrimps.id))


#shrims_kb = InlineKeyboardMarkup(
#        inline_keyboard=[
#            [InlineKeyboardButton(text=f"{shrims.name} , цена: {shrims.price} {shrims.img}" , callback_data=shrims.id) ]
#    ]
#)
#################################################################################################################







#catalog_kb = InlineKeyboardMarkup(
#    inline_keyboard=[
#        [
#         [InlineKeyboardButton(text="Креветки",callback_data="Shrims")]
#        ]
#    ]
#)