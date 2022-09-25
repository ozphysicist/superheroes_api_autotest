from typing import Optional

from pydantic import BaseModel


class Superhero(BaseModel):
    birthDate: str
    city: str
    fullName: str
    gender: str
    id: int
    mainSkill: str
    phone: Optional[str] = None
