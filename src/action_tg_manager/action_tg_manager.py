from tg_message_manager.tg_message_manager import TgMessageManager
from user_manager.user import User


class ActionTgManager:
    def __init__(self, user: User, tg_message_manager: TgMessageManager):
        self._user = user
        self._tg_message_manager = tg_message_manager

    async def action_tg_manager(self, event):
        data = event.data.decode("utf-8")
        res = data.split(":")
        action = res[0]
        value = res[1]
        if "add_filter" == action:
            await self.add_filter(event, value)

    async def add_filter(self, event, value):
        try:
            chat_id = event.chat_id
            await self._user.add_filter(chat_id, value)
            await self._tg_message_manager.send_message(
                chat_id, "You successful add filter"
            )
            return True
        except NameError:
            print(NameError)
            return False
