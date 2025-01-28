import sqlalchemy
from sqlalchemy import Column, select, func

from Bot.settings.config_bot import Base, async_session


class Baskets(Base):
    __tablename__ = 'basket'
    basket_id  = Column(sqlalchemy.INTEGER,primary_key=True)
    user_id    = Column(sqlalchemy.ForeignKey('users.user_id'))
    product_id = Column(sqlalchemy.ForeignKey('products.id'))
    quantity   = Column(sqlalchemy.INTEGER)

    def __init__(self,basket_id,user_id,product_id,quantity):
        self.basket_id  = basket_id
        self.user_id    = user_id
        self.product_id = product_id
        self.quantity   = quantity

    @classmethod
    async def full_list_basket(cls):
        async with async_session() as session:
            full_list_basket = await session.execute(select(cls))
            full_list_basket = full_list_basket.scalars().all()
            return full_list_basket

    @classmethod
    async def find_by_id_basket(cls, basket_id):
        async with async_session() as session:
            existing_basket = await session.execute(select(cls).where(cls.user_id == basket_id))
            existing_basket = existing_basket.scalars().all()
            if len(existing_basket) != 0:
                await session.commit()
                return existing_basket
            else:
                await session.commit()
                return None

    @classmethod
    async def dell_by_id_basket(cls, basket_id):
        async with async_session() as session:
            result = await session.execute(select(cls).where(cls.basket_id == basket_id))
            existing_basket_id = result.scalars().first()  # Получаем первого пользователя, если он существует

            if existing_basket_id:
                await session.delete(existing_basket_id)  # Удаляем пользователя
                await session.commit()  # Подтверждаем изменения
                return True  # Возвращаем результат успешного удаления
            else:
                print("basket_id not found")  # Обработка случая, когда пользователь не найден
                return False  # Возвращаем результат, если пользователь не найден

    @classmethod
    async def create(cls, user_id, product_id, quantity):  # Добавлен параметр id
        async with async_session() as session:
            id = 0
            max_id = await session.execute(select(func.max(cls.basket_id)))
            max_id = max_id.scalars().first() or 0  # Обработка случая, когда max_id может быть None
            new_prod = cls(basket_id=max_id + 1, user_id=user_id, product_id=product_id, quantity=quantity)
            session.add(new_prod)
            await session.commit()
            return True