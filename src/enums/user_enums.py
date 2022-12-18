from enum import Enum

from src.baseclasses.pyenum import PyEnam


class Genders(Enum):
    FEMAIL = 'female'
    MALE = 'male'


class Statutes(PyEnam):
    INACTIVE = 'INACTIVE'
    ACTIVE = 'ACTIVE'
    DELETED = 'DELETED'
    BANNED = 'BANNED'


class UserErrors(Enum):
    WRONG_EMAIL = 'Email doesn`t contain @'


print(Statutes.list())
