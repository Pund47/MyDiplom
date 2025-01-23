import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import foreign

from Bot.settings.config_bot import Base


class Product(Base):
    __tablename__ = 'products'
    name      = Column(sqlalchemy.Text)
    id        = Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    price     = Column(sqlalchemy.INTEGER)
    img       = Column(sqlalchemy.String)
    basket_id = Column(sqlalchemy.INTEGER,ForeignKey("basket_id"))
    category  = Column(sqlalchemy.String)

    def __init__(self,name,id,price,img,basket_id,category):
        self.name      = name
        self.id        = id
        self.price     = price
        self.img       = img
        self.basket_id = basket_id
        self.category = category
#Base.metadata.create_all(bind=engine)