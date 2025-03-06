from abc import ABC, abstractmethod
from typing import List

from src.types.vacancies_dou_type import VacanciesScrapType


class VacanciesDjinniSource(ABC):
    @abstractmethod
    async def get_djinni_vacancies(self, url: str) -> List[VacanciesScrapType]:
        pass
