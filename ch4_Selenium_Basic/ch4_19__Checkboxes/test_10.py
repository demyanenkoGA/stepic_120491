"""
4.19 Взаимодействие с Check box
"""
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'

driver.get(base_url)
driver.maximize_window()

sleep(5)

chbx_1 = driver.find_element(By.XPATH, '//input[@value="cb1"]')
chbx_1.click()

sleep(3)

selected_chbx_3 = driver.find_element(By.XPATH, '//input[@value="cb3"][@checked]')
selected_chbx_3.click()

sleep(5)
driver.close()
