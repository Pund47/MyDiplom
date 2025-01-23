import sqlalchemy
from sqlalchemy import Column

from Bot.settings.config_bot import Base


class Baskets(Base):
    __tablename__ = 'basket'
    basket_id  = Column(sqlalchemy.INTEGER)
    user_id    = Column(sqlalchemy.ForeignKey('users.user_id'))
    product_id = Column(sqlalchemy.ForeignKey('products.id'))
    quantity   = Column(sqlalchemy.INTEGER)

    def __init__(self,basket_id,user_id,product_id,quantity):
        self.basket_id  = basket_id
        self.user_id    = user_id
        self.product_id = product_id
        self.quantity   = quantity