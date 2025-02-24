import asyncio
from dou.vacancies_dou_source import VacanciesDouSource


class GetVacancies:
    def __init__(
        self, cluster, getVacanciesDou: VacanciesDouSource, getVacanciesDjinni
    ):
        self.cluster = cluster
        self.getVacanciesDou = getVacanciesDou
        self.getVacanciesDjinni = getVacanciesDjinni

    async def get_vacancies(self, category: str, year: str):
        url=f"https://jobs.dou.ua/vacancies/?category={category}&exp={year}"

        dou = asyncio.run(self.getVacanciesDou.get_duo_vacancies(url))
