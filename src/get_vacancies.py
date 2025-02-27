import asyncio
from src.category.get_category_source import GetCategorySource
from src.djinni.vacancies_djinni_source import VacanciesDjinniSource
from src.dou.vacancies_dou_source import VacanciesDouSource


class GetVacancies:
    def __init__(
        self, cluster, getVacanciesDou: VacanciesDouSource, getVacanciesDjinni:VacanciesDjinniSource,getCategory:GetCategorySource
    ):
        self.cluster = cluster
        self.getVacanciesDou = getVacanciesDou
        self.getVacanciesDjinni = getVacanciesDjinni
        self.getCategory=getCategory
    async def vacancies(self):
        category =await self.getCategory.get_category()
        expirence =await self.getCategory.get_experience()
        await self.get_vacancies(expirence)
    async def get_vacancies(self,expirence):
        for exp in expirence: 
             vacancies = await self.get_one_vacancies("Node.js", exp["dou"], "Node.js", exp["djinni"]) 
             print(vacancies)

    async def get_one_vacancies(self, category_dou: str, year_dou: str,category_djinni: str, year_djinni: str,):
        url_dou=f"https://jobs.dou.ua/vacancies/?category={category_dou}&exp={year_dou}"
        url_djinni=f"https://djinni.co/jobs/?primary_keyword={category_djinni}&exp_level={year_djinni}" 

        


        dou, djinni = await asyncio.gather(
            self.getVacanciesDou.get_duo_vacancies(url_dou),
            self.getVacanciesDjinni.get_djinni_vacancies(url_djinni),
        )
        return dou,djinni
