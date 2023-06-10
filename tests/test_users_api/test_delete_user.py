import pytest
import requests


@pytest.mark.smoke
def test_delete_user_status_code(url_users_default):
    # Вызов API Get list users
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    # Вызов API Delete user
    url = f'{url_users_default}/users/{first_id}'
    response = requests.delete(url)
    # Проверка статус кода ответа
    assert response.status_code == 204


def test_delete_exist_user(url_users_default):
    # Вызов API Get list users
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    # Вызов API Delete user
    url = f'{url_users_default}/users/{first_id}'
    response = requests.delete(url)
    # Проверка статус кода ответа
    assert response.status_code == 204


def test_delete_check_deleting_user(url_users_default):
    # Вызов API Get list users
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    # Вызов API Delete user
    url = f'{url_users_default}/users/{first_id}'
    response = requests.delete(url)
    # Проверка статус кода ответа
    assert response.status_code == 204
    # Вызов API Get list users
    get_response = requests.get(f'{url_users_default}/users/{first_id}')
    assert get_response.status_code == 404


def test_delete_not_exist_user(url_users_default):
    # Вызов API Get list users
    get_first = requests.get(f'{url_users_default}/users?page=1')
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    url = f'{url_users_default}/users/{last_id + 1}'
    # Вызов API Delete user
    response = requests.delete(url)
    assert response.status_code == 404


def test_delete_user_without_id(url_users_default):
    # Вызов API Delete user
    url = f'{url_users_default}/users'
    response = requests.delete(url)
    assert response.status_code == 400


def test_delete_user_string_id(url_users_default):
    # Вызов API Delete user
    url = f'{url_users_default}/users/test'
    response = requests.delete(url)
    assert response.status_code == 400
