import logging
logging.basicConfig(level=logging.INFO)

import asyncio


from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.testing.pickleable import User
from sqlalchemy.testing.plugin.plugin_base import warnings

from database import *
import pandas as pd     # библиотека для чтения CSV

from database.main import create_table


async def query_add_user_two(data: pd.DataFrame) -> str:
    async with Session() as session:
        for row in data.to_dict(orient='records'):
            session.add(UserBaseModel(**row))
        await session.commit()
        return "Данные успешно добавлены! Второй вариант"


async def query_add_user(data: pd.DataFrame) -> str:
    async with Session() as session:
        for row in data.to_dict(orient='records'):
            columns = ', '.join(row.keys())
            placeholders = ', '.join([f':{col}' for col in row.keys()])
            sql_query = f"""INSERT INTO users ({columns}) VALUES ({placeholders})"""
            await session.execute(text(sql_query), row)
        await session.commit()
        return "Данные успешно добавлены!"


async def read_file(file_path="name.csv") -> None:
    try:
        await create_table()  # Для очистки и создания новой таблицы
        data = pd.read_csv(file_path, sep=';', encoding='utf-8')
        logging.info(msg=await query_add_user_two(data))
    except Exception as e:
        logging.warning(f"Ошибка: {e}")
        return False


if __name__ == '__main__':

    logging.info("Запуск программы")
    asyncio.run(read_file())
    logging.info("Завершение работы программы")