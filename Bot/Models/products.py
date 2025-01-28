import sqlalchemy
from sqlalchemy import Column, select, ForeignKey, func
from Bot.settings.config_bot import Base, async_session


class Product(Base):
    __tablename__ = 'products'
    name      = Column(sqlalchemy.Text)
    id        = Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    price     = Column(sqlalchemy.INTEGER)
    img       = Column(sqlalchemy.String) #BLOB
    count     = Column(sqlalchemy.INTEGER)
    category  = Column(sqlalchemy.String)

    def __init__(self,name,id,price,img,count,category):
        self.name     = name
        self.id       = id
        self.price    = price
        self.img      = img
        self.count    = count
        self.category = category


    @classmethod
    async def find_by(cls, category):
        async with async_session() as session:
            existing_prod = await session.execute(select(cls).where(cls.category == category))
            existing_prod = existing_prod.scalars().all()
            #await session.commit()
            return existing_prod

    @classmethod
    async def find_by_id(cls, id):
        async with async_session() as session:
            found_prod = await session.execute(select(cls).where(cls.id == id))
            found_prod = found_prod.scalars().all()
            await session.commit()
            return found_prod

    @classmethod
    async def create(cls, name, price, img, count, category):  # Добавлен параметр id
        async with async_session() as session:
            id = 0
            max_id = await session.execute(select(func.max(cls.id)))
            max_id = max_id.scalars().first() or 0  # Обработка случая, когда max_id может быть None
            new_prod = cls(id=max_id + 1, name=name, price=price, img=img, count=count, category=category)
            session.add(new_prod)
            await session.commit()
            return new_prod

    @classmethod
    async def dell_by_id_prod(cls, id):
        async with async_session() as session:
            result = await session.execute(select(cls).where(cls.id == id))
            existing_prod = result.scalars().first()  # Получаем первого продукцию, если она существует
           # print(id)
            if existing_prod:
                await session.delete(existing_prod)  # Удаляем продукцию
                await session.commit()  # Подтверждаем изменения
                return True  # Возвращаем результат успешного удаления
            else:
                print("Product not found")  # Обработка случая, когда продукция не найден
                return False  # Возвращаем результат, если продукция не найдена

    @classmethod
    async def full_list_prod(cls):
        async with async_session() as session:
            full_list_prod = await session.execute(select(cls))
            full_list_prod = full_list_prod.scalars().all()
            return full_list_prod

    @classmethod
    async def change_by_id_prod(cls, id, atr_tochange, new_val):
        async with async_session() as session:
            result = await session.execute(select(cls).where(cls.id == id))
            existing_prod = result.scalars().first()  # Получаем первого продукцию, если она существует
            if existing_prod:
                # Изменяем атрибут существующего продукта
                setattr(existing_prod, atr_tochange, new_val)  # Изменяем указанный атрибут
                await session.commit()  # Подтверждаем изменения
                return True  # Возвращаем результат успешного изменения
            else:
                print("Product not found")  # Обработка случая, когда продукция не найдена
                return False  # Возвращаем результат, если продукция не найдена