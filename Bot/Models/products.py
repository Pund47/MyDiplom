import sqlalchemy
from sqlalchemy import Column, select, ForeignKey
from Bot.settings.config_bot import Base, async_session


class Product(Base):
    __tablename__ = 'products'
    name      = Column(sqlalchemy.Text)
    id        = Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    price     = Column(sqlalchemy.INTEGER)
    img       = Column(sqlalchemy.String)
    basket_id = Column(sqlalchemy.INTEGER,ForeignKey("products.basket_id"))
    category  = Column(sqlalchemy.String)

    def __init__(self,name,id,price,img,basket_id,category):
        self.name      = name
        self.id        = id
        self.price     = price
        self.img       = img
        self.basket_id = basket_id
        self.category = category
#Base.metadata.create_all(bind=engine)

    @classmethod
    async def find_by(cls, category):
        async with async_session() as session:
            existing_prod = await session.execute(select(cls).where(cls.category == category))
            existing_prod = existing_prod.scalars().all()
            await session.commit()
            return existing_prod

    @classmethod
    async def find_by_id(cls, id):
        async with async_session() as session:
            found_prod = await session.execute(select(cls).where(cls.id == id))
            found_prod = found_prod.scalars().all()
            await session.commit()
            return found_prod