import asyncio
from dou.vacancies_dou_source import VacanciesDouSource


class GetVacancies:
    def __init__(
        self, cluster, getVacanciesDou: VacanciesDouSource, getVacanciesDjinni
    ):
        self.cluster = cluster
        self.getVacanciesDou = getVacanciesDou
        self.getVacanciesDjinni = getVacanciesDjinni
    async def vacancies(self):
        print("si")
        
    async def get_vacancies(self, category_dou: str, year_dou: str,category_djinni: str, year_djinni: str,):
        url_dou=f"https://jobs.dou.ua/vacancies/?category={category_dou}&exp={year_dou}"
        url_djinni=f"https://djinni.co/jobs/?primary_keyword={category_djinni}&exp_level={year_djinni}" 
        dou, djinni = await asyncio.gather(
            self.getVacanciesDou.get_duo_vacancies(url_dou),
            self.getVacanciesDjinni.get_djinni_vacancies(url_djinni),
        )
        return dou,djinni
