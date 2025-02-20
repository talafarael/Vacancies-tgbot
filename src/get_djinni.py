import requests
import re
import urllib
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://jobs.dou.ua/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}
async def get_djinni(url:str):
    try:
        response = requests.get(url, headers=headers, proxies=urllib.request.getproxies())
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return

    soup = BeautifulSoup(response.content, "html.parser")
    pattern = re.compile(r'^job-item-\d+$')

    for item in soup.find_all('li', id=pattern):
        title = item.find(class_="job-item__title-link")
        company = item.find(class_="fw-medium d-flex flex-wrap align-items-center gap-1")
        description = item.find(class_="js-truncated-text")

        print(title.text.strip() )
        print(company.text.strip() )
        print(description.text.strip())

