from abc import ABC, abstractmethod
from typing import List

from vacancy_types.vacancies_scrap_full_djinni_type import VacanciesScrapFullDjinniType
from vacancy_types.vacancies_scrap_type import VacanciesScrapType


class VacanciesDouSource(ABC):
    @abstractmethod
    async def get_duo_vacancies(
        self, url: str, year: str
    ) -> List[VacanciesScrapFullDjinniType]:
        pass
