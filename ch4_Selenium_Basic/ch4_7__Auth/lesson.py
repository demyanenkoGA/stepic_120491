"""
4.7 Авторизация на сайте
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@data-test="username"]')
user_name.send_keys("standard_user")

password = driver.find_element(By.CSS_SELECTOR, '#password')  # CSS_SELECTOR
password.send_keys("secret_sauce")

btn_login = driver.find_element(By.ID, "login-button")
btn_login.click()

sleep(60)
driver.close()
