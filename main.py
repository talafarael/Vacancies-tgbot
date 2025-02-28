import asyncio
from src.category.get_category import GetCategory
from src.get_vacancies import GetVacancies
from src.dou.get_dou import GetVacanciesDou
from src.djinni.get_djinni import GetVacanciesDjinni
from src.create_data_for_bot import CreateDataForBot
from src.connect_db import connect_db
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from src.tgbot_service.tgbot import TgBot

load_dotenv()
print( os.getenv("TOKEN"))


experience = [
    {"name": "0-1 years", "dou": "0-1", "djinni": "1y"},
    {"name": "1-2 years", "dou": "1-3", "djinni": "2y"},
    {"name": "2-3 years", "dou": "1-3", "djinni": "3y"},
    {"name": "3-4 years", "dou": "3-5", "djinni": "4y"},
    {"name": "4-5 years", "dou": "3-5", "djinni": "5y"},
    {"name": "5-6 years", "dou": "5plus", "djinni": "6y"},
    {"name": "6-7 years", "dou": "5plus", "djinni": "7y"},
    {"name": "7-8 years", "dou": "5plus", "djinni": "8y"},
    {"name": "8-9 years", "dou": "5plus", "djinni": "9y"},
    {"name": "9-10 years", "dou": "5plus", "djinni": "10y"},
]
categories = [
    {"name": "Java", "djinni": "Java", "dou": "Java"},
    {"name": ".NET", "djinni": ".NET", "dou": ".NET"},
    {"name": "PHP", "djinni": "PHP", "dou": "PHP"},
    {"name": "C++", "djinni": "C++", "dou": "C++"},
    {"name": "Python", "djinni": "Python", "dou": "Python"},
    {"name": "AI/ML", "djinni": "AI/ML", "dou": "ML AI"},
    {"name": "Golang", "djinni": "Golang", "dou": "Golang"},
    {"name": "iOS/macOS", "djinni": "iOS/macOS", "dou": "iOS"},
    {"name": "Android", "djinni": "Android", "dou": "Android"},
    {"name": "Front End", "djinni": "Front End", "dou": "Fullstack"},
    {"name": "Node.js", "djinni": "Node.js", "dou": "Node.js"},
    {"name": "DevOps", "djinni": "DevOps", "dou": "DevOps"},
    {"name": "Rust", "djinni": "Rust", "dou": "Rust"},
    {"name": "Ruby", "djinni": "Ruby", "dou": "Ruby"},
    {"name": "Scala", "djinni": "Scala", "dou": "Scala"},
    {"name": "Erlang", "djinni": "Erlang", "dou": "None"},
    {"name": "Flutter", "djinni": "Flutter", "dou": "Flutter"},
    {"name": "React Native", "djinni": "React Native", "dou": "React Native"},
    {"name": "Elixir", "djinni": "None", "dou": "Elixir"},
    {"name": "Kotlin", "djinni": "None", "dou": "Kotlin"},
    {"name": "Salesforce", "djinni": "None", "dou": "Salesforce"},
    {"name": "ERP", "djinni": "None", "dou": "ERP"},
    {"name": "QA", "djinni": "None", "dou": "QA"},
    {"name": "Technical Writing", "djinni": "None", "dou": "Technical Writing"},
    {"name": "Marketing", "djinni": "None", "dou": "Marketing"},
    {"name": "HR", "djinni": "None", "dou": "HR"},
    {"name": "Support", "djinni": "None", "dou": "Support"},
]
url="https://djinni.co/jobs/"

async def create_data_for_bot():
    cluster = await connect_db()
    create_vacancies = CreateDataForBot(cluster)
    # results = await create_vacancies.create_vacancies(experience, "experience")
    results = await create_vacancies.create_vacancies(categories, "category") 




#asyncio.run(create_data_for_bot()) 

async def scrap():
    cluster = await connect_db()
    getVacanciesDjinni=GetVacanciesDjinni()
    getVacanciesDou=GetVacanciesDou()
    getCategory=GetCategory(cluster)
    getVacancies=GetVacancies(cluster,getVacanciesDou,getVacanciesDjinni,getCategory)
    await getVacancies.vacancies()
client = TelegramClient('bot', os.getenv("API_ID"), os.getenv("API_HASH")).start(bot_token=os.getenv("TOKEN"))
tg_bot=None
#async def start_bot():                       

    
    
    






@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    print("pec")
    cluster = await connect_db()              
    getCategory=GetCategory(cluster)          
    tg_bot=TgBot(cluster,client,getCategory)  

    if tg_bot:
        await tg_bot.button_return("category",event)


@client.on(events.CallbackQuery)
async def handle_callback(event):
    user_id = event.sender_id
    print(event)
    data = event.data.decode("utf-8")
    text = button_texts.get(data, "Неизвестная команда")
    print(data)











client.run_until_disconnected()

async def main():
    await start_bot()
    print("Bot started successfully!")
    await client.run_until_disconnected() 



asyncio.run(main())




#asyncio.run(scrap())
