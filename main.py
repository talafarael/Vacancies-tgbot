import requests
import xml.etree.ElementTree as ET

url = "https://jobs.dou.ua/vacancies/feeds"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://jobs.dou.ua/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}


class Vacancies:
    def __init__(self, title, descritpion, link):
        self.title = title
        self.description = descritpion
        self.link = link


try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP request errors
    root = ET.fromstring(response.content)

    for item in root.findall(".//item"):
        vacancies = Vacancies(
            getattr(item.find("title"), "text", None),
            getattr(item.find("description"), "text", None),
            getattr(item.find("link"), "text", None),
        )
        print(vacancies.link)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
