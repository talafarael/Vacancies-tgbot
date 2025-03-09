from abc import ABC, abstractmethod
from typing import List
from bson import ObjectId
from vacancy_types.vacancies_full_obj_type import VacanciesFullType


class GetVacanciesCollectionSource(ABC):
    @abstractmethod
    async def get_vacancy(self, id: ObjectId) -> VacanciesFullType:
        pass

    @abstractmethod
    async def get_vacancies(self) -> List[VacanciesFullType]:
        pass
