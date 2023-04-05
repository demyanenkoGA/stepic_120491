"""
4.11 Имитация нажатия клавиш на клавиатуре с помощью Selenium
"""


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

base_url = 'https://www.saucedemo.com/'
authorized_url = 'https://www.saucedemo.com/inventory.html'
login_standard_user = 'standard_user'
password_for_all = 'secret_sauce'

driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print(f"Input Login {login_standard_user}")

# sleep(3)
# user_name.send_keys(Keys.BACKSPACE)
# sleep(3)
# user_name.send_keys(Keys.BACKSPACE)
# sleep(3)
# user_name.send_keys("er")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_for_all)
print(f"Input Password {password_for_all}")
password.send_keys(Keys.RETURN)

btn_filter = driver.find_element(By.XPATH, '//select[@class="product_sort_container"]')
btn_filter.click()
print("Click Filter")
sleep(5)
btn_filter.send_keys(Keys.DOWN)
sleep(3)
btn_filter.send_keys(Keys.RETURN)

sleep(10)
driver.close()
