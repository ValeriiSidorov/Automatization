import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

delay = 45
waiter = WebDriverWait(driver, delay)

driver.get(url)

driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys(delay)

driver.find_element(By.XPATH, f"//span[text()='{7}']").click()
driver.find_element(By.XPATH, f"//span[text()='{'+'}']").click()
driver.find_element(By.XPATH, f"//span[text()='{8}']").click()
driver.find_element(By.XPATH, f"//span[text()='{'='}']").click()

time.sleep(delay + 1)

res = driver.find_element(By.CSS_SELECTOR, "div.screen").text
if int(res) == 15:
    print("Результат сложения верный и равен 15")
else:
    print("Результат сложения некорректный")

driver.quit()
