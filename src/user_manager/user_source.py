from abc import ABC, abstractmethod
from typing import List

from vacancy_types.user_obj_type import UserType


class UserSource(ABC):
    @abstractmethod
    async def user_vacancies_find(self, vacancy_id: str) -> List[UserType]:
        pass

    @abstractmethod
    async def user_create(
        self, chat_id: str, user_id: str, name: str
    ) -> UserType | None:
        pass

    @abstractmethod
    async def add_filter(self, chat_id: str, vacancy_collection_id: str) -> bool:
        pass
