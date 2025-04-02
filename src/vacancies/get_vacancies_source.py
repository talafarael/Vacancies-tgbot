from abc import ABC, abstractmethod
from types import NoneType
from typing import List, Tuple

from vacancy_types.vacancies_scrap_full_djinni_type import VacanciesScrapFullDjinniType
from vacancy_types.vacancies_scrap_type import VacanciesScrapType


get_one_vacancies_type = Tuple[
    List[VacanciesScrapFullDjinniType], List[VacanciesScrapFullDjinniType]
]


class GetVacanciesSource(ABC):
    @abstractmethod
    async def vacancies(self) -> NoneType:
        pass

    @abstractmethod
    async def get_one_vacancies(
        self,
        category_dou: str,
        year_dou: str,
        category_djinni: str,
        year_djinni: str,
    ) -> get_one_vacancies_type:
        pass

    @abstractmethod
    async def get_vacancy(self, vacancies) -> get_one_vacancies_type:
        pass
