from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
waiter = WebDriverWait(driver, 10)

driver.get(url)

content = driver.find_element(By.CSS_SELECTOR, "div#image-container")

waiter.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "img#landscape")))

images = content.find_elements(By.CSS_SELECTOR, "img")

image_sources = [img.get_attribute('src') for img in images]

print(image_sources[2])

driver.quit()
