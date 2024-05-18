import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/entry_ad"

driver.get(url)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

driver.quit()
