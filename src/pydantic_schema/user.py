from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statutes, UserErrors


class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statutes

    @validator('email')
    def check_that_dog_is_presented_in_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)

