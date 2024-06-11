import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form_submission(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    waiter = WebDriverWait(driver, 10)
    colors = []
    user = ["Иван", "Петров", "Ленина, 55-3", "test@skypro.com",
            "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro"]
    inputs = ["first-name", "last-name", "address", "e-mail",
              "phone", "zip-code", "city", "country", "job-position", "company"]

    driver.get(url)

    # Заполнение формы
    driver.find_element(
        By.CSS_SELECTOR, "input[name='first-name']").send_keys(user[0])
    driver.find_element(
        By.CSS_SELECTOR, "input[name='last-name']").send_keys(user[1])
    driver.find_element(
        By.CSS_SELECTOR, "input[name='address']").send_keys(user[2])
    driver.find_element(
        By.CSS_SELECTOR, "input[name='e-mail']").send_keys(user[3])
    driver.find_element(
        By.CSS_SELECTOR, "input[name='phone']").send_keys(user[4])
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear()
    driver.find_element(
        By.CSS_SELECTOR, "input[name='city']").send_keys(user[6])
    driver.find_element(
        By.CSS_SELECTOR, "input[name='country']").send_keys(user[7])
    driver.find_element(
        By.CSS_SELECTOR, "input[name='job-position']").send_keys(user[8])
    driver.find_element(
        By.CSS_SELECTOR, "input[name='company']").send_keys(user[9])

    # Ожидание и клик по кнопке
    button = waiter.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    driver.execute_script("arguments[0].click();", button)

    # Сборка цвета полей
    field_ids = ["first-name", "last-name", "address", "e-mail", "phone",
                 "zip-code", "city", "country", "job-position", "company"]
    for field_id in field_ids:
        color = driver.find_element(
            By.CSS_SELECTOR, f"#{field_id}").value_of_css_property('background-color')
        assert color, f"Цвет поля {field_id} не найден."
        colors.append(color)

    # Проверка цвета полей
    for i, color in enumerate(colors):
        field_name = inputs[i]
        if field_name == "zip-code":
            assert color == "rgba(248, 215, 218, 1)", f"Поле {field_name} должно быть подсвечено красным, но подсвечено {color}"
        else:
            assert color == "rgba(209, 231, 221, 1)", f"Поле {field_name} должно быть подсвечено зеленым, но подсвечено {color}"
