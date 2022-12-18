import pytest
from random import randrange
from src.generators.player import Player
from src.generators.film_generators import FilmBuilder

from db import Session
import tables


@pytest.fixture()
def get_player_generator():
    return Player()


@pytest.fixture()
def get_film_generator():
    return FilmBuilder()


@pytest.fixture(autouse=False)
def say_hello():
    print('\nhello')
    return 14


@pytest.fixture()
def get_number():
    return randrange(1, 1000, 5)


def _calculate(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture()
def calculate():
    return _calculate


@pytest.fixture()
def make_number():
    print('\nI am getting number')
    number = randrange(1, 1000, 5)
    yield number
    print(f'\nNumber at home {number}')


@pytest.fixture()
def get_db_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


def delete_test_data(session, table, filter_dats):
    session.query(table).filter(filter_dats).delete()
    session.commit()


def add_method(session, item):
    session.add(item)
    session.commit()


@pytest.fixture()
def get_delete_method():
    return delete_test_data


@pytest.fixture()
def get_add_method():
    return add_method


@pytest.fixture()
def generate_film(get_db_session, get_film_generator, get_add_method, get_delete_method):
    film = tables.Films(**get_film_generator.build())
    get_add_method(get_db_session, film)
    yield film

    get_delete_method(get_db_session, tables.Films, tables.Films.film_id == film.film_id)
