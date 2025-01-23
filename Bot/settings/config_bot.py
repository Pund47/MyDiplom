from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.dialects import sqlite
from sqlalchemy.orm import DeclarativeBase

API = "7595050434:AAG5uOSuKS_pRXmfcg6X_9SJemSmx9LYlp4"


engine = create_async_engine('sqlite+aiosqlite:///my_db.db')
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all(bind=engine))

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

