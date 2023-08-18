from selenium.webdriver.common.by import By
from Lesson_9.pages.base_page import BasePage


class AuthPage(BasePage):
    _url = 'https://esia-portal1.test.gosuslugi.ru/'

    _login_input = (By.ID, 'login')
    _pwd_input = (By.ID, 'password')

    def fill_login_input(self, login):
        self._driver.find_element(*self._login_input).send_keys(login)

    def fill_pwd_input(self, pwd):
        self._driver.find_element(*self._pwd_input).send_keys(pwd)
