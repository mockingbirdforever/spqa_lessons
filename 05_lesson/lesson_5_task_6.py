from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/login")
username_input = driver.find_element(By.ID, 'username')
sleep(2)

username_input.send_keys("tomsmith")
sleep(3)

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys("SuperSecretPassword!")
sleep(3)

login_button = driver.find_element(By.TAG_NAME, 'button')
login_button.click()
sleep(3)
