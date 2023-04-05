"""
4.24 Взаимодействие с ползунком
"""
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'

try:
    driver.get(base_url)
    driver.maximize_window()

    action = ActionChains(driver)
    sleep(2)
    price = driver.find_element(By.XPATH, '//input[@class="slider-square"]')
    action.click_and_hold(price).move_by_offset(200, 0).release().perform()
    print("Price +")

finally:
    sleep(5)
    driver.close()
