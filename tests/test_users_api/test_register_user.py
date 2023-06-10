import pytest
import requests
import random
from data.constants import user_registration


@pytest.mark.smoke
def test_register_user_status_code(url_users_default):
    # Вызов API Post register users
    url = f'{url_users_default}/register'
    response = requests.post(url, json={
        'email': "eve.holt@reqres.in",
        'password': "pistol"
    })
    # Проверка статус кода ответа
    assert response.status_code == 200


def test_register_users_valid_request_all_fields(url_users_default):
    # Вызов API Get list users
    url = f'{url_users_default}/register'
    # В документации указано, что лишь определённые пользователи могут пройти регистрацию.
    # Список почт этих пользователей хранится в файле data/constants.py
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post register users
    response = requests.post(url, json={'email': email,
                                        'password': password})
    # Проверка статус кода ответа
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'token' in response.json()


def test_register_users_check_login_user(url_users_default):
    # Вызов API Get list users
    url = f'{url_users_default}/register'
    # В документации указано, что лишь определённые пользователи могут пройти регистрацию.
    # Список почт этих пользователей хранится в файле data/constants.py
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post register users
    response = requests.post(url, json={'email': email,
                                        'password': password})
    # Проверка статус кода ответа
    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'token' in response.json()
    url_login = f'{url_users_default}/login'
    response_login = requests.post(url_login, json={'email': email,
                                        'password': password})
    assert response_login.status_code == 200
    assert 'token' in response_login.json()


def test_register_user_empty_request(url_users_default):
    # Вызов API Post register users
    url = f'{url_users_default}/register'
    response = requests.post(url, json={})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_register_user_only_password(url_users_default):
    # Вызов API Post register users
    url = f'{url_users_default}/register'
    response = requests.post(url, json={'password': 'password'})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_register_user_only_email(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/register'
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    # Вызов API Post register users
    response = requests.post(url, json={'email': email})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_register_user_third_field(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/register'
    n = random.randint(0, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post register users
    response = requests.post(url, json={'email': email,
                                        'password': password,
                                        'kl': 'qwe'})
    # Проверка статус кода ответа
    assert response.status_code == 400


def test_register_user_wrong_email_field(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/register'
    n = random.randint(0, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post register users
    response = requests.post(url, json={'emaal': email,
                                        'password': password})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_register_user_wrong_password_field(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/register'
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post register users
    response = requests.post(url, json={'passwored': password,
                                        'email': email})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_register_wrong_user(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/register'
    email = 'george.bluth'
    password = random.random()
    # Вызов API Post register users
    response = requests.post(url, json={'password': password,
                                        'email': email})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Note: Only defined users succeed registration'
