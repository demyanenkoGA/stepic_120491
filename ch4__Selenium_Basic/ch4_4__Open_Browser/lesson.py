from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome()

# driver.get('https://www.saucedemo.com/')
# driver.maximize_window()
# sleep(60)
# driver.close()


driver_f = webdriver.Firefox()
driver_f.get('https://www.saucedemo.com/')
driver_f.maximize_window()
#sleep(60)
#driver_f.close()
