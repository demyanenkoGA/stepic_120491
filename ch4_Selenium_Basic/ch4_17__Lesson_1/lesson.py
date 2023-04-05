"""
4.17 Тестовое задание по Selenium №1

1.Авторизоваться на сайте

2.Выбрать 2 товара

3.Сохранить в переменные названия и цены товаров

4.Пройти весь БП, на моменте оплаты товара сверить сохраненные значения, а так же что
система правильно посчитала сумму товаров (отдельно считаем сумм товаров и проверяем
с тем что говорит нам система)
"""

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

base_url = 'https://www.saucedemo.com/'
authorized_url = 'https://www.saucedemo.com/inventory.html'
login_standard_user = 'standard_user'
password_for_all = 'secret_sauce'

# Инициализация драйвера Chrome
driver = webdriver.Chrome()

# Переходим на https://www.saucedemo.com/
driver.get(base_url)
driver.maximize_window()
print(f"Переходим на {base_url}")

user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
user_name.send_keys(login_standard_user)
print(f"Ввод логина")

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys(password_for_all)
print(f"Ввод пароля и Enter")
password.send_keys(Keys.RETURN)

get_url = driver.current_url

assert get_url == authorized_url
print("Успешная авторизация\n")


# Информация по первому товару
product_1 = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[1]')
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_product_1 = driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[1]//button[text()="Add to cart"]')
select_product_1.click()
print("Выбран первый товар")


# Информация по второму товару
product_2 = driver.find_element(By.XPATH, '//a[@id="item_0_title_link"]')
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, '(//div[@class="inventory_item_price"])[2]')
value_price_product_2 = price_product_2.text
print(value_price_product_2)

select_product_2 = driver.find_element(By.XPATH, '(//div[@class="inventory_item"])[2]//button[text()="Add to cart"]')
select_product_2.click()
print("Выбран второй товар\n")


# Переход в корзину
not_empty_cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
not_empty_cart.click()
print("Переход в корзину")

# Проверяем первый товар в корзине
cart_product_1 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_name"]')
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1, f"{value_product_1} != {value_cart_product_1}"
print("Информация по первому товару успешно проверена\n")

cart_price_product_1 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_price"]')
value_cart_price_product_1 = cart_price_product_1.text
print(value_cart_price_product_1)
assert value_price_product_1 == value_cart_price_product_1
print("Информация по цене первого товара успешно проверена\n")

# Проверяем второй товар в корзине
cart_product_2 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[2]//div[@class="inventory_item_name"]')
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2, f"{value_product_2} != {value_cart_product_2}"
print("Информация по второму товару успешно проверена\n")

cart_price_product_2 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[2]//div[@class="inventory_item_price"]')
value_cart_price_product_2 = cart_price_product_2.text
print(value_cart_price_product_2)
assert value_price_product_2 == value_cart_price_product_2
print("Информация по цене второго товара успешно проверена\n")


# Переход кликом по кнопке Checkout
btn_checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
btn_checkout.click()
print("Click Checkout")


# Заполнение клиентской информации
first_name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
first_name.send_keys('Petr')
print("Enter First Name")
last_name = driver.find_element(By.XPATH, '//input[@id="last-name"]')
last_name.send_keys('Petrov')
print("Enter Last Name")
zip_code = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
zip_code.send_keys('000000')
print("Enter Zip Code\n")

btn_continue = driver.find_element(By.XPATH, '//input[@id="continue"]')
btn_continue.click()
print("Click Continue\n")

finish_product = lambda number: driver.find_element(By.XPATH, f'(//div[@class="cart_item_label"])[{number}]')
# Финальная инофрмация по первому товару
finish_product_1 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_name"]')
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO Cart Product 1 Good")

finish_price_product_1 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_price"]')
value_finish_price_product_1 = finish_price_product_1.text
print(value_finish_price_product_1)
assert value_price_product_1 == value_finish_price_product_1
print("INFO Cart Price Product 1 Good\n")

# Финальная инофрмация по второму товару
finish_product_2 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[2]//div[@class="inventory_item_name"]')
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("INFO Cart Product 2 Good")

finish_price_product_2 = driver.find_element(By.XPATH, '(//div[@class="cart_item_label"])[2]//div[@class="inventory_item_price"]')
value_finish_price_product_2 = finish_price_product_2.text
print(value_finish_price_product_2)
assert value_price_product_2 == value_finish_price_product_2, f"{value_price_product_2} != {value_finish_price_product_2}"
print("INFO Cart Price Product 2 Good\n")

summary_price = driver.find_element(By.XPATH, f'//div[@class="summary_subtotal_label"]')
value_summary_price = summary_price.text
print(value_summary_price)

total_price_products = float(value_finish_price_product_1.replace("$", "")) + float(value_finish_price_product_2.replace("$", ""))

item_total = f'Item total: ${total_price_products}'
print(item_total)
assert value_summary_price == item_total
print("Total summary price corrected")

sleep(5)
driver.close()
