


class User:
    def __init__(self, cluster) -> None:
        self._cluster = cluster
       
    async def user_create(self, chat_id: str, user_id: str,name:str):
        try:
            collection = self._cluster.test.user
            user = {
                "chat_id": chat_id,
                "user_id": user_id,
                "name":name,
                "vacancies":[]
            }
            res = await collection.insert_one(user)
            return res.inserted_id  
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None 


    async def add_filter(self,chat_id:str,vacancy_collection_id:str):
        try:
            collection = self._cluster.test.user
            await collection.update_one(
                {"chat_id": chat_id},
                {"$addToSet": {"vacancies": vacancy_collection_id}}  
            )
            return True
        except Exception as e:
            print(e)
            return False

