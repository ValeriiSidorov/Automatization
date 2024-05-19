import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "http://the-internet.herokuapp.com/login"

driver.get(url)

username = driver.find_element(By.CSS_SELECTOR, "input#username")
username.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
time.sleep(2)

driver.quit()
