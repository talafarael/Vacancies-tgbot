from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv 

load_dotenv()             


async def connect_db()-> AsyncIOMotorClient:
    cluster=AsyncIOMotorClient(os.getenv("DB"))
    return cluster
