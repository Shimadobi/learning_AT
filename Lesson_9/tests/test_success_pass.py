import time
from Lesson_9.pages.profile_page import ProfilePage
from Lesson_9.pages.auth_page import AuthPage
from selenium.webdriver.common.by import By


class TestSuccessPass:
    def test_success_pass(self, driver):
        auth_page = AuthPage(driver=driver)
        profile_page = ProfilePage(driver=driver)

        auth_page.open()
        time.sleep(2)
        auth_page.fill_login_input('+79653698447')
        auth_page.fill_pwd_input('q~F!qS51+')

        btn = auth_page.get_element(By.XPATH, '//button[contains(text(),"Войти")]')
        btn.click()

        time.sleep(1)
        title = profile_page.get_title()
        assert title == 'The uniform system of authorization and authentication'
