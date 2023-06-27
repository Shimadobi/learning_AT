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


class Data(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str


class Support(BaseModel):
    url: str
    text: str


class GetResourceId(BaseModel):
    data: Data
    support: Support


class TestResource:
    @pytest.mark.parametrize(
        "r_id",
        ["1", "2", "3"],
    )
    def test_get_resource_id(self, get_resource_id, r_id):
        reply = requests.get(get_resource_id + r_id)
        assert reply.status_code == requests.codes.ok
        assert GetResourceId(**reply.json())

    @pytest.mark.parametrize(
        "r_id",
        ["100", "2000", "356573"],
    )
    def test_get_wrong_resource_id(self, get_resource_id, r_id):
        reply = requests.get(get_resource_id + r_id)
        assert reply.status_code == 404
