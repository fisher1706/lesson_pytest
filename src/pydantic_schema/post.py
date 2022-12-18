from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=10)
    # id: int
    title: str
    # name: str = Field(alias='_name')

    # @validator('id')
    # def check_that_id_is_less_that_two(cls, v):
    #     if v > 10:
    #         raise ValueError('id is not less than two')
    #     else:
    #         return v


# {'id': 1, 'title': 'Post_1', '_name': 'Oleg'}