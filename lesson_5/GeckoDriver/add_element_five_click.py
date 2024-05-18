from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
url = "http://the-internet.herokuapp.com/add_remove_elements/"

driver.get(url)

for _ in range(0, 5):
    driver.find_element(
        By.CSS_SELECTOR, "button[onclick='addElement()']").click()

print(len(driver.find_elements(By.CSS_SELECTOR,
      "button[onclick='deleteElement()']")))

driver.quit()
