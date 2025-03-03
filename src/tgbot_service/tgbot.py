#from telethon import TelegramClient, events
from telethon import Button


from src.category.get_category_source import GetCategorySource


class TgBot:
    def __init__(self,cluster,client,getCategory:GetCategorySource) -> None:
        self._cluster=cluster
        self._client=client 
        self._getCategory=getCategory

    async def start(self, event):
        print("a")
   
    async def button_return(self,type_button:str,event)->None:
        method = await self._getCategory.get(type_button)
        if method: 
           buttons = [
                [Button.inline(item["name"],f"add_filter_category:{item["name"]}" )]
                for item in method
            ]
           await event.respond("Выберите команду:", buttons=buttons)
           return
        else:
            None
        


