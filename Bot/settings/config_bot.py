from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

API = "7595050434:AAG5uOSuKS_pRXmfcg6X_9SJemSmx9LYlp4"
ADMIN_ID = 5288495744
list_of_category = ["shrimps", "shellfish" , "fish" , "caviar"]
list_of_atr_productions_to_make_change = ["name","price","img","count","category"]


engine = create_async_engine('sqlite+aiosqlite:///my_db.db')
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def create_tables():
    from Bot.Models.user import User
    from Bot.Models.products import Product
    from Bot.Models.basket import Baskets

    async with engine.begin() as conn:
        await conn.run_sync(lambda sync_conn: Base.metadata.create_all(bind=sync_conn))


#    async with engine.begin() as conn:
#        await conn.run_sync(Base.metadata.create_all(engine))

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

