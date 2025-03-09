from abc import ABC, abstractmethod
from typing import List

from vacancy_types.category_obj_type import CategoryType
from vacancy_types.collection import CollectionName




class GetCategorySource(ABC):
    @abstractmethod
    async def get_one(self, id: str, name_collection: CollectionName) -> CategoryType:
        pass

    @abstractmethod
    async def get(self, name_collection: CollectionName) -> List[CategoryType]:
        pass

    @abstractmethod
    async def get_experience(self) -> List[dict]:
        pass
