# Задание 6. Модальное окно

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(3)

driver.find_element(By.CSS_SELECTOR, ".modal-footer").click()

sleep(3)
driver.quit()
