import sqlalchemy
from sqlalchemy import Column, Integer, String

from Bot.settings.config_bot import Base


class Product(Base):
    __tablename__ = 'products'
    name = Column(sqlalchemy.Text)
    id = Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    price = Column(sqlalchemy.INTEGER)
    img = Column(sqlalchemy.String)

#Base.metadata.create_all(bind=engine)