import random
from typing import List
import requests
import re
import urllib.request
from bs4 import BeautifulSoup

from djinni.vacancies_djinni_source import VacanciesDjinniSource
from vacancy_types.vacancies_scrap_type import VacanciesScrapType


class GetVacanciesDjinni(VacanciesDjinniSource):
    async def get_djinni_vacancies(self, url: str) -> List[VacanciesScrapType]:
        try:
            USER_AGENTS = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
            ]
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Referer": "https://jobs.dou.ua/",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            }
            response = requests.get(
                url, headers=headers, proxies=urllib.request.getproxies()
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        pattern = re.compile(r"^job-item-\d+$")
        arr_varancie = []
        for item in soup.find_all("li", id=pattern):
            title_element = item.find(class_="job-item__title-link")
            title = title_element.text.strip() if title_element else ""

            description_element = item.find(class_="js-truncated-text")
            description = (
                description_element.text.strip() if description_element else ""
            )

            link = title_element.get("href") if title_element else ""

            company_element = item.find(class_="text-body js-analytics-event")
            company = company_element.text.strip() if company_element else ""
            company_link = company_element.get("href") if company_element else ""

            company_img_element = item.find(class_="userpic-image userpic-image_img")
            company_img = company_img_element.get("src") if company_img_element else ""

            salary_element = item.find(class_="text-success text-nowrap")
            salary = salary_element.text.strip() if salary_element else ""

            info_section = item.find(
                class_="fw-medium d-flex flex-wrap align-items-center gap-1"
            )
            location_element = (
                info_section.find(class_="text-nowrap") if info_section else None
            )
            location = location_element.text.strip() if location_element else ""

            company = getattr(
                item.find(class_="fw-medium d-flex flex-wrap align-items-center gap-1"),
                "text",
                "",
            )

            varancie_djinni: VacanciesScrapType = {
                "title": title,
                "description": description,
                "link": f"https://djinni.co{link}",
                "location": location,
                "company": company,
                "company_img": company_img,
                "company_link": company_link,
                "salary": salary,
            }
            arr_varancie.append(varancie_djinni)
        return arr_varancie
