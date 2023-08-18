from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


"""
1. На странице https://esia-portal1.test.gosuslugi.ru/ найти все элементы по xpath //input и заполнить логин/пароль. 
Не заполнять те поля, которые имеют type="hidden".
"""

option = webdriver.ChromeOptions()
option.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get('https://esia-portal1.test.gosuslugi.ru/')

driver.find_element(By.XPATH, '//input[@id="login"]').send_keys('username')
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys('username')

