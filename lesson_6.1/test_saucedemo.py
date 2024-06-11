import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_purchase(driver):
    url = "https://www.saucedemo.com/"
    waiter = WebDriverWait(driver, 4)

    driver.get(url)

    element_text = driver.find_element(By.CSS_SELECTOR, "div.login_password").text
    password = element_text.split(':')[-1].strip()
    login = "standard_user"

    # Авторизация
    driver.find_element(By.CSS_SELECTOR, "input#user-name").clear()
    driver.find_element(By.CSS_SELECTOR, "input#user-name").send_keys(login)
    driver.find_element(By.CSS_SELECTOR, "input#password").clear()
    driver.find_element(By.CSS_SELECTOR, "input#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input#login-button").click()

    # Покупка товара
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack")))
    driver.find_element(
       By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()

    # Просмотр корзины
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.CSS_SELECTOR, "button#checkout").click()

    # Данные пользователя
    waiter.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input#first-name")))
    driver.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("Ivan")
    driver.find_element(By.CSS_SELECTOR, "input#last-name").send_keys("Petrov")
    driver.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys("192222")
    driver.find_element(By.CSS_SELECTOR, "input#continue").click()

    # Поиск общей суммы
    total_text = driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text
    total = total_text.split(':')[-1].strip()

    assert total == "$58.29", f"Сумма покупок не сходится: {total}"
