import pytest
import requests
from pydantic import BaseModel

"""
Протестировать API.
Можно взять одно из двух на выбор:
https://dummy.restapiexample.com/
https://reqres.in/

Необходимо написать не менее пяти тестов.
Протестировать как методы GET так и пост POST.
При создании тестов использовать фикстуры.
"""


class PostLogin(BaseModel):
    token: str


class PostLoginFail(BaseModel):
    error: str


class TestLogin:
    def test_post_login(self, post_login_url):
        param_request = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"}
        reply = requests.post(post_login_url, json=param_request)
        assert reply.status_code == requests.codes.ok
        assert PostLogin(**reply.json())

    def test_wrong_post_login(self, post_login_url):
        param_request = {
            "email": "string",
            "password": "pistol"}
        reply = requests.post(post_login_url, json=param_request)
        assert reply.status_code == 400
        assert PostLoginFail(**reply.json())