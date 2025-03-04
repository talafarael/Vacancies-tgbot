

class TgMessageManager():
    def __init__(self,client):
        self._client=client


    async def send_message(self,chat_id,message):
        try:
            await self._client.send_message(chat_id, message)  
        except NameError:
            return None
