from src.get_djinni import get_djinni
from src.connect_db import connect_db
import asyncio

async def insert_data():
    cluster = await connect_db()  
url="https://djinni.co/jobs/?primary_keyword=JavaScript&primary_keyword=React.js"
asyncio.run(get_djinni(url))
