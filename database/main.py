import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.base import Base
from database.models import *
from database.settings import get_settings_connect

engine = create_async_engine(
    url=get_settings_connect(),
    echo=False,
    pool_size=10,
    max_overflow=100,
)





Session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
async def create_table():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
        print("создано")




# asyncio.run(create_table())