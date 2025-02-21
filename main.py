from src.create_vacancies_variant import CreateVacancie
from src.connect_db import connect_db


async def insert_data():
    cluster = await connect_db()
    create_vacancies = CreateVacancie(cluster)
    await create_vacancies.create_vacancies()


url = "https://djinni.co/jobs/?primary_keyword=JavaScript&primary_keyword=React.js"
