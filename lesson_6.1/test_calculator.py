import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    delay = 45
    waiter = WebDriverWait(driver, delay + 1)

    driver.get(url)

    driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys(delay)

    driver.find_element(By.XPATH, f"//span[text()='{7}']").click()
    driver.find_element(By.XPATH, f"//span[text()='{'+'}']").click()
    driver.find_element(By.XPATH, f"//span[text()='{8}']").click()
    driver.find_element(By.XPATH, f"//span[text()='{'='}']").click()

    # ожидаем, пока текст на экране не станет "15"
    result_element = waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )

    res = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    assert int(res) == 15, f"Результат сложения некорректный: {res}"
