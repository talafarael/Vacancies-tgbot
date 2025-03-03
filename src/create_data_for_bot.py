
import asyncio
from src.category.get_category_source import GetCategorySource



class CreateDataForBot:
    def __init__(self, cluster,getCategory:GetCategorySource):
        self.cluster = cluster
        self.getCategory=getCategory

    async def create_vacancy(self, value, name_value):
        vacancies = {
            "dou": value["dou"],
            "djinni": value["djinni"],
            "name": value["name"],
            "users":[],
        }
        collection = self.cluster.test[name_value]
        await collection.insert_one(vacancies)

    async def create_vacancies(self):
        categories=await self.getCategory.get("category")
        experiencies=await self.getCategory.get("experience") 
        tasks = []
        for category in categories:
            for experience in experiencies:
                tasks.append(self.create_vacancies_relationship_collect(category["_id"], experience["_id"], category["name"],category["name"]))
        
        await asyncio.gather(*tasks)
    async def create_vacancies_relationship_collect(self,id_category:str,id_experience:str,name:str,experience:str):
        vacancies={
            "name":f"{name} {experience}",
            "id_category":id_category,
            "id_experience":id_experience
            }
        await self.cluster.test.vacancies.insert_one(vacancies)
