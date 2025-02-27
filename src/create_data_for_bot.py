import asyncio





class CreateDataForBot:
    def __init__(self, cluster):
        self.cluster = cluster

    async def create_vacancy(self, value, name_value):
        vacancies = {
            "dou": value["dou"],
            "djinni": value["djinni"],
            "name": value["name"],
            "users":[],
        }
        collection = self.cluster.test[name_value]
        await collection.insert_one(vacancies)

    async def create_vacancies(self, value, name_value: str):
        tasks = [self.create_vacancy(values, name_value) for values in value]
        await asyncio.gather(*tasks)
