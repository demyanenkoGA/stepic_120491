"""
4.16 Smoke testing всего бизнес пути
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
print(f"Input Login")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_for_all)
print(f"Input Password")

btn_login = driver.find_element(By.XPATH, '//input[@id="login-button"]')
btn_login.click()
print(f"Click Login Button")


# INFO PRODUCT #1
tested_product = 1
product = lambda number: driver.find_element(By.XPATH, f'(//div[@class="inventory_item"])[{number}]')
product_1 = product(tested_product).find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = product(tested_product).find_element(By.XPATH, '//div[@class="inventory_item_price"]')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = product(tested_product).find_element(By.XPATH, '//button[text()="Add to cart"]')
select_product_1.click()
print("Select Product 1")

not_empty_cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
not_empty_cart.click()
print("Click to Cart")


# INFO IN CART Product 1
cart_product = driver.find_element(By.XPATH, f'(//div[@class="cart_item_label"])[1]')
cart_product_1 = cart_product.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO Cart Product 1 Good")

cart_price_product_1 = cart_product.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("INFO Cart Price Product 1 Good")

btn_checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
btn_checkout.click()
print("Click Checkout")

# Select Client Info
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('Petr')
print("Enter First Name")
last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys('Petrov')
print("Enter Last Name")
zip_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip_code.send_keys('000000')
print("Enter Zip Code")

btn_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
btn_continue.click()
print("Click Continue")

# INFO Finish Product

finish_product = driver.find_element(By.XPATH, f'(//div[@class="cart_item_label"])[1]')
finish_product_1 = finish_product.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO Cart Product 1 Good")

finish_price_product_1 = finish_product.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO Cart Price Product 1 Good")

summary_price = driver.find_element(By.XPATH, f'//div[@class="summary_subtotal_label"]')
value_summary_price = summary_price.text
print(value_summary_price)

item_total = f'Item total: {value_finish_price_product_1}'
print(item_total)
assert value_summary_price == item_total
print("Total summary price corrected")

# now_datetime = datetime.datetime.utcnow().strftime("%Y.%m.%d_%H.%M.%S")
# name_screenshot = f'./screen/SCREENSHOT_{now_datetime}.png'
# driver.save_screenshot(name_screenshot)

sleep(5)
driver.close()
