import pytest
import json
import requests

@pytest.mark.parametrize('brewery', ['5128df48-79fc-4f0f-8b52-d06be54d0cec', '9c5a66c8-cc13-416f-a5d9-0a769c87d318'])
def test_brewery_unic_id(brewery):
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries/{brewery}')

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'

    response_json = response.json()

    assert 'id' in response_json


@pytest.mark.parametrize('city', ['San Diego', 'Norman', 'Mount Pleasant'])
def test_sort_by_city(city):
    response = requests.get(f'https://api.openbrewerydb.org/v1/breweries?by_city={city}&per_page=3')

    assert response.status_code == 200

    response_json = response.json()

    for brewery in response_json:
        assert brewery['city'].lower() == city.lower()


def test_get_random_name():
    url = 'https://api.openbrewerydb.org/v1/breweries/random'

    response = requests.request('GET', url)

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'
    assert 'name' in response.text


def test_pagination():
    url_1 = requests.get('https://api.openbrewerydb.org/v1/breweries?page=15&per_page=3')
    url_2 = requests.get('https://api.openbrewerydb.org/v1/breweries?page=25&per_page=3')

    assert url_1.status_code == 200, f'Ожидаемый статус 200, получен{url_1.status_code}'
    assert url_2.status_code == 200, f'Ожидаемый статус 200, получен{url_2.status_code}'

    assert url_1.json() != url_2.json(), f'Данные должны быть разными'


def test_invalid_size():
    url = 'https://api.openbrewerydb.org/v1/breweries/random?size=51'
    response = requests.get(url)

    assert response.status_code == 400, f'Ожидаемый статус 400, получен{response.status_code}'

    response_json = response.json()

    assert response_json['size'][0] == 'The size field must not be greater than 50.'



