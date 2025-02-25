from typing import List, Tuple
from src.category.get_category_source import GetCategorySource


class GetCategory(GetCategorySource):
    def __init__(self,cluster) -> None:
        self.cluster=cluster
    async def get_category(self) -> Tuple[List[dict], List[dict]] :
        try:
            category=await self.cluster.test.category.find().to_list(length=None)
            expirence=await self.cluster.test.experience.find().to_list(length=None)
            return category ,expirence
        except NameError:
            print(NameError)
            return [],[]

