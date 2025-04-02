from abc import ABC, abstractmethod
from typing import List

from vacancy_types.vacancies_scrap_full_djinni_type import VacanciesScrapFullDjinniType
from vacancy_types.vacancies_scrap_type import VacanciesScrapType


class VacanciesDjinniSource(ABC):
    @abstractmethod
    async def get_djinni_vacancies(self, url: str) -> List[VacanciesScrapFullDjinniType]:
        pass
