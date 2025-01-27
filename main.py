from pydantic import BaseModel, Field, ValidationError, validator, root_validator, constr, conint
from typing import List, Dict, Any, Union, Optional
from datetime import datetime
from enum import Enum
import json


class Person(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    age: conint(ge=0, le=130)

class Engineer(Person):
    skills: List[str]
    experiences: List[int]

    @validator('experiences')
    @classmethod
    def check_experiences(cls, v, values):
        if 'Python' in values.get('skills', []) and any(exp < 3 for exp in v):
            raise ValueError('Python engineer must have at least 3 years of experience')
        return v