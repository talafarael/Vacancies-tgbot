from abc import ABC, abstractmethod                                                                    
from typing import List

from src.types.collection import CollectionName
from src.types.category_obj_type import CategoryType                                                                                
                                                                                                      
                                                                                                       
class GetCategorySource(ABC):                                                                      
    @abstractmethod                                                                                     
    async def get_one(self,id:str,name_collection:CollectionName )-> CategoryType :                                  
        pass                                                                                            

    @abstractmethod                                                                                    
    async def get(self,name_collection:CollectionName )-> List[CategoryType] :                          
        pass                                                                                           
    @abstractmethod
    async def get_experience(self)->List[dict]:
        pass

                                                                                                       
