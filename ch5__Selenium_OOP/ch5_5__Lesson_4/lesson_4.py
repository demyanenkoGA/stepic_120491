"""
5.5 Тестовое задание по Selenium №4
"""
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from contextlib import suppress
from ch5__Selenium_OOP.ch5_5__Lesson_4.login_page import Login_page

driver = webdriver.Chrome()
base_url = 'https://www.saucedemo.com/'
users_login = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
password_for_all = 'secret_sauce'

try:
    driver.get(base_url)
    driver.maximize_window()

    for user in users_login:
        print(f'Test authentication for "{user}"')
        try:
            login = Login_page(driver)
            login.authorization(user, password_for_all)
            if user == "locked_out_user":
                with suppress(TimeoutException):
                    locked_error = WebDriverWait(driver, 30).until(
                        EC.element_to_be_clickable((By.XPATH, '//div[@class="error-message-container error"]/h3')))
                    value_locked_error = locked_error.text
                    assert value_locked_error == "Epic sadface: Sorry, this user has been locked out."
                    print(f'Authentication error for "{user}". Text: {value_locked_error}\n')
                    driver.get(base_url)
                    continue

            title_cart = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))
            value_title_cart = title_cart.text
            assert value_title_cart == "Products"
            print(f'Authentication for "{user}" Success')

            menu = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@id="react-burger-menu-btn"]')))
            menu.click()
            print(f"Click Menu Button")

            btn_logout = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@id="logout_sidebar_link"]')))
            btn_logout.click()
            print(f'Logout for "{user}" Success\n')
        except TimeoutException:
            print(f'Test error for "{user}"!!!\n')
            driver.get(base_url)
            continue

finally:
    sleep(5)
    driver.close()
