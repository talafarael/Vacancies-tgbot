



class ActionTgManager():
    async def action_tg_manager(self,event):
        user_id = event.sender_id         
        data = event.data.decode("utf-8") 
        res=data.split(":")               
        action = res[0]                   
        value=res[0]                      

