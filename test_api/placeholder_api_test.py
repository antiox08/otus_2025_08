import pytest
import json
import requests

JSON_URL = 'https://jsonplaceholder.typicode.com'
@pytest.mark.parametrize('num', [1, 3, 5])
def test_post_num(num):
    response = requests.request('GET', f'{JSON_URL}/posts/{num}')

    response_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'
    assert response_json['id'] == num

@pytest.mark.parametrize('postid', [7, 9, 11])
def test_postid(postid):
    response = requests.request('GET', f'{JSON_URL}/comments?postId={postid}')

    response_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'
    assert len(response_json) > 0, f'Длина должна быть больше 0 {response.status_code}'

def test_post_field():
    response = requests.request('GET', f'{JSON_URL}/posts')

    response_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'

    for post in response_json:
        assert 'userId' in post, 'userId should be in posts'
        assert 'id' in post, 'id should be in posts'
        assert 'title' in post, 'title should be in posts'
        assert 'body' in post, 'body should be in posts'

def test_users_field():
    response = requests.request('GET', f'{JSON_URL}/users')

    response_json = response.json()

    assert response.status_code == 200, f'Ожидаемый статус 200, получен{response.status_code}'

    for user in response_json:
        assert isinstance(user['name'], str)
        assert isinstance(user['username'], str)

def test_invalid_url():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/usersd')

    assert response.status_code == 404, f'Ожидаемый статус 404, получен{response.status_code}'