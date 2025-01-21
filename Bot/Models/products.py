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

#Base.metadata.create_all(bind=engine)