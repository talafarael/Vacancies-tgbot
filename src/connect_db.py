from motor.motor_asyncio import AsyncIOMotorClient

async def connect_db()-> AsyncIOMotorClient:
    cluster=AsyncIOMotorClient("mongodb+srv://fara:123456780a@cluster0.fnu9v.mongodb.net/test")
    return cluster
