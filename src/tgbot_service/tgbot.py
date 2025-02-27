
#from telethon import TelegramClient, events


from src.category.get_category_source import GetCategorySource


class TgBot:
    def __init__(self,cluster,client,getCategory:GetCategorySource) -> None:
        self._cluster=cluster
        self._client=client 
        self._getCategory=getCategory
        self.methods = {
            "get_category": self._getCategory.get_category,
            "get_experience": self._getCategory.get_experience,
        }

    async def start(self, event):
        print("a")
   
    async def button_return(self,type_button:str)->None:
        print("")
        method = self.methods.get(type_button)
        if method: 
            res=await method()
        else:
            None
        


