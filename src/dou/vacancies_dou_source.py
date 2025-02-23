from abc import ABC, abstractmethod
from typing import List

from src.dou.vacancies_dou import VacanciesDou


class VacanciesDouSource(ABC):
    @abstractmethod
    async def get_duo_vacancies(self, url: str) -> List[VacanciesDou]:
        pass
