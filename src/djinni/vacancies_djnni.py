from ..dou.vacancies_dou import VacanciesDou


class VacanciesDjinni(VacanciesDou):
    def __init__(
        self,
        title,
        description,
        link,
        company,
        company_img,
        salary,
        production,
        year_experience,
    ):
        super().__init__(title, description, link)
        self.company = company
        self.company_img = company_img
