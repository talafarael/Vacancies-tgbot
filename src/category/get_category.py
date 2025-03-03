from typing import List
from src.category.get_category_source import GetCategorySource


class GetCategory(GetCategorySource):
    def __init__(self,cluster) -> None:
        self.cluster=cluster
    async def get(self,name_collection:str) -> List[dict] :
        try:
            collection =self.cluster.test[name_collection]
            category=await collection.find().to_list(length=None)
            return category 
        except NameError:
            print(NameError)
            return []
    async def get_experience(self)->List[dict]:
        try:
            expirence=await self.cluster.test.experience.find().to_list(length=None) 
            return expirence
        except NameError:
            print(NameError)
            return []


