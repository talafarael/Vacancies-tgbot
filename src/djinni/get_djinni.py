from typing import List
import requests
import re
import urllib.request
from bs4 import BeautifulSoup

from src.djinni.vacancies_djinni_source import VacanciesDjinniSource
from src.types.vacancies_dou_type import VacanciesScrapType


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://jobs.dou.ua/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}


class GetVacanciesDjinni(VacanciesDjinniSource):
    async def get_djinni_vacancies(self, url: str)->List[VacanciesScrapType]:
        try:
            response = requests.get(
                url, headers=headers, proxies=urllib.request.getproxies()
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        pattern = re.compile(r"^job-item-\d+$")
        arr_varancie=[]
        for item in soup.find_all("li", id=pattern):
            title = getattr(item.find(class_="job-item__title-link"),"text","")
            description=getattr(item.find(class_="js-truncated-text"), "text", "") 
            link=item.find(class_="job-item__title-link").get("href") 
            company=getattr(item.find(class_="text-body js-analytics-event"), "text", "")  
            company_img_element = item.find(class_="userpic-image userpic-image_img")
            company_img = company_img_element.get("src") if company_img_element and company_img_element.get("src") else ""

            company_link=item.find(class_="text-body js-analytics-event").get("href")   
            salary= getattr(item.find(class_="text-success text-nowrap"), "text", "")   



            info_section = item.find(class_="fw-medium d-flex flex-wrap align-items-center gap-1")
            location= info_section.find(class_="text-nowrap").text


            company = getattr(item.find(
                class_="fw-medium d-flex flex-wrap align-items-center gap-1"
            ),"text","")

            varancie_djinni=VacanciesDjinni(
                title,
                description,
                f"https://djinni.co{link}",
                location,
                company,
                company_img,
                company_link,
                salary,
            )
            arr_varancie.append(varancie_djinni) 
        return arr_varancie

