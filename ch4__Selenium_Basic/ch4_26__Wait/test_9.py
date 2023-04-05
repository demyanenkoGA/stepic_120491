"""
4.26 Явное и Неявное ожидание
"""
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
# driver.maximize_window()
# driver.implicitly_wait(10)


try:
    # print("Start test")
    # visible_btn = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
    # visible_btn.click()
    # print("Finish Test")

    print("Start test")
    visible_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="visibleAfter"]')))
    visible_btn.click()
    print("Finish Test")
finally:
    sleep(5)
    driver.close()
