import pytest
import requests
import random
from data.constants import user_registration


@pytest.mark.smoke
def test_login_user_status_code(url_users_default):
    # Вызов API Post login
    url = f'{url_users_default}/login'
    response = requests.post(url, json={
        'email': "eve.holt@reqres.in",
        'password': "pistol"
    })
    # Проверка статус кода ответа
    assert response.status_code == 200


def test_login_users_valid_request_all_fields(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/login'
    # В документации указано, что лишь определённые пользователи могут пройти регистрацию и войти в систему.
    # Список почт этих пользователей хранится в файле data/constants.py
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post login
    response = requests.post(url, json={'email': email,
                                        'password': password})
    # Проверка статус кода ответа
    assert response.status_code == 200
    assert 'token' in response.json()


def test_login_user_empty_request(url_users_default):
    # Вызов API Post login
    url = f'{url_users_default}/login'
    response = requests.post(url, json={})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_login_user_only_password(url_users_default):
    # Вызов API Post login
    url = f'{url_users_default}/login'
    response = requests.post(url, json={'password': 'password'})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_login_user_only_email(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/login'
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    # Вызов API Post login
    response = requests.post(url, json={'email': email})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_login_user_third_field(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/login'
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post login
    response = requests.post(url, json={'email': email,
                                        'password': password})
    # Проверка статус кода ответа
    assert response.status_code == 200


def test_login_user_wrong_email_field(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/login'
    n = random.randint(0, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post login
    response = requests.post(url, json={'emaal': email,
                                        'password': password})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing email or username'


def test_login_user_wrong_password_field(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/login'
    n = random.randint(1, len(user_registration)-1)
    email = user_registration[n]
    password = random.random()
    # Вызов API Post login
    response = requests.post(url, json={'passwored': password,
                                        'email': email})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_login_not_exist_user(url_users_default):
    # Подготовка данных
    url = f'{url_users_default}/login'
    email = 'george.bluth'
    password = random.random()
    # Вызов API Post login
    response = requests.post(url, json={'password': password,
                                        'email': email})
    # Проверка статус кода ответа
    assert response.status_code == 400
    assert response.json()['error'] == 'user not found'
