import pytest
import requests


@pytest.fixture
def get_list_users_url():
    return 'https://reqres.in/api/users'


@pytest.fixture
def post_login_url():
    return 'https://reqres.in/api/login'


@pytest.fixture
def get_resource_id():
    return 'https://reqres.in/api/{resource}/'
