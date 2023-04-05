"""
4.15 Взаимодействие со скрытыми элементами
"""
import datetime

from selenium import webdriver
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

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_for_all)
print(f"Input Password {password_for_all}")

btn_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
btn_login.click()
print(f"Click Login Button")

menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
menu.click()
print(f"Click Menu Button")
sleep(3)

link_about = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
link_about.click()
print(f"Click Link Button")

btn_signin = driver.find_element(By.XPATH, '//button[text()="Sign in"]')

now_datetime = datetime.datetime.utcnow().strftime("%Y.%m.%d_%H.%M.%S")
name_screenshot = f'./screen/SCREENSHOT_{now_datetime}.png'
driver.save_screenshot(name_screenshot)

sleep(5)
driver.close()
