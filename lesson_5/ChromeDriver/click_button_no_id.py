import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = "http://uitestingplayground.com/dynamicid"

driver.get(url)
for _ in range(3):
    driver.find_element(By.CSS_SELECTOR, "h4+button").click()
    driver.refresh()
    time.sleep(2)
