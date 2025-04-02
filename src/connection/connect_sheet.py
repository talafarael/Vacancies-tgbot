import asyncio
from typing import Awaitable
import gspread_asyncio
from google.oauth2.service_account import Credentials
import os


class ConnectSheet:
    async def client_connect(self):
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]
        json_path = os.path.abspath("./artful-journey-455514-e2-319e56628090.json")

        def get_creds():
            return Credentials.from_service_account_file(json_path, scopes=scopes)

        agcm = gspread_asyncio.AsyncioGspreadClientManager(
            get_creds
        )  # ✅ Передаём функцию!
        client = await agcm.authorize()
        return client

    async def connect_sheet(self, name: str):
        client = await self.client_connect()  # ✅ Исправлено
        try:
            sheet = await client.open(name)
            return sheet
        except NameError:
            sheet = await client.create(name)
            return sheet
