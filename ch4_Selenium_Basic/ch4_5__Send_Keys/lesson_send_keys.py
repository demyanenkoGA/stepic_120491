"""
4.5 Заполнение полей с помощью метода send_keys
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")
sleep(60)
driver.close()
