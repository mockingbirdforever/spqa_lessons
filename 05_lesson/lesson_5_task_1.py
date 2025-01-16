from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()


driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
button = driver.find_element(By.CSS_SELECTOR, 'button')

delete_buttons = []

for i in range(0, 5):
    button.click()
    delete_button = driver.find_element(By.CSS_SELECTOR, 'button.added-manually').text
    delete_buttons.append(delete_button)

print(len(delete_buttons))

