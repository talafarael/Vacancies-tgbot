from typing import TypedDict
from bson import ObjectId


class CategoryType(TypedDict):
    _id: ObjectId
    id_category: ObjectId
    id_experience: ObjectId
