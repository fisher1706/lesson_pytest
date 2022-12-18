import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA
from src.pydantic_schema.post import Post


def test_getting_posts():
    resp = requests.get(url=SERVICE_URL)

    response = Response(resp)
    # response.assert_status_code(200).validate_json(POST_SCHEMA)
    response.assert_status_code(200).validate_pydantic(Post)


def test_somrthing(get_number):
    assert 1 == 1
    print(f'\n{get_number}')
