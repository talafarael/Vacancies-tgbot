import asyncio


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


class CreateDataForBot:
    def __init__(self, cluster):
        self.cluster = cluster

    async def create_vacancy(self, value, name_value):
        vacancies = {
            "dou": value["dou"],
            "djinni": value["djinni"],
            "name": value["name"],
        }
        collection = self.cluster.test[name_value]
        await collection.insert_one(vacancies)

    async def create_vacancies(self, value, name_value: str):
        tasks = [self.create_vacancy(values, name_value) for values in value]
        await asyncio.gather(*tasks)
