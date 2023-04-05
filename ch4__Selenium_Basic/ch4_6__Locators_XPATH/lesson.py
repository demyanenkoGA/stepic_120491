"""
4.6 Поиск локаторов. Что такое XPATH
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com/')
driver.maximize_window()

# user_name = driver.find_element(By.ID, "user-name")  # ID
# user_name = driver.find_element(By.NAME, "user-name")  # NAME
# user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # XPATH
# user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')  # XPATH with ID
user_name = driver.find_element(By.XPATH, '//input[@data-test="username"]')  # XPATH with data-test

user_name.send_keys("standard_user")
sleep(60)
driver.close()


"""
ID
NAME
CLASS_NAME
XPATH
LINK_TEXT
PARTIAL_LINK_TEXT
TAG_NAME
CSS_SELECTOR
"""