# from telethon import TelegramClient, events


from get_vacancies_collection.get_vacancies_collection_source import GetVacanciesCollectionSource
from telethon import Button


class TgBot:
    def __init__(
        self, cluster, client, getVacanciesCollection: GetVacanciesCollectionSource
    ) -> None:
        self._cluster = cluster
        self._client = client
        self._getVacanciesCollection = getVacanciesCollection

    async def start(self, event):
        print("a")

    async def button_return(self, type_button: str, event) -> None:
        method = await self._getVacanciesCollection.get_vacancies()
        if method:
            buttons = [
                [
                    Button.inline(
                        f"{item['category']['name']} | {item['experience']['name']}",
                        f"add_filter:{item['_id']}",
                    )
                ]
                for item in method
            ]
            await event.respond("Выберите команду:", buttons=buttons)
            return
        else:
            None
