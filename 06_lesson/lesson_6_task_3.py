from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 20)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')


pic = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#landscape'))
)

text = driver.find_element(By.CSS_SELECTOR, 'img#award').get_attribute('src')
print(text)

driver.quit()

