# Задание 7. Поле ввода

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/inputs")
search_input = driver.find_element(By.TAG_NAME, 'input')
sleep(2)
search_input.send_keys("1000")
sleep(2)
search_input.clear()
sleep(2)
search_input.send_keys("999")

driver.quit()
