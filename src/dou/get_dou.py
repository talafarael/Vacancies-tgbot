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
                    print(getattr(item.find(class_="date"), "text", None))
            return arr_varancie
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return []


