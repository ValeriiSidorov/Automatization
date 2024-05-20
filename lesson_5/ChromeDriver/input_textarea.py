from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "http://the-internet.herokuapp.com/inputs"

driver.get(url)
input_textarea = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_textarea.send_keys("1000")
input_textarea.clear()
input_textarea.send_keys("999")
