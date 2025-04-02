from typing import TypedDict
from vacancy_types.job_requirements_enum import (
    Editorial,
    Employment,
    Experience,
    Language,
    Region,
    TypeProdcut,
)


class JobRequirements(TypedDict):
    language: Language | None
    experience: Experience | None
    employment: Employment | None
    region: Region | None
    editorial: Editorial | None
    type_product: TypeProdcut | None
