import asyncio
from src.category.get_category import GetCategory
from src.get_vacancies import GetVacancies
from src.dou.get_dou import GetVacanciesDou
from src.djinni.get_djinni import GetVacanciesDjinni
from src.create_data_for_bot import CreateDataForBot
from src.connect_db import connect_db

experience = [
    {"name": "0-1 years", "dou": "0-1", "djinni": "1y"},
    {"name": "1-2 years", "dou": "1-3", "djinni": "2y"},
    {"name": "2-3 years", "dou": "1-3", "djinni": "3y"},
    {"name": "3-4 years", "dou": "3-5", "djinni": "4y"},
    {"name": "4-5 years", "dou": "3-5", "djinni": "5y"},
    {"name": "5-6 years", "dou": "5plus", "djinni": "6y"},
    {"name": "6-7 years", "dou": "5plus", "djinni": "7y"},
    {"name": "7-8 years", "dou": "5plus", "djinni": "8y"},
    {"name": "8-9 years", "dou": "5plus", "djinni": "9y"},
    {"name": "9-10 years", "dou": "5plus", "djinni": "10y"},
]

url="https://djinni.co/jobs/"

async def create_data_for_bot():
    cluster = await connect_db()
    create_vacancies = CreateDataForBot(cluster)
    results = await create_vacancies.create_vacancies(experience, "experience")




async def scrap():
    cluster = await connect_db()
    getVacanciesDjinni=GetVacanciesDjinni()
    getVacanciesDou=GetVacanciesDou()
    getCategory=GetCategory(cluster)
    getVacancies=GetVacancies(cluster,getVacanciesDou,getVacanciesDjinni,getCategory)
    await getVacancies.vacancies()




 
asyncio.run(scrap())

