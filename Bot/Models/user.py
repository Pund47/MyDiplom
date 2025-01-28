import sqlalchemy
from sqlalchemy import Column, select, false

from Bot.settings.config_bot import Base, async_session


class User(Base):
    __tablename__ = 'users'
    user_id  = Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    username = Column(sqlalchemy.Text)
    age      = Column(sqlalchemy.INTEGER)
    password = Column(sqlalchemy.INTEGER, nullable=False)
    status_admin = Column(sqlalchemy.Boolean, default=False)
    status_block = Column(sqlalchemy.Boolean, default=False)


    def __init__(self,username,password,age,user_id):
        self.password = password
        self.username = username
        self.age      = age
        self.user_id  = user_id

    @classmethod
    async def create (cls,user_id,username,age,password):
        async with async_session() as session:
            existing_user = await session.execute(select(cls).where(cls.user_id == user_id))
            existing_user = existing_user.scalars().all()
            if len(existing_user) != 0:
                return existing_user
            new_user = cls(user_id = user_id,username= username, age= age,password = password)
            session.add(new_user)
            await session.commit()
            return new_user

    @classmethod
    async def find_by_id(cls, user_id):
        async with async_session() as session:
            existing_user = await session.execute(select(cls).where(cls.user_id == user_id))
            existing_user = existing_user.scalars().all()
            if len(existing_user) != 0:
                await session.commit()
                return existing_user
            else:
                await session.commit()
                return None

    @classmethod
    async def full_list(cls):
        async with async_session() as session:
            full_list_user = await session.execute(select(cls))
            full_list_user = full_list_user.scalars().all()
            return full_list_user

    @classmethod
    async def dell_by_id(cls, user_id):
        async with async_session() as session:
            result = await session.execute(select(cls).where(cls.user_id == user_id))
            existing_user = result.scalars().first()  # Получаем первого пользователя, если он существует

            if existing_user:
                await session.delete(existing_user)  # Удаляем пользователя
                await session.commit()  # Подтверждаем изменения
                return True  # Возвращаем результат успешного удаления
            else:
                print("User not found")  # Обработка случая, когда пользователь не найден
                return False  # Возвращаем результат, если пользователь не найден






