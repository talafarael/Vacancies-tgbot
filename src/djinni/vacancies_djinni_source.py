from abc import ABC, abstractmethod                                    
from typing import List

from src.djinni.vacancies_djnni import VacanciesDjinni                                                
                                                                       
class VacanciesDjinniSource(ABC):                                         
    @abstractmethod                                                    
    async def get_djinni_vacancies(self, url: str) -> List[VacanciesDjinni]: 
        pass                                                           

