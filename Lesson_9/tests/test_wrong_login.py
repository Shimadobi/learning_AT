import time
from Lesson_9.pages.base_page import BasePage
from Lesson_9.pages.auth_page import AuthPage
from selenium.webdriver.common.by import By


class TestWrongLogin:
    def test_wrong_login(self, driver):
        auth_page = AuthPage(driver=driver)
        auth_page.open()
        time.sleep(2)
        auth_page.fill_login_input('ddd')
        auth_page.fill_pwd_input('1234')

        base_page = BasePage(driver=driver)
        login_btn = base_page.get_element(By.XPATH,
                                          '/html/body/esia-root/div/esia-login/div/div[1]/form/div[4]/button',
                                          timeout=10)
        driver.execute_script('arguments[0].click();', login_btn)
        assert base_page.text_is_displayed('/html/body/esia-root/div/esia-login/div/div[1]/form/div[1]/div',
                                           'Введите логин', timeout=10)
