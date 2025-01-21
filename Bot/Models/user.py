import sqlalchemy
from sqlalchemy import Column

from Bot.settings.config_bot import Base


class User(Base):
    __tablename__ = 'users'
    user_id  = Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    username = Column(sqlalchemy.Text)
    age      = Column(sqlalchemy.INTEGER)
    password = Column(sqlalchemy.INTEGER, nullable=False)