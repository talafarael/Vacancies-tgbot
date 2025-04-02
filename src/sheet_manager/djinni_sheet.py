from connection.connect_sheet import ConnectSheet
from vacancy_types.vacancies_scrap_full_djinni_type import VacanciesScrapFullDjinniType


class DjinniSheet:
    def __init__(self, connect_sheet: ConnectSheet) -> None:
        self._connect_sheet = connect_sheet

    async def fill_sheet(self, djinni_vacancies: VacanciesScrapFullDjinniType):
        sheet = await self._connect_sheet.connect_sheet("python-data-vacancies")
        worksheet = await sheet.get_worksheet(0)
        values = await worksheet.get_values()
        next_row = len(values) + 1
        row_values = [
            djinni_vacancies["title"],
            djinni_vacancies["description"],
            djinni_vacancies["link"],
            djinni_vacancies["location"],
            djinni_vacancies["company"],
            djinni_vacancies["company_img"],
            djinni_vacancies["company_link"],
            djinni_vacancies["salary"],
            djinni_vacancies["language"],
            djinni_vacancies["experience"],
            djinni_vacancies["employment"],
            djinni_vacancies["region"],
            djinni_vacancies["editorial"],
            djinni_vacancies["type_product"],
        ]
        await worksheet.update(f"A{next_row}", [row_values])
