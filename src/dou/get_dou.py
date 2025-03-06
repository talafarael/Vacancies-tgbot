import random
import time
from typing import List
from src.dou.vacancies_dou_source import VacanciesDouSource
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src.types.vacancies_dou_type import VacanciesScrapType
from webdriver_manager.chrome import ChromeDriverManager


class GetVacanciesDou(VacanciesDouSource):
    async def get_duo_vacancies(self, url: str) -> List[VacanciesScrapType]:
        try:
            USER_AGENTS = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            ]
            user_agent = random.choice(USER_AGENTS)

            # Настройки Chrome
            chrome_options = Options()
            chrome_options.add_argument(f"user-agent={user_agent}")
            chrome_options.add_argument("--headless")  # Запуск без интерфейса
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            # Запуск WebDriver
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=chrome_options
            )
            driver.get(url)
            time.sleep(3)  # Даем странице время загрузиться

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
