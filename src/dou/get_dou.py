from typing import List
import requests
from bs4 import BeautifulSoup
from src.dou.vacancies_dou import VacanciesDou
from src.dou.vacancies_dou_source import  VacanciesDouSource





class GetVacanciesDou(VacanciesDouSource):
    async def get_duo_vacancies(self, url: str) -> List[VacanciesDou]:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://jobs.dou.ua/",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        }

        try:
            arr_varancie = []
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            for item in soup.find_all(class_="l-vacancy"):
                description=getattr(item.find(class_="sh-info"), "text", "")
                title=getattr(item.find(class_="title"), "text", "") 
                link=item.find(class_="vt").get("href")

                location=getattr(item.find(class_="cities"), "text", "")
                company_link=item.find(class_="company").get("href")
                company_img = item.find(class_="f-i")
                company_img = company_img['src'] if company_img and 'src' in company_img.attrs else None
                company=getattr(item.find(class_="company"), "text", None)
                salary=getattr(item.find(class_="salary"), "text", None) 
                vacancies_dou =VacanciesDou(
                    title,
                    description,
                    link,
                    location,
                    company,
                    company_link,
                    company_img,
                    salary
                )
                arr_varancie.append(vacancies_dou)



            return arr_varancie
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []


