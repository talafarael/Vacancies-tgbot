


class User:
    def __init__(self, cluster) -> None:
        self.cluster = cluster

    async def user_create(self, chat_id: str, user_id: str):
        try:
            collection = self.cluster.test.user
            user = {
                "chat_id": chat_id,
                "user_id": user_id,
                "category": [],
                "experience_year": [],
                "language_level": []
            }
            res = await collection.insert_one(user)
            return res.inserted_id  
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None 
