import requests
import pytest


@pytest.fixture
def url_users_default():
    url_users_default = "https://reqres.in/api"
    return url_users_default


@pytest.fixture
def session():
    sess = requests.Session()
    return sess

@pytest.fixture
def url_brewery_default():
    url_brewery_default = 'https://api.openbrewerydb.org/breweries'
    return url_brewery_default


@pytest.fixture
def url_json_default():
    url_json_default = 'https://jsonplaceholder.typicode.com/posts'
    return url_json_default


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="request_url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="Expected status code"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="Types of methods"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def code_status(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def request_method(request):
    return request.config.getoption("--method")
