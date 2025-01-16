from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()


driver.get("https://the-internet.herokuapp.com/entry_ad")
sleep(5)
stupid_button = driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')

stupid_button.click()

sleep(3)
