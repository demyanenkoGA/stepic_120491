"""
5.5 Тестовое задание по Selenium №4
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Login_page:
    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login, pass_word):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login)
        print(f"Input Login")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(pass_word)
        print(f"Input Password")

        btn_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        btn_login.click()
        print(f"Click Login Button")
