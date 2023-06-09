"""
5.2 Smoke testing всего бизнес пути + ООП
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_1():
    def test_select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        sleep(5)

        print("Start Test")

        login_standard_user = 'standard_user'
        password_for_all = 'secret_sauce'

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        user_name.send_keys(login_standard_user)
        print(f"Input Login")

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password.send_keys(password_for_all)
        print(f"Input Password")

        btn_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        btn_login.click()
        print(f"Click Login Button")

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')))
        select_product.click()
        print(f"Click Select Product")

        not_empty_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="shopping_cart_badge"]')))
        not_empty_cart.click()
        print("Enter shopping cart")

        title_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
        value_title_cart = title_cart.text
        assert value_title_cart == "Your Cart"
        print("Test Success")

        sleep(5)

test = Test_1()
test.test_select_product()
