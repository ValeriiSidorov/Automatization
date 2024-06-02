from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "http://uitestingplayground.com/textinput"
text = "SkyPro"
waiter = WebDriverWait(driver, 4)

driver.get(url)

content = driver.find_element(By.CSS_SELECTOR, ".form-group")

content.find_element(By.CSS_SELECTOR, "input#newButtonName").send_keys(text)

driver.find_element(By.CSS_SELECTOR, "button#updatingButton").click()

waiter.until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "button#updatingButton"), text))

print(driver.find_element(By.CSS_SELECTOR, "button#updatingButton").text)

driver.quit()
