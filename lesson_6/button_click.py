from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "http://uitestingplayground.com/ajax"

waiter = WebDriverWait(driver, 20)

driver.get(url)

driver.find_element(By.CSS_SELECTOR, "button#ajaxButton").click()

waiter.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "p.bg-success"), "Data loaded with AJAX get request."))

print(driver.find_element(By.CSS_SELECTOR, "p.bg-success").text)

driver.quit()
