from typing import  List, TypedDict
from bson import ObjectId 
class CategoryType(TypedDict):
    _id:  ObjectId
    dou: int
    djinni: int
    name: str
    users: List[str]
