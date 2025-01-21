import sqlalchemy
from sqlalchemy import Column

from Bot.settings.config_bot import Base


class User(Base):
    __tablename__ = 'users'
    username = Column(sqlalchemy.Text)
    user_id  = Column(sqlalchemy.INTEGER, primary_key =True, autoincrement =True)
    age      = Column(sqlalchemy.INTEGER)
