import asyncio
from typing import List, Tuple
from connection.connect_sheet import ConnectSheet
from sheet_manager.djinni_sheet import DjinniSheet
from vacancy_types.vacancies_scrap_full_djinni_type import VacanciesScrapFullDjinniType
from vacancy_types.vacancies_scrap_type import VacanciesScrapType


class SheetManager:
    def __init__(self, connect_sheet: ConnectSheet) -> None:
        self._connect_sheet = connect_sheet

    async def distributor_vacancies(self, vacancies):
        if not vacancies:
            return
        await asyncio.gather(*(self.fill_sheet(vacancy) for vacancy in vacancies))

    async def fill_sheet(self, vacancies):
        if not vacancies:
            return
        sheet = await self._connect_sheet.connect_sheet("python-data-vacancies")
        worksheet = await sheet.get_worksheet(0)
        values = await worksheet.get_values()

        for vacancy in vacancies:
            print(vacancy)
            next_row = len(values) + 1
            title = vacancy.get("title", "")
            description = vacancy.get("description", "")
            link = vacancy.get("link", "")
            location = vacancy.get("location", "")
            company = vacancy.get("company", "")
            company = "" if len(company) > 15 else company
            company_img = vacancy.get("company_img", "")
            company_link = vacancy.get("company_link", "")
            language = vacancy.get("language", "")
            experience = vacancy.get("experience", "")
            salary = vacancy.get("salary", "")
            employment = vacancy.get("employment", "")
            region = vacancy.get("region", "")
            editorial = vacancy.get("editorial", "")
            type_product = vacancy.get("type_product", "")

            await worksheet.append_row(
                [
                    title,
                    description,
                    link,
                    location,
                    company,
                    company_img,
                    company_link,
                    salary,
                    language,
                    experience,
                    employment,
                    region,
                    editorial,
                    type_product,
                ]
            )
