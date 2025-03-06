from typing import TypedDict


class VacanciesScrapType(TypedDict):
    title: str
    description: str
    link: str
    location: str
    company: str
    company_link: str
    company_img: str
    salary: str
