import asyncio
from typing import List

from vacancy_types.user_obj_type import UserType
from vacancy_types.vacancies_scrap_type import VacanciesScrapType








class TgMessageManager:
    def __init__(self, client):
        self._client = client

    async def user_vacancies_mailing_list(
        self, users: List[UserType], vacancies_lsit: List[VacanciesScrapType]
):
        tasks = []
        for vacancy in vacancies_lsit:
            
            text = (
                f"📌 *{vacancy['title']}*\n"
                f"🏢 *Компания:* [{vacancy['company']}]({vacancy['company_link']})\n"
                f"📍 *Локация:* {vacancy['location']}\n"
                f"💰 *Зарплата:* {vacancy['salary']}\n\n"
                f"📝 *Описание:*\n{vacancy['description']}\n\n"
                f"🔗 [Подробнее]({vacancy['link']})"
            )
            print(text)
            print(users)
            for user in users:
                print(user)
                tasks.append(self.send_message(user["chat_id"], text))

        await asyncio.gather(*tasks)

    async def send_message(self, chat_id, message):
        try:
            await self._client.send_message(chat_id, message)
        except NameError:
            return None
