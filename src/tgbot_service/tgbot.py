from telethon.tl.custom import Button
#from telethon import TelegramClient, events


from src.category.get_category_source import GetCategorySource


class TgBot:
    def __init__(self,cluster,client,getCategory:GetCategorySource) -> None:
        self._cluster=cluster
        self._client=client 
        self._getCategory=getCategory
        self.methods = {
            "category": self._getCategory.get_category,
            "experience": self._getCategory.get_experience,
        }

    async def start(self, event):
        print("a")
   
    async def button_return(self,type_button:str,event)->None:
        method = self.methods.get(type_button)
        if method: 
            res=await method()
            buttons = [
                [Button.inline(item["name"],f"add_filter_category:{item["name"]}" )]
                for item in res
            ]
            await event.respond("Выберите команду:", buttons=buttons)
            return
        else:
            None
        


