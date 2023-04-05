"""
4.19 Взаимодействие с Check box
"""
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

base_url = 'https://demoqa.com/checkbox'

driver.get(base_url)
driver.maximize_window()

chbx = driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]')
chbx.click()

selected_chbx = driver.find_element(By.XPATH, '//div[@id="result"]')

list_tree = driver.find_element(By.XPATH, '//button[@title="Toggle"]')
list_tree.click()

list_second_subtree = driver.find_element(By.XPATH, '(//li[contains(@class, "rct-node-parent")])[2]')


sleep(5)
driver.close()
