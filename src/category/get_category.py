from typing import List
from category.get_category_source import GetCategorySource
from vacancy_types.category_obj_type import CategoryType
from vacancy_types.collection import CollectionName




class GetCategory(GetCategorySource):
    def __init__(self, cluster) -> None:
        self.cluster = cluster

    async def get_one(self, id: str, name_collection: CollectionName) -> CategoryType:
        collection = await self.cluster[name_collection]
        return collection

    async def get(self, name_collection: CollectionName) -> List[CategoryType]:
        try:
            collection = self.cluster.test[name_collection]
            category = await collection.find().to_list(length=None)
            return category
        except NameError:
            print(NameError)
            return []

    async def get_experience(self) -> List[dict]:
        try:
            expirence = await self.cluster.test.experience.find().to_list(length=None)
            return expirence
        except NameError:
            print(NameError)
            return []
