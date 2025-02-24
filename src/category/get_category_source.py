from abc import ABC, abstractmethod                                                                    
from typing import List                                                                                
                                                                                                       
from src.djinni.vacancies_djnni import VacanciesDjinni                                                 
                                                                                                       
class GetCategorySource(ABC):                                                                      
    @abstractmethod                                                                                    
    async def get_category(self, cluster)-> dict(langauge:str,year:str):                          

        pass                                                                                           
                                                                                                       

