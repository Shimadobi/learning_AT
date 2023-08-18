from Lesson_9.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class ProfilePage(BasePage):
    _url = 'https://esia-portal1.test.gosuslugi.ru/profile/user/personal'

    def get_title(self, timeout=10):
        title_element = WebDriverWait(self._driver, timeout).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//title')))
        return title_element.get_attribute('textContent')
