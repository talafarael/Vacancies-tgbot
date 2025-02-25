from abc import ABC, abstractmethod                                                                    
from typing import List, Tuple                                                                                
                                                                                                       
                                                                                                       
class GetCategorySource(ABC):                                                                      
    @abstractmethod                                                                                    
    async def get_category(self)-> Tuple[List[dict],List[dict]] :                          
        pass                                                                                           
                                                                                                       

