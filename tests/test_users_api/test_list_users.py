import pytest
import requests
import random


@pytest.mark.smoke
def test_list_users_status_code(url_users_default):
    # Вызов API Get list users
    r = requests.get(f'{url_users_default}/users?page=1')
    # Проверка статус кода ответа
    assert r.status_code == 200


def test_list_users_page(url_users_default):
    # Подготвка данных: выбор страницы
    page = 1
    # Вызов API Get list users
    response = requests.get(f'{url_users_default}/users?page={page}')
    # Проверка статус кода ответа
    assert response.status_code == 200
    # Проверка наличия полей в ответе API согласно документации
    assert response.json()['page'] == page
    assert 'per_page' in response.json()
    assert 'total' in response.json()
    assert 'total_pages' in response.json()
    assert 'data' in response.json()
    assert 'id' in response.json()['data'][0]
    assert 'email' in response.json()['data'][0]
    assert 'first_name' in response.json()['data'][0]
    assert 'last_name' in response.json()['data'][0]
    assert 'avatar' in response.json()['data'][0]


def test_list_users_user(url_users_default):
    # Подготовка данных
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    user_id = random.randint(first_id, last_id)
    # Вызов API Get list users
    response = requests.get(f'{url_users_default}/users/{user_id}')
    # Проверка статус кода ответа
    assert response.status_code == 200
    # Проверка наличия полей в ответе API согласно документации
    assert 'data' in response.json()
    assert response.json()['data']['id'] == user_id
    assert 'email' in response.json()['data']
    assert 'first_name' in response.json()['data']
    assert 'last_name' in response.json()['data']
    assert 'avatar' in response.json()['data']


def test_list_users_negative_not_found_user(url_users_default):
    # Вызов API Get list users
    response = requests.get(f'{url_users_default}/users?page=2')
    # Получение последнего id пользователя из списка
    last_user_id = response.json()['data'][-1]['id']
    # Вызов API Get list users с несуществующим id пользователя
    response_negative = requests.get(f'{url_users_default}/users/{last_user_id+1}')
    # Проверка статус кода ответа
    assert response_negative.status_code == 404


def test_list_users_negative_not_found_page(url_users_default):
    # Вызов API Get list users
    response = requests.get(f'{url_users_default}/users?page=1')
    # Получение общего количества страниц
    page_amount = response.json()['total_pages']
    # Вызов API Get list users с несуществующей страницей
    response_negative = requests.get(f'{url_users_default}/users?page={page_amount+1}')
    # Проверка статус кода ответа
    assert response_negative.status_code == 404


def test_list_users_empty_requests(url_users_default):
    # Вызов API Get list users
    response = requests.get(f'{url_users_default}/users')
    # Проверка статус кода ответа
    assert response.status_code == 400


def test_list_users_negative_string_user(url_users_default):
    # Вызов API Get list users
    response = requests.get(f'{url_users_default}/users/test')
    # Проверка статус кода ответа
    assert response.status_code == 400


def test_list_users_negative_string_page(url_users_default):
    # Вызов API Get list users
    response = requests.get(f'{url_users_default}/users?page=test')
    # Проверка статус кода ответа
    assert response.status_code == 400
