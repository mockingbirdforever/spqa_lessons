from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://ya.ru/")
sleep(5)

driver.fullscreen_window()
sleep(5)

driver.save_screenshot('./ya.png')
