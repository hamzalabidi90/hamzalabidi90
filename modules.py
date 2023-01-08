from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid4, UUID
from enum import Enum

class Gender(str, Enum):
    male= "Male"
    female= "Female"

class Role(str, Enum):
    admin= "Admin"
    user= "User"
    
class User(BaseModel):
    id: Optional[UUID]= uuid4
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    role: List[Role]
