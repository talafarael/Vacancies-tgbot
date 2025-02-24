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
        production,
        year_experience,
        remote_type
    ):
        super().__init__(title, description, link,location,company,company_link,company_img,salary)
        self.production=production
        self.year_experience=year_experience
        self.remote_type=remote_type
