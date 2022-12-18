from enum import Enum


class PyEnam(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
