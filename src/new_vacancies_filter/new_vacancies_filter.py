from typing import List, Tuple                              
from src.types.vacancies_dou_type import VacanciesScrapType 




get_one_vacancies_type=Tuple[List[VacanciesScrapType],List[VacanciesScrapType]]

class NewVacanciesFilter():
    def __init__(self,cluster) -> None:
        self._cluster=cluster
    async def filter_vacancies(self,get_one_vacancies_type:get_one_vacancies_type):
         all_vacancies = get_one_vacancies_type[0] + get_one_vacancies_type[1]
         vacancy_links = [vac["link"] for vac in all_vacancies]
         existing_links = await self._cluster.test.filter.distinct("link", {"link": {"$in": vacancy_links}})
         filtered_vacancies = [vac for vac in all_vacancies if vac["link"] not in existing_links]
         for vacancy in  filtered_vacancies:


    async def check_filter(self,vacancies:VacanciesScrapType):
        pass
    async def add_vacancies_filter_list(self):
        pass

