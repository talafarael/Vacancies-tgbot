from typing import TypedDict
from bson import ObjectId


class VacanciesObjType(TypedDict):
    _id: ObjectId
    id_category: ObjectId
    id_experience: ObjectId
