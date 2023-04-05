"""
4.27 Тестовое задание по Selenium №3
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

base_url = 'https://www.saucedemo.com/'
authorized_url = 'https://www.saucedemo.com/inventory.html'
login_standard_user = 'standard_user'
password_for_all = 'secret_sauce'



print("Приветствую тебя в нашем интернет-магазине")
product = input("Выбери один из следующих товаров и укажи его номер:\n"
                "1 - Sauce Labs Backpack,\n"
                "2 - Sauce Labs Bike Light,\n"
                "3 - Sauce Labs Bolt T-Shirt,\n"
                "4 - Sauce Labs Fleece Jacket,\n"
                "5 - Sauce Labs Onesie,\n"
                "6 - Test.allTheThings() T-Shirt (Red)\n--> ")
driver = webdriver.Chrome()
try:
    if product in ['1', '2', '3', '4', '5', '6']:
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

        # Информация по выбранному товару
        product_1 = driver.find_element(By.XPATH, f'(//div[@class="inventory_item_label"]/a)[{product}]')
        value_product_1 = product_1.text
        print(value_product_1)

        price_product_1 = driver.find_element(By.XPATH, f'(//div[@class="inventory_item_price"])[{product}]')
        value_price_product_1 = price_product_1.text
        print(value_price_product_1)

        select_product_1 = driver.find_element(By.XPATH, f'(//div[@class="inventory_item"])[{product}]//button[text('
                                                         f')="Add to cart"]')
        select_product_1.click()
        print(f"Выбран товар # {product}")

        # Переход в корзину
        not_empty_cart = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
        not_empty_cart.click()
        print("Переход в корзину")

        # Проверяем первый товар в корзине
        cart_product_1 = driver.find_element(By.XPATH,
                                             '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_name"]')
        value_cart_product_1 = cart_product_1.text
        print(value_cart_product_1)
        assert value_product_1 == value_cart_product_1, f"{value_product_1} != {value_cart_product_1}"
        print("Информация по первому товару успешно проверена\n")

        cart_price_product_1 = driver.find_element(By.XPATH,
                                                   '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_price"]')
        value_cart_price_product_1 = cart_price_product_1.text
        print(value_cart_price_product_1)
        assert value_price_product_1 == value_cart_price_product_1
        print("Информация по цене первого товара успешно проверена\n")

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
        finish_product_1 = driver.find_element(By.XPATH,
                                               '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_name"]')
        value_finish_product_1 = finish_product_1.text
        print(value_finish_product_1)
        assert value_product_1 == value_finish_product_1
        print("INFO Cart Product 1 Good")

        finish_price_product_1 = driver.find_element(By.XPATH,
                                                     '(//div[@class="cart_item_label"])[1]//div[@class="inventory_item_price"]')
        value_finish_price_product_1 = finish_price_product_1.text
        print(value_finish_price_product_1)
        assert value_price_product_1 == value_finish_price_product_1
        print("INFO Cart Price Product 1 Good\n")

        summary_price = driver.find_element(By.XPATH, f'//div[@class="summary_subtotal_label"]')
        value_summary_price = summary_price.text
        print(value_summary_price)

        item_total = f'Item total: {value_finish_price_product_1}'
        print(item_total)
        assert value_summary_price == item_total
        print("Total summary price corrected")
    else:
        print("Такого товара не существует")
finally:
    sleep(5)
    driver.close()
