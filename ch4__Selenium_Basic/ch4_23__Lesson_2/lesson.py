"""
4.23 Тестовое задание по Selenium №2

1.открыть календарь на сайте demoqa.com

2.Используя библиотеку datetime, создать дату, которая на 10 дней (+10 дней) позже текущей, и ввести ее в поле даты. При выполнении задания НЕЛЬЗЯ использовать локаторы дат, только библиотеку datetime

3. Не забывайте добавлять PRINT и КОММЕНТАРИИ для лучшей читаемости кода

"""
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/date-picker'

try:
    driver.get(base_url)
    driver.maximize_window()
    sleep(2)

    field_calendar = driver.find_element(By.XPATH, '//input[@id="datePickerMonthYearInput"]')
    value_current_date = field_calendar.get_attribute('value')
    field_calendar.click()
    sleep(2)

    date_after_10days = datetime.datetime.utcnow() + datetime.timedelta(days=10)  # Получаем текущую дату + 10 дней
    value_date_after_10days = date_after_10days.strftime("%m/%d/%Y")
    print(f'Текущая дата + 10 дней будет: {date_after_10days.strftime("%m/%d/%Y")}')

    locator = f'//div[@aria-label="Choose {date_after_10days.strftime("%A")}, {date_after_10days.strftime("%B")} {date_after_10days.strftime("%d")}th, {date_after_10days.strftime("%Y")}"]'
    print(locator)

    any_date_after_10_days = driver.find_element(By.XPATH, locator)
    any_date_after_10_days.click()

    value_selected_date = field_calendar.get_attribute('value')
    assert value_selected_date == value_date_after_10days
    print(f'Текущая дата: {value_current_date}. Успешно выбрана дата {value_selected_date}')

finally:
    sleep(5)
    driver.close()
