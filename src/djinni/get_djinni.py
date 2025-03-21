from enum import Enum
import random
from typing import List, TypedDict
import requests
import re
import urllib.request
from bs4 import BeautifulSoup


from djinni.vacancies_djinni_source import VacanciesDjinniSource
from vacancy_types.vacancies_scrap_type import VacanciesScrapType


class ValidEnum(Enum):
    @staticmethod
    def is_valid(value):
        return value in ValidEnum._value2member_map_


class Language(ValidEnum):
    NoEnglish = "No English"
    BeginnerElementary = "Beginner/Elementary"
    PreIntermediate = "Pre-Intermediate"
    Intermediate = "Intermediate"
    UpperIntermediate = "Upper-Intermediate"
    AdvancedFluent = "Advanced/Fluent"


class Experience(ValidEnum):
    Бездосвіду = "Без досвіду"
    рік1 = "1 рік"
    роки2 = "2 роки"
    роки3 = "3 роки"
    роки4 = "4 роки"
    років5 = "5 років"
    років6 = "6 років"
    років7 = "7 років"
    років8 = "8 років"
    років9 = "9 років"
    років_та_більше10 = "10 років та більше"


class Employment(ValidEnum):
    Віддалена_робота = "Віддалена робота"
    Part_time = "Part-time"
    Офіс = "Офіс"


class Region(ValidEnum):
    Україна = "Україна"
    Країни_ЄС = "Країни ЄС"
    Інші_країни = "Інші країни"


class Editorial(ValidEnum):
    Вказана_зарплатна_вилка = "Вказана зарплатна вилка"
    Ukrainian_Product = "Ukrainian Product 🇺🇦"
    MilTech = "MilTech 🪖"
    Mobilisation_Reservation = "Mobilisation reservation ⏳"


class JobRequirements(TypedDict):
    language: Language | None 
    experience: Experience | None
    employment: Employment| None
    region: Region| None
    editorial: Editorial| None


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
            print("work")
            company_element = item.find(class_="text-body js-analytics-event")
            company = company_element.text.strip() if company_element else ""
            company_link = company_element.get("href") if company_element else ""

            company_img_element = item.find(class_="userpic-image userpic-image_img")
            company_img = company_img_element.get("src") if company_img_element else ""

            salary_element = item.find(class_="text-success text-nowrap")
            salary = salary_element.text.strip() if salary_element else ""
            # this i need upgrade
            info_section = item.find(
                class_="fw-medium d-flex flex-wrap align-items-center gap-1"
            )
            self.get_parametr(info_section)
            print(info_section)
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

    def get_parametr(self, medium_div):
        jobRequirements: JobRequirements={
             "language":  None,     
             "experience":  None, 
             "employment":  None,  
             "region":  None,          
             "editorial":  None    
        }
        field_checks = {
            "language": Language,
            "experience": Experience,
            "employment": Employment,
            "region": Region,
            "editorial": Editorial
        }
        for span in medium_div.find_all("span", class_="text-nowrap"):
            result = span.get_text(strip=True)
            for field, FieldClass in field_checks.items():
                if FieldClass.is_valid(result):
                    jobRequirements[field] = FieldClass(result).value
        return jobRequirements
