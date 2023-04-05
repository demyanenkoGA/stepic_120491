"""
4.21 Двойной клик и клик правой клавишей мыши
"""
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

base_url = 'https://demoqa.com/buttons'

driver.get(base_url)
driver.maximize_window()

sleep(3)

action = ActionChains(driver)

elem_for_double_click = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
action.double_click(elem_for_double_click).perform()
msg_double_click = driver.find_element(By.XPATH, '//p[@id="doubleClickMessage"]')
print("Успешный двойной клик ЛКМ")

elem_for_right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
action.context_click(elem_for_right_click).perform()
msg_right_click = driver.find_element(By.XPATH, '//p[@id="rightClickMessage"]')
print("Успешный клик ПКМ")

sleep(5)
driver.close()
