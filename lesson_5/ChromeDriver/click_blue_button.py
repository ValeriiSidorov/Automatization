import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://uitestingplayground.com/classattr"

driver.get(url)
for _ in range(3):
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.refresh()
    time.sleep(2)
