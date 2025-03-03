from typing import  TypedDict 
from bson import ObjectId
from src.types.category_obj_type import CategoryType

class VacanciesFullType(TypedDict):
    _id:  ObjectId
    name:str
    id_category:ObjectId
    id_experience:ObjectId
    category:CategoryType
    experience:CategoryType
