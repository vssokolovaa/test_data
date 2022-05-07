import pytest
import cerberus


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_create_json_status_code(user_id, session, url_json_default):
    response = session.post(url_json_default, json={
        'title': 'test',
        'body': 'test for hw',
        'userId': user_id})
    assert response.ok


@pytest.mark.parametrize("id", [1, 2, 3])
def test_get_json_schema(id, session, url_json_default):
    response = session.get(f'{url_json_default}/{id}')
    schema = {
        "userId": {"type": "number"},
        "id": {"type": "number"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    }
    v = cerberus.Validator()
    assert v.validate(response.json(), schema)


def test_list_json(session, url_json_default):
    response = session.get(f'{url_json_default}')
    assert response.ok


def test_update_json_status_code(session, url_json_default):
    response = session.post(url_json_default, json={
        'id': '1',
        'title': 'test',
        'body': 'test for hw',
        'userId': 5})
    assert response.ok


def test_list_json(session, url_json_default):
    response = session.delete(f'{url_json_default}/1')
    assert response.ok
