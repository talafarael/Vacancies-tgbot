import asyncio


categories = [
    {"name": "JavaScript", "djinni": True, "dou": False},
    {"name": "Angular", "djinni": True, "dou": False},
    {"name": "React.js", "djinni": True, "dou": False},
    {"name": "Svelte", "djinni": True, "dou": False},
    {"name": "Vue.js", "djinni": True, "dou": False},
    {"name": "Node.js", "djinni": True, "dou": True},
    {"name": "Python", "djinni": True, "dou": True},
    {"name": "PHP", "djinni": True, "dou": True},
    {"name": "C++", "djinni": True, "dou": True},
    {"name": ".NET", "djinni": True, "dou": True},
    {"name": "Java", "djinni": True, "dou": True},
    {"name": "AI/ML", "djinni": False, "dou": True},
    {"name": "Golang", "djinni": True, "dou": True},
    {"name": "iOS/macOS", "djinni": False, "dou": True},
    {"name": "Android", "djinni": True, "dou": True},
    {"name": "Front End", "djinni": False, "dou": True},
    {"name": "DevOps", "djinni": True, "dou": True},
    {"name": "Rust", "djinni": True, "dou": True},
    {"name": "Ruby", "djinni": True, "dou": True},
    {"name": "Scala", "djinni": True, "dou": True},
    {"name": "Erlang", "djinni": False, "dou": True},
    {"name": "Flutter", "djinni": True, "dou": True},
    {"name": "React Native", "djinni": True, "dou": True},
]


class CreateVacancie:
    def __init__(self, cluster):
        self.cluster = cluster

    async def create_vacancie(self, dou: bool, djinni: bool, name: str):
        print("aa")
        vacancies = {
            dou: dou,
            djinni: djinni,
        }

    async def create_vacancies(self):
        tasks = [
            self.create_vacancie(category["dou"], category["djinni"], category["name"])
            for category in categories
        ]
        await asyncio.gather(*tasks)
