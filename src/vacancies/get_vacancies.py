import asyncio
from typing import List
from src.new_vacancies_filter.new_vacancies_filter import NewVacanciesFilter
from src.get_vacancies_collection.get_vacancies_collection_source import (
    GetVacanciesCollectionSource,
)
import random
from src.djinni.vacancies_djinni_source import VacanciesDjinniSource
from src.dou.vacancies_dou_source import VacanciesDouSource
from src.user_manager.user_source import UserSource
from src.vacancies.get_vacancies_source import GetVacanciesSource
from src.tg_message_manager.tg_message_manager import TgMessageManager
from src.types.user_obj_type import UserType


class GetVacancies(GetVacanciesSource):
    def __init__(
        self,
        cluster,
        getVacanciesDou: VacanciesDouSource,
        getVacanciesDjinni: VacanciesDjinniSource,
        getVacancieCollection: GetVacanciesCollectionSource,
        userManager: UserSource,
        newVacanciesFilter: NewVacanciesFilter,
        tgMessageManager: TgMessageManager,
    ):
        self.cluster = cluster
        self.getVacanciesDou = getVacanciesDou
        self.getVacanciesDjinni = getVacanciesDjinni
        self._getVacancieCollection = getVacancieCollection
        self._userManager = userManager
        self._newVacanciesFilter = newVacanciesFilter
        self._tgMessageManager = tgMessageManager

    async def vacancies(self):
        vacancies_list = await self._getVacancieCollection.get_vacancies()
        for vacancy in vacancies_list:
            dou_list, djinni_list = await self.get_vacancy(vacancy)
            list_vacancy = await self._newVacanciesFilter.filter_vacancies(
                (dou_list, djinni_list)
            )

            users: List[UserType] = await self._userManager.user_vacancies_find(
                vacancy["_id"]
            )
            await self._tgMessageManager.user_vacancies_mailing_list(
                users, list_vacancy
            )

    async def get_vacancy(self, vacancies):
        dou, djinni = await self.get_one_vacancies(
            vacancies["category"]["dou"],
            vacancies["experience"]["dou"],
            vacancies["category"]["djinni"],
            vacancies["experience"]["djinni"],
        )
        return dou, djinni

    async def get_one_vacancies(
        self,
        category_dou: str,
        year_dou: str,
        category_djinni: str,
        year_djinni: str,
    ):
        url_dou = (
            f"https://jobs.dou.ua/vacancies/?category={category_dou}&exp={year_dou}"
        )
        url_djinni = f"https://djinni.co/jobs/?primary_keyword={category_djinni}&exp_level={year_djinni}"
        await asyncio.sleep(random.uniform(2, 5))
        dou, djinni = await asyncio.gather(
            self.getVacanciesDou.get_duo_vacancies(url_dou),
            self.getVacanciesDjinni.get_djinni_vacancies(url_djinni),
        )
        return dou, djinni
