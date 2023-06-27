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
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class GetListUsers(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[Data]
    support: Support


@pytest.mark.parametrize(
    "page,per_page",
    [(3, 1), (2, 2), (1, 12)],
)
def test_get_list_users(get_list_users_url, page, per_page):
    param_request = {"page": page, "per_page": per_page}
    reply = requests.get(get_list_users_url, params=param_request)
    assert reply.status_code == requests.codes.ok
    assert GetListUsers(**reply.json())
