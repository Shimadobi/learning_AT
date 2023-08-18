import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', name='driver')
def get_driver():
    option = webdriver.ChromeOptions()
    option.add_argument("start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
