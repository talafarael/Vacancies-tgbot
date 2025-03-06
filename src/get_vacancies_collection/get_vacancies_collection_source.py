from abc import ABC, abstractmethod
from typing import List
from src.types.vacancies_full_obj_type import VacanciesFullType
from bson import ObjectId


class GetVacanciesCollectionSource(ABC):
    @abstractmethod
    async def get_vacancy(self, id: ObjectId) -> VacanciesFullType:
        pass

    @abstractmethod
    async def get_vacancies(self) -> List[VacanciesFullType]:
        pass
