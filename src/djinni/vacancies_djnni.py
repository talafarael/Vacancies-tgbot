from ..dou.vacancies_dou import VacanciesDou


class VacanciesDjinni(VacanciesDou):
    def __init__(
        self,
        title,
        description,
        link,
        location,
        company,
        company_img,
        company_link,
        salary,
    ):
        super().__init__(title, description, link,location,company,company_link,company_img,salary)
      
