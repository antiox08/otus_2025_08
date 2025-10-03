import json
import requests
import pytest


def test_get_random_image():
    url = 'https://dog.ceo/api/breeds/image/random'

    response = requests.request('GET', url)

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'
    assert 'message' in response.text


@pytest.mark.parametrize('value', [1, 3, 5])
def test_dog_value(value):
    response = requests.get(f'https://dog.ceo/api/breed/hound/images/random/{value}')

    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json['message']) == value


@pytest.mark.parametrize('breed', ['affenpinscher', 'african'])
def test_dog_breed(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

    response_json = response.json()

    assert response.status_code == 200
    assert response_json['status'] == 'success'
    assert response_json['message'].startswith('https://images.dog.ceo/breeds/'), f'должно приходить изображение, а пришло{response_json}'


def test_get_list_all():
    url = 'https://dog.ceo/api/breeds/list/all'

    response = requests.request('GET', url)

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'
    response_json = response.json()
    assert response_json['status'] == 'success'
    assert len(response_json['message']) > 0
    assert 'affenpinscher' in response_json['message']


@pytest.mark.parametrize('breed', ['dog', 'cat'])
def test_invalid_dog_breed(breed):
    response = requests.get(f'https://dog.ceo/api/breed/{breed}/images/random')

    response_json = response.json()

    assert response.status_code == 404, f'Ожидаемый статус 404, получен{response.status_code}'
    assert response_json['status'] == 'error'
