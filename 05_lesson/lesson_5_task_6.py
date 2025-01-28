# Задание 8. Форма авторизации

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

driver.find_element(By.ID, 'username').send_keys("tomsmith")
driver.find_element(By.ID, 'password').send_keys("SuperSecretPassword!")
driver.find_element(By.TAG_NAME, 'button').click()

sleep(3)
driver.quit()

