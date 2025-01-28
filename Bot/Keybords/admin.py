from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Покупатели", callback_data="Users")],
        [InlineKeyboardButton(text="Продукция", callback_data="Products")],
        [InlineKeyboardButton(text="Корзины", callback_data="Baskets")]
    ]
)

admin_panel_users = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Вывести список зарегистрированных", callback_data="Users_list")],
        [InlineKeyboardButton(text="Добавить нового", callback_data="add_new_user")],
        [InlineKeyboardButton(text="Изменить по id", callback_data="change_by_id_user")],
        [InlineKeyboardButton(text="Удалить по id", callback_data="dell_by_id")]
    ]
)

admin_panel_basket = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Вывести список", callback_data="basket_list")],
        [InlineKeyboardButton(text="Добавить новую", callback_data="add_new_basket")],
        [InlineKeyboardButton(text="Удалить по id", callback_data="dell_by_id_basket")]
    ]
)

admin_panel_products = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Вывести список", callback_data="product_list")],
        [InlineKeyboardButton(text="Добавить новую позицию", callback_data="add_new_product")],
        [InlineKeyboardButton(text="Изменить позицию по id", callback_data="change_product")],
        [InlineKeyboardButton(text="Удалить по id", callback_data="dell_by_id_product")]
    ]
)