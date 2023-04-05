"""
4.10 Обновление страницы
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
authorized_url = 'https://www.saucedemo.com/inventory.html'
login_standard_user = 'standard_user'
password_for_all = 'secret_sauce2'

driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print(f"Input Login {login_standard_user}")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_for_all)
print(f"Input Password {password_for_all}")

btn_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
btn_login.click()
print(f"Click Login Button")

warning_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
value_warning_text = warning_text.text
print(value_warning_text)
assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
print('Good test')

driver.refresh()

sleep(5)
driver.close()
