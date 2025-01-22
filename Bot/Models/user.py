import sqlalchemy
from sqlalchemy import Column, select

from Bot.settings.config_bot import Base, async_session


class User(Base):
    __tablename__ = 'users'
    user_id  = Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    username = Column(sqlalchemy.Text)
    age      = Column(sqlalchemy.INTEGER)
    password = Column(sqlalchemy.INTEGER, nullable=False)


    def __init__(self,username,password,age):
        self.password = password
        self.username = username
        self.age      = age

    @classmethod
    async def create (cls,user_id,username,age,password):
        async with async_session() as session:
            existing_user = await session.execute(select(cls).where(cls.user_id == user_id))
            #existing_user = existing_user.scalars()
            if len(existing_user) != 0:
                return existing_user
            new_user = cls(user_id = user_id,password = password,username = username,age=age )
            session.add(new_user)
            await session.commit()
            return new_user

