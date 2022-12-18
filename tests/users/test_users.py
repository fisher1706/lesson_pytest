import requests
from configuration import SERVICE_URL_NEW
from src.baseclasses.response import ResponseNew
from src.pydantic_schema.user import User
import pytest
from src.generators.player_localization import PlayerLocalization
from src.enums.user_enums import Statutes
import tables


def test_getting_users_list(make_number):
    resp = requests.get(SERVICE_URL_NEW)

    # """all information about response"""
    # print(resp.__getstate__())

    test_object = ResponseNew(resp)
    test_object.assert_status_code(200).validate(User)
    x = test_object.get_parsed_object()
    print(f'\nx: {x}')
    print(f'\nemail: {x.email}')
    print(f'\njson: {x.schema_json()}')

    print(f'{make_number}')
    # print(test_object)


def test_getting_users_fixture(get_users, get_number, calculate):
    ResponseNew(get_users).assert_status_code(200).validate(User)
    print(f'\n{get_number}')

    print(f'\n{calculate}')
    print(f'\n{calculate(1, 1)}')


@pytest.mark.skip('ZAPEL')
def test_another():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize('first_val, second_val, result', [
    (1, 2, 3),
    (3, 4, 7)
])
def test_calculatuion(first_val, second_val, result, calculate):
    assert calculate(first_val, second_val) == result

# @pytest.mark.parametrize('status', [
#     'ACTIVE',
#     'BANNED',
#     'DELETED',
#     'INACTIVE'
# ])
#
# @pytest.mark.parametrize('status', [
#     *Statutes.list()
# ])

@pytest.mark.parametrize('status', Statutes.list())
def test_somthing_1(status, get_player_generator):
    print(get_player_generator.set_status(status).build())


@pytest.mark.parametrize('balance_value', [
    '100',
    '0',
    '-10',
    'zapel'
])
def test_somthing_2(balance_value, get_player_generator):
    print(get_player_generator.set_balance(balance_value).build())


@pytest.mark.parametrize('delete_key', [
    'account_status',
    'balance',
    'localize',
    'avatar'
])
def test_somthing_3(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    print(delete_key)
    print(object_to_send)


def test_somthing_4(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        'localize', PlayerLocalization('fr_FR').set_number(15).build()
    ).build()
    print(object_to_send)


def test_somthing_5(get_player_generator):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', 'fr', 'is', 'the', 'best', 'lang'], PlayerLocalization('fr_FR').set_number(15).build()
    ).build()
    print(object_to_send)


@pytest.mark.parametrize('localizations', [
    'rf', 'de', 'ch'
])
def test_somthing_6(get_player_generator, localizations):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization('fr_FR').set_number(15).build()
    ).build()
    print(object_to_send)


@pytest.mark.parametrize('localizations, loc', [
    ('fr', 'fr_FR')
])
def test_somthing_7(get_player_generator, localizations, loc):
    object_to_send = get_player_generator.update_inner_value(
        ['localize', localizations],
        PlayerLocalization(loc).set_number(15).build()
    ).build()
    print(object_to_send)


def test_get_data_films(get_db_session):
    data = get_db_session.query(tables.Films).first()
    print(data.film_id)


def test_try_to_delete_someting(get_delete_method, get_db_session):
    get_delete_method(get_db_session, tables.Films, (tables.Films.film_id == 3))


def test_try_to_add_testdata_first(get_db_session, get_add_method):
    new_film = {
        'title': 'The Zappel',
        'status': 'John R. R. Zapel',
        'is_premiere': True
    }

    film = tables.Films(**new_film)
    get_add_method(get_db_session, film)
    print(film.film_id)


def test_try_to_add_testdata_second(get_db_session, get_add_method, get_film_generator):
    film = tables.Films(**get_film_generator.build())
    get_add_method(get_db_session, film)
    print(film.film_id)


def test_try_to_add_testdata_third(generate_film):
    print(generate_film.film_id)
