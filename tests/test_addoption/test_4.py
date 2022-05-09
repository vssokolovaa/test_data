def test_url_status(base_url, session, code_status):
    response = session.get(base_url)
    assert response.status_code == code_status
