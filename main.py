import requests
import re
import urllib
from bs4 import BeautifulSoup
url = "https://djinni.co/jobs/?primary_keyword=Node.js"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://jobs.dou.ua/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

response = requests.get(url, headers=headers, proxies=urllib.request.getproxies()) 
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")
pattern = re.compile(r'^job-item-\d+$')
for item in soup.find_all('li',id=pattern):
    print(item.find(class_="job-item__title-link").text)
    items =  getattr(soup.find(class_="job-item__title-link"),"href",None)
    print(items)

    print(item.find(class_="fw-medium d-flex flex-wrap align-items-center gap-1").text)
    print(item.find(class_="js-truncated-text").text)

    print("_____________________________________________________________________________________")
else:
    print("")
