# import requests
# import pytest
#
# r = requests.get('https://dog.ceo/api/breeds/image/random')
#
#
# @pytest.mark.parametrize("code_status", [200])
# def test_dog_status_code(code_status):
#     assert r.status_code == code_status
#
#
# def test_dog_status_json():
#     response = r.json()
#     assert response["status"] == "success"
#
#
# def test_dog_type_of_file():
#     response = r.json()
#     response_body = response.get("message")
#     b = ".jpg"
#     if b in response_body:
#         assert True
#     else:
#         assert False
#
#
# def test_dog_url_in_message():
#     response = r.json()
#     response_body = response.get("message")
#     b = "https://images.dog.ceo/breeds/"
#     if b in response_body:
#         assert True
#     else:
#         assert False
#
#
# @pytest.mark.parametrize("code_status_image", [200])
# def test_dog_code_status_image(code_status_image):
#     response = r.json()
#     response_body = response.get("message")
#     image = requests.get(response_body)
#     assert image.status_code == code_status_image
