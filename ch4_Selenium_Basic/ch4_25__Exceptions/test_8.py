"""
4.25 Отработка исключений
"""
from selenium import webdriver
from selenium.common import NoSuchElementException

from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

# base_url = 'https://demoqa.com/dynamic-properties'
# driver.get(base_url)
# driver.maximize_window()
#
# sleep(3)
# try:
#     visible_btn = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_btn.click()
#     print("Успех")
# except NoSuchElementException:
#     print("NoSuchElementException")
#     sleep(5)
#     visible_btn = driver.find_element(By.XPATH, '//button[@id="visibleAfter"]')
#     visible_btn.click()
# finally:
#     sleep(5)
#     driver.close()


base_url = 'https://demoqa.com/radio-button'
driver.get(base_url)
driver.maximize_window()

sleep(3)
try:
    yes_chbx = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    yes_chbx.click()
    msg = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_msg = msg.text
    print(value_msg)
    assert value_msg == "No"
except AssertionError:
    driver.refresh()
    yes_chbx = driver.find_element(By.XPATH, '//label[@for="yesRadio"]')
    yes_chbx.click()
    msg = driver.find_element(By.XPATH, '//span[@class="text-success"]')
    value_msg = msg.text
    print(value_msg)
    assert value_msg == "Yes"
finally:
    print("Test Over")
    sleep(5)
    driver.close()
