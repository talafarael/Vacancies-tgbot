from typing import List
from dou.vacancies_dou_source import VacanciesDouSource
from get_page.get_page import GetPage
from selenium.webdriver.common.by import By
from vacancy_types.vacancies_scrap_type import VacanciesScrapType


class GetVacanciesDou(VacanciesDouSource):
    def __init__(self,get_page:GetPage) -> None:
        self.get_page=get_page
    async def get_duo_vacancies(self, url: str) -> List[VacanciesScrapType]:
        try:
            driver=await self.get_page.get_page(url)

            vacancies = []
            vacancy_elements = driver.find_elements(By.CLASS_NAME, "l-vacancy")

            for item in vacancy_elements:
                title = (
                    item.find_element(By.CLASS_NAME, "title").text
                    if item.find_elements(By.CLASS_NAME, "title")
                    else ""
                )
                link = (
                    item.find_element(By.CLASS_NAME, "vt").get_attribute("href")
                    if item.find_elements(By.CLASS_NAME, "vt")
                    else ""
                )
                description = (
                    item.find_element(By.CLASS_NAME, "sh-info").text
                    if item.find_elements(By.CLASS_NAME, "sh-info")
                    else ""
                )
                location = (
                    item.find_element(By.CLASS_NAME, "cities").text
                    if item.find_elements(By.CLASS_NAME, "cities")
                    else ""
                )
                company = (
                    item.find_element(By.CLASS_NAME, "company").text
                    if item.find_elements(By.CLASS_NAME, "company")
                    else ""
                )
                company_link = (
                    item.find_element(By.CLASS_NAME, "company").get_attribute("href")
                    if item.find_elements(By.CLASS_NAME, "company")
                    else ""
                )
                company_img = (
                    item.find_element(By.CLASS_NAME, "f-i").get_attribute("src")
                    if item.find_elements(By.CLASS_NAME, "f-i")
                    else None
                )
                salary = (
                    item.find_element(By.CLASS_NAME, "salary").text
                    if item.find_elements(By.CLASS_NAME, "salary")
                    else ""
                )

                vacancies.append(
                    {
                        "title": title,
                        "description": description,
                        "link": link,
                        "location": location,
                        "company": company,
                        "company_link": company_link,
                        "company_img": company_img,
                        "salary": salary,
                    }
                )
            driver.quit()
            return vacancies

        except Exception as e:
            print(f"Error: {e}")
            return []
