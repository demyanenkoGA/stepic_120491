"""
5.1 Создание класса и метода
"""
from selenium import webdriver
from time import sleep


class Test_1():
    def test_select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://demoqa.com/dynamic-properties'
        driver.get(base_url)
        driver.maximize_window()
        sleep(5)


test = Test_1()
test.test_select_product()
