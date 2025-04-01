from connection.connect_sheet import ConnectSheet
from vacancy_types.vacancies_scrap_full_djinni_type import VacanciesScrapFullDjinniType


class DjinniSheet:
    def __init__(self,connect_sheet:ConnectSheet) -> None:
        self._connect_sheet=connect_sheet
    def fill_sheet(self,djinni_vacancies:VacanciesScrapFullDjinniType):
        pass
