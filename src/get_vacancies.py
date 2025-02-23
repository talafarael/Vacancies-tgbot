from dou.vacancies_dou_source import VacanciesDouSource


class GetVacancies:
    def __init__(
        self, cluster, getVacanciesDou: VacanciesDouSource, getVacanciesDjinni
    ):
        self.cluster = cluster
        self.getVacanciesDou = getVacanciesDou
        self.getVacanciesDjinni = getVacanciesDjinni

    async def get_vacancies(self, title: str, year: str):
        dou = self.getVacanciesDou.get_duo_vacancies("")
