import pytest
import requests
from data.datetime_data import DateData


@pytest.mark.smoke
def test_create_users_status_code(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/users'
    name = 'Valeriya'
    job = 'QA'
    # Вызов API Post create user
    response = requests.post(url, json={'name': name,
                                        'job': job}
                             )
    # Проверка статус кода ответа
    assert response.status_code == 201


def test_create_users_valid_request_several_fields(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/users'
    name = 'Valeriya'
    job = 'QA'
    created_at = DateData().get_time_now_string_utc()
    # Вызов API Post create user
    response = requests.post(url, json={'name': name,
                                        'job': job})
    # Проверка статус кода и полей ответа
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job
    assert 'id' in response.json()
    assert response.json()['createdAt'][:16] == created_at[:16]


def test_create_users_valid_request_without_job(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/users'
    name = 'Valeriya'
    created_at = DateData().get_time_now_string_utc()
    # Вызов API Post create user
    response = requests.post(url, json={'name': name})
    # Проверка статус кода и полей ответа
    assert response.status_code == 201
    assert response.json()['name'] == name
    assert 'id' in response.json()
    assert response.json()['createdAt'][:16] == created_at[:16]


def test_create_users_valid_request_without_name(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/users'
    job = 'QA'
    created_at = DateData().get_time_now_string_utc()
    # Вызов API Post create user
    response = requests.post(url, json={'job': job})
    # Проверка статус кода и полей ответа
    assert response.status_code == 201
    assert response.json()['job'] == job
    assert 'id' in response.json()
    assert response.json()['createdAt'][:16] == created_at[:16]


def test_create_users_valid_request_with_unknown_field(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/users'
    last_name = 'Ivanov'
    created_at = DateData().get_time_now_string_utc()
    # Вызов API Post create user
    response = requests.post(url, json={'last_name': last_name})
    # Проверка статус кода и полей ответа
    assert response.status_code == 201
    assert response.json()['last_name'] == last_name
    assert 'id' in response.json()
    assert response.json()['createdAt'][:16] == created_at[:16]


def test_create_users_check_creating_user(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/users'
    name = 'Valeriya'
    job = 'QA'
    # Вызов API Post create user
    create_response = requests.post(url, json={'name': name,
                                               'job': job})
    # Получение идентификатора созданного пользователя
    user_id = create_response.json()['id']
    # Отправка запроса в API Get list users для получения информации по данному пользователю
    get_response = requests.get(f'{url_users_default}/users/{user_id}')
    # Проверка статус кода и ответа метода для создания пользователя
    assert create_response.status_code == 201, 'Пользователь не создан'
    assert get_response.status_code == 200, 'Пользователь не добавлен в систему'
    # Проверка наличия полей в ответе API согласно документации
    assert 'data' in get_response.json()
    assert get_response.json()['data']['id'] == user_id
    assert 'name' in get_response.json()['data']
    assert 'job' in get_response.json()['data']
    assert get_response.json()['data']['name'] == name
    assert get_response.json()['data']['job'] == job


def test_create_users_negative_empty_request(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/users'
    # Вызов API Post create user
    response = requests.post(url, json={})
    # Проверка статус кода ответа
    assert response.status_code == 400


def test_create_users_valid_request_exist_user(url_users_default):
    # Вызов API Get list users
    get_user = requests.get(f'{url_users_default}/users/1')
    id = get_user.json()['data']['id']
    email = get_user.json()['data']['email']
    first_name = get_user.json()['data']['first_name']
    last_name = get_user.json()['data']['last_name']
    avatar = get_user.json()['data']['avatar']
    url = f'{url_users_default}/users'
    # Вызов API Post create user
    response = requests.post(url, json={'id': id,
                                        'email': email,
                                        'first_name': first_name,
                                        'last_name': last_name,
                                        'avatar': avatar})
    # Проверка статус кода ответа
    assert response.status_code == 409

