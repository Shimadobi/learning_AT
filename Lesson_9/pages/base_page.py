from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePage:
    _url = None

    def __init__(self, driver):
        self._driver = driver

    def open(self):
        self._driver.get(self._url)

    def get_element(self, selector_type, selector, timeout=10):
        _element = (selector_type, selector)
        return WebDriverWait(self._driver, timeout).until(
            expected_conditions.visibility_of_element_located(_element))

    def get_elements(self, selector_type, selector, timeout=10):
        _elements = (selector_type, selector)
        return WebDriverWait(self._driver, timeout).until(
            expected_conditions.visibility_of_any_elements_located(_elements))

    def text_is_displayed(self, locator, text, timeout=10):
        _locator = (By.XPATH, locator)
        _text = WebDriverWait(self._driver, timeout).until(
            expected_conditions.text_to_be_present_in_element(_locator, text))
        return True if _text is not None else False
