from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

waiter = WebDriverWait(driver, 10)
colors = []
user = ["Иван", "Петров", "Ленина, 55-3", "test@skypro.com",
        "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro"]

inputs = ["First_name", "Last_name", "Address", "E-mail",
          "Job-Position", "Company", "Phone", "Country", "City", "Zip_code"]

driver.get(url)

driver.find_element(
    By.CSS_SELECTOR, "input[name='first-name']").send_keys(user[0])
driver.find_element(
    By.CSS_SELECTOR, "input[name='last-name']").send_keys(user[1])
driver.find_element(
    By.CSS_SELECTOR, "input[name='address']").send_keys(user[2])
driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(user[3])
driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(user[4])
driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").clear()
driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(user[6])
driver.find_element(
    By.CSS_SELECTOR, "input[name='country']").send_keys(user[7])
driver.find_element(
    By.CSS_SELECTOR, "input[name='job-position']").send_keys(user[8])
driver.find_element(
    By.CSS_SELECTOR, "input[name='company']").send_keys(user[9])

# ожидание присутствия элемента
button = waiter.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "button[type='submit']")))

# скролл до кнопки
driver.execute_script("arguments[0].scrollIntoView(true);", button)

# Клик по кнопке с помощью JS
driver.execute_script("arguments[0].click();", button)

first_name_color = driver.find_element(
    By.CSS_SELECTOR, "#first-name").value_of_css_property('background-color')
colors.append(first_name_color)

last_name_color = driver.find_element(
    By.CSS_SELECTOR, "#last-name").value_of_css_property('background-color')
colors.append(last_name_color)

address_color = driver.find_element(
    By.CSS_SELECTOR, "#address").value_of_css_property('background-color')
colors.append(address_color)

e_mail_color = driver.find_element(
    By.CSS_SELECTOR, "#e-mail").value_of_css_property('background-color')
colors.append(e_mail_color)

job_position_color = driver.find_element(
    By.CSS_SELECTOR, "#job-position").value_of_css_property('background-color')
colors.append(job_position_color)

company_color = driver.find_element(
    By.CSS_SELECTOR, "#company").value_of_css_property('background-color')
colors.append(company_color)

phone_color = driver.find_element(
    By.CSS_SELECTOR, "#phone").value_of_css_property('background-color')
colors.append(phone_color)

country_color = driver.find_element(
    By.CSS_SELECTOR, "#country").value_of_css_property('background-color')
colors.append(country_color)

city_color = driver.find_element(
    By.CSS_SELECTOR, "#city").value_of_css_property('background-color')
colors.append(city_color)

zip_code_color = driver.find_element(
    By.CSS_SELECTOR, "#zip-code").value_of_css_property('background-color')
colors.append(zip_code_color)

for i in range(0, 10):
    if colors[i] == "rgba(209, 231, 221, 1)":
        print("Поле", inputs[i], "подсвечено зеленым")
    elif colors[i] == "rgba(248, 215, 218, 1)":
        print("Поле", inputs[i], "подсвечено красным")
    else:
        print("Значение цвета не найдено")

driver.quit()
