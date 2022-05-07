import requests
import pytest


def test_brewery_status_code(url_brewery_default):
    r = requests.get(url_brewery_default)
    assert r.status_code == 200


@pytest.mark.parametrize("dog_filter", ["dog", "cat"])
def test_search_brewery_dog(dog_filter, url_brewery_default, session):
    r = 'https://api.openbrewerydb.org/breweries/search'
    parameter = {'query': dog_filter}
    search = session.get(r, params=parameter)
    response = search.text
    if dog_filter in response:
        assert True
    else:
        assert False


def test_get_brewery():
    brewery = requests.get('https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati')
    response = brewery.text
    b = "madtree-brewing-cincinnati"
    if b in response:
        assert True
    else:
        assert False


def test_brewery_by_city():
    by_city = requests.get('https://api.openbrewerydb.org/breweries?by_city=san_diego')
    response = by_city.text
    substriting_city = "San Diego"
    substriting_name = "name"
    assert response.count(substriting_name) == response.count(substriting_city)


@pytest.mark.parametrize("page_size", [49, 50])
def test_brewery_per_page(page_size, session, url_brewery_default):
    parameter = {'per_page': page_size}
    r = session.get(url_brewery_default, params=parameter)
    assert len(r.json()) == page_size


@pytest.mark.parametrize("page_size", [51, 52])
def test_brewery_per_page(page_size, session, url_brewery_default):
    parameter = {'per_page': page_size}
    r = session.get(url_brewery_default, params=parameter)
    assert len(r.json()) == 50
