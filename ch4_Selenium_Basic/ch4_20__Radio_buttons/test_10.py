"""
4.20 Взаимодействие с Radio Button
"""
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

base_url = 'https://demoqa.com/radio-button'

driver.get(base_url)
driver.maximize_window()

sleep(3)

rbtn_1 = driver.find_element(By.XPATH, '//input[@value="rd1"]')
rbtn_1.click()
print("Click Radio Button 1")


sleep(5)
driver.close()
