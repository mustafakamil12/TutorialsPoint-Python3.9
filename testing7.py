import pytest
import requests
import json

def test_valid_login():
    url = "https://reqres.in/api/login/"
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(url,data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QpwL5tke4Pnpja7X4"