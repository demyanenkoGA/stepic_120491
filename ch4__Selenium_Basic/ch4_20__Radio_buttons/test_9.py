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

rbtnYes = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
rbtnYes.click()


sleep(5)
driver.close()
