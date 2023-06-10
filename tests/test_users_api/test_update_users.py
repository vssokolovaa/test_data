import pytest
import requests
import random
from data.datetime_data import DateData


@pytest.mark.smoke
def test_update_users_status_code(url_users_default):
    # Вызов API Put Update users
    url = f'{url_users_default}/users/1'
    response = requests.put(url, json={'name': 'morpheus',
                                       'job': '1job'})
    # Проверка статус кода ответа
    assert response.status_code == 200


def test_update_users_valid_request_without_job(url_users_default):
    # Вызов API Get list users для получения id пользователя
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    user_id = random.randint(first_id, last_id)
    # Подготовка данных
    url = f'{url_users_default}/users/{user_id}'
    name = 'Valeriya'
    updated_at = DateData().get_time_now_string_utc()
    # Вызов API Put Update users
    response = requests.put(url, json={'name': name})
    # Проверка статус кода и полей в ответе
    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['updatedAt'][:16] == updated_at[:16]


def test_update_users_valid_request_without_name(url_users_default):
    # Вызов API Get list users для получения id пользователя
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    user_id = random.randint(first_id, last_id)
    # Подготовка данных
    url = f'{url_users_default}/users/{user_id}'
    job = 'QA'
    updated_at = DateData().get_time_now_string_utc()
    # Вызов API Put Update users
    response = requests.put(url, json={'job': job})
    # Проверка статус кода и полей в ответе
    assert response.status_code == 200
    assert response.json()['job'] == job
    assert response.json()['updatedAt'][:16] == updated_at[:16]


def test_update_users_valid_request(url_users_default):
    # Вызов API Get list users для получения id пользователя
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    id = random.randint(first_id, last_id)
    # Подготовка данных
    url = f'{url_users_default}/users/{id}'
    name = 'Valeriya'
    job = 'QA'
    updated_at = DateData().get_time_now_string_utc()
    # Вызов API Put Update users
    response = requests.put(url, json={'name': name,
                                       'job': job})
    # Проверка полей в ответе и статус кода
    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert response.json()['updatedAt'][:16] == updated_at[:16]


def test_update_users_check_updating_user(url_users_default):
    # Вызов API Get list users для получения id пользователя
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    user_id = random.randint(first_id, last_id)
    # Подготовка данных
    url = f'{url_users_default}/users/{user_id}'
    first_name = 'Valeriya'
    last_name = 'Sokolova'
    updated_at = DateData().get_time_now_string_utc()
    # Вызов API Put Update users
    response = requests.put(url, json={'first_name': first_name,
                                       'last_name': last_name})
    # Проверка полей в ответе и статус кода
    assert response.status_code == 200
    assert response.json()['first_name'] == first_name
    assert response.json()['last_name'] == last_name
    assert response.json()['updatedAt'][:16] == updated_at[:16]
    # Вызов API Get list для проверки обнволения данных в системе
    get_request = requests.get(f'{url_users_default}/users/{user_id}')
    assert get_request.json()['data']['first_name'] == first_name
    assert get_request.json()['data']['last_name'] == last_name
    assert get_request.json()['data']['updatedAt'][:16] == updated_at[:16]


def test_update_users_request_with_unknown_field(url_users_default):
    # Вызов API Get list users для получения id пользователя
    get_first = requests.get(f'{url_users_default}/users?page=1')
    first_id = int(get_first.json()['data'][0]['id'])
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    id = random.randint(first_id, last_id)
    # Подготовка данных
    url = f'{url_users_default}/users/{id}'
    name = 'Valeriya'
    job = 'QA'
    age = 21
    updated_at = DateData().get_time_now_string_utc()
    # Вызов API Put update users
    response = requests.put(url, json={'name': name,
                                       'job': job,
                                       'age': age})
    # Проверка полей в ответе и статус кода
    assert response.status_code == 200
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert response.json()['age'] == age
    assert response.json()['updatedAt'][:16] == updated_at[:16]


def test_update_users_negative_request_exist_data(url_users_default):
    # Вызов API Get list users
    get_user = requests.get(f'{url_users_default}/users/1')
    id = get_user.json()['data']['id']
    email = get_user.json()['data']['email']
    first_name = get_user.json()['data']['first_name']
    last_name = get_user.json()['data']['last_name']
    avatar = get_user.json()['data']['avatar']
    url = f'{url_users_default}/users/1'
    # Подготовка данных
    updated_at = DateData().get_time_now_string_utc()
    # Вызов API Put update users
    response = requests.put(url, json={'id': id,
                                       'email': email,
                                       'first_name': first_name,
                                       'last_name': last_name,
                                       'avatar': avatar})
    # Проверка статус кода ответа
    assert response.status_code == 409


def test_update_users_negative_empty_request(url_users_default):
    # Вызов API Put Update users
    url = f'{url_users_default}/users/4'
    response = requests.put(url, json={})
    # Проверка статус кода ответа
    assert response.status_code == 400


def test_update_users_not_exist_id(url_users_default):
    # Вызов API Get list users
    get_first = requests.get(f'{url_users_default}/users?page=1')
    amount_of_page = get_first.json()['total_pages']
    get_last = requests.get(f'{url_users_default}/users?page={amount_of_page}')
    last_id = int(get_last.json()['data'][-1]['id'])
    # Вызов API Put Update users
    url = f'{url_users_default}/users/{last_id + 1}'
    response = requests.put(url, json={'name': 'Valery'})
    assert response.status_code == 404


def test_update_users_without_id(url_users_default):
    # Вызов API Put Update users
    url = f'{url_users_default}/users'
    response = requests.put(url, json={'name': 'Valery'})
    assert response.status_code == 404


def test_update_users_string_id(url_users_default):
    # Вызов API Put Update users
    url = f'{url_users_default}/users/test'
    response = requests.put(url, json={'name': 'Valery'})
    assert response.status_code == 400
