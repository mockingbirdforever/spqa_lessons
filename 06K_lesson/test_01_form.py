from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')


input_element = driver.find_element(By.CSS_SELECTOR, 'first-name')
input_element.send_keys('Skypro')
sleep(5)

driver.quit()
