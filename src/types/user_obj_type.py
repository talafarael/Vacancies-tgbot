from typing import  List, TypedDict        
from bson import ObjectId            
class UserType(TypedDict):       
    _id:  ObjectId                   
    chat_id:str
    user_id:str
    name:str
    vacancies:List[ObjectId]

