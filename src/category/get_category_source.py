from abc import ABC, abstractmethod                                                                    
from typing import List                                                                                
                                                                                                       
                                                                                                       
class GetCategorySource(ABC):                                                                      
    @abstractmethod                                                                                    
    async def get_category(self)-> List[dict] :                          
        pass                                                                                           
    @abstractmethod
    async def get_experience(self)->List[dict]:
        pass

                                                                                                       

