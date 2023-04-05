"""
4.22 Взаимодействие с календарем
"""
import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    base_url = 'https://demoqa.com/date-picker'

    driver.get(base_url)
    driver.maximize_window()

    sleep(3)

    field_calendar = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
    # field_calendar.send_keys(Keys.CONTROL + "a")
    # field_calendar.send_keys(Keys.BACKSPACE)
    # sleep(3)
    # field_calendar.send_keys("01/01/1999")
    # sleep(3)
    # field_calendar.send_keys(Keys.RETURN)

    field_calendar.click()
    sleep(2)

    now_datetime = datetime.datetime.utcnow().strftime("%d")
    print(now_datetime)
    date = int(now_datetime) + 1
    locator = '//div[@aria-label="Choose Thursday, April ' + str(date) + 'th, 2023"]'
    print(locator)
    date_17 = driver.find_element(By.XPATH, locator)

    # date_15_any_month = driver.find_element(By.XPATH, '//div[contains(@class, "react-datepicker__day--015")]')
    # date_15_any_month.click()
    # date_27 = driver.find_element(By.XPATH, '//div[@aria-label="Choose Thursday, April 27th, 2023"]')
    # date_27.click()

finally:
    sleep(5)
    driver.close()
