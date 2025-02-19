import asyncio
from src.get_dou import get_duo_vacancies


url = "https://jobs.dou.ua/vacancies/feeds"


dou =asyncio.run(get_duo_vacancies(url))
print(dou[0].title)




