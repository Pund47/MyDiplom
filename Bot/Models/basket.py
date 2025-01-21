import sqlalchemy
from sqlalchemy import Column

from Bot.settings.config_bot import Base


class Baskets(Base):
    __tablename__ = 'basket'
    basket_id  = Column(sqlalchemy.INTEGER)
    user_id    = Column(sqlalchemy.ForeignKey('users.user_id'))
    product_id = Column(sqlalchemy.ForeignKey('products.id'))
    quantity   = Column(sqlalchemy.INTEGER)
