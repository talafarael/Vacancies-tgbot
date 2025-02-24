import requests
import re
import urllib.request
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://jobs.dou.ua/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}


class GetVacanciesDjinni:
    async def get_djinni(self, url: str):
        try:
            response = requests.get(
                url, headers=headers, proxies=urllib.request.getproxies()
            )
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        pattern = re.compile(r"^job-item-\d+$")
        for item in soup.find_all("li", id=pattern):
            title = getattr(item.find(class_="job-item__title-link"),"text","")
            description=getattr(item.find(class_="js-truncated-text"), "text", "") 
            link=item.find(class_="job-item__title-link").get("href") 
            info_section = item.find(class_="fw-medium d-flex flex-wrap align-items-center gap-1")
            info_items= info_section.find_all(class_="text-nowrap")

            remote_type=info_items[0].text
            
            print("Удаленная работа:", remote_type)
            company = getattr(item.find(
                class_="fw-medium d-flex flex-wrap align-items-center gap-1"
            ),"text","")

            #VacanciesDjinni(
            #    title,
            #    description,
            #    f"https://djinni.co{link}",


            #)
