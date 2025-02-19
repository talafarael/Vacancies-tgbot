import requests
from bs4 import BeautifulSoup
url = "https://jobs.dou.ua/vacancies/feeds"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://jobs.dou.ua/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}
response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.content, "xml")

# Перевіряємо вміст
print(soup.prettify())

# Спробуємо знайти потрібний елемент
job_lit_div = soup.find("div", {"class": "job-lit"})

if job_lit_div:
    print(job_lit_div.prettify())  # Виводимо красиво форматований HTML/XML
else:
    print("Div with class 'job-lit' not found!")
